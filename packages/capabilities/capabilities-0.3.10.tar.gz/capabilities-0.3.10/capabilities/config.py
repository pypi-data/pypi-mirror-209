import asyncio
from dataclasses import dataclass
import os
import time
from typing import Optional
import warnings
import aiohttp
import pydantic
from pathlib import Path
import requests
from rich import print
import sys
import logging
from capabilities.util.config import SecretPersist, get_app_config_dir
from capabilities.search.oai import CONFIG as OAI
from capabilities.search.oai import AzureOpenAISettings

AOAI = AzureOpenAISettings()

logger = logging.getLogger(__name__)

_OPENAI_FORWARD_WARNED = False
_AZURE_FORWARD_WARNED = False


class CapabilitiesClientError(Exception):
    pass


class CapabilitiesServerError(Exception):
    pass


class Config(pydantic.BaseSettings, SecretPersist):
    api_key: Optional[pydantic.SecretStr] = pydantic.Field(default=None, is_secret=True)
    api_url: str = "https://api.blazon.ai"
    forward_openai: bool = False
    """ If this value is true, capabilities will forward your OPENAI_API_KEY to the capabilities API if it is present.

    This is useful if you want to use credits on your own OpenAI account or want to avoid rate limits.
    The capabilities server only knows this key for the duration of the API call. It is not stored.
    """
    forward_azure: bool = False
    """ If this value is true, capabilities will forward your AZURE_OPENAI_API_KEY to the capabilities API if it is present.

    This is useful if you want to use credits on your own OpenAI account or want to avoid rate limits.
    The capabilities server only knows this key for the duration of the API call. It is not stored.
    """

    config_dir: Path = pydantic.Field(
        default_factory=lambda: get_app_config_dir("capabilities")
    )

    @property
    def secrets_file(self) -> Optional[Path]:
        if self.config_dir.exists():
            return self.config_dir / "secrets.json"
        else:
            return None

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        env_prefix = "CAPABILITIES_"
        secret_postfix = lambda self: self.api_url

    def get_api_key(self) -> Optional[str]:
        api_key = self.get_secret("api_key")
        if api_key is None and not getattr(self, "_api_key_warned", False):
            print(
                (
                    r" \[[red bold]warning[/]\] "
                    "CAPABILITIES_API_KEY not set, get one here: https://blazon.ai/signin"
                    "then try `capabilities login ${paste_api_key_here}`"
                    "\n"
                ),
                file=sys.stderr,
            )
            self._api_key_warned = True
        assert isinstance(api_key, Optional[str])
        return api_key

    def get_headers(self) -> dict:
        k = self.get_api_key()
        if k is None:
            raise ValueError(
                "CAPABILITIES_API_KEY not set, get one here: https://blazon.ai/signin"
            )
        return {
            "Content-Type": "application/json",
            "api-key": self.get_api_key(),
        }

    def _get_payload(self, payload: dict) -> dict:
        payload = dict(**payload)
        if "clients" not in payload:
            payload["clients"] = []
        if self.forward_openai and OAI.api_key is not None:
            global _OPENAI_FORWARD_WARNED
            if not _OPENAI_FORWARD_WARNED:
                logger.warn("WARNING: forwarding OPENAI_API_KEY to capabilities API")
                _OPENAI_FORWARD_WARNED = True
            payload["clients"] += [
                {"api_key": OAI.api_key.get_secret_value(), "api_url": OAI.api_url}
            ]
        if self.forward_azure and AOAI.api_key is not None:
            global _AZURE_FORWARD_WARNED
            if not _AZURE_FORWARD_WARNED:
                logger.warn(
                    "WARNING: forwarding AZURE_OPENAI_API_KEY to capabilities API"
                )
                _AZURE_FORWARD_WARNED = True
            payload["clients"] += [
                {"api_key": AOAI.api_key.get_secret_value(), "api_url": AOAI.api_url}
            ]
        return payload

    def post_sync(self, endpoint, payload):
        patience = 8
        count = 0
        headers = self.get_headers()
        url = f"{self.api_url}{endpoint}"
        payload = self._get_payload(payload)
        while True:
            try:
                resp = requests.post(url, json=payload, headers=headers)
                if resp.status_code >= 400:
                    j = resp.json()
                    if 500 > resp.status_code:
                        raise CapabilitiesClientError(j["message"])
                    else:
                        raise CapabilitiesServerError(j["message"])
                resp.raise_for_status()
                return resp.json()
            except CapabilitiesServerError as e:
                if count >= patience:
                    raise e
                sleep_duration = 2.0**count
                logger.error(str(e))
                logger.info(f"retrying after sleeping for {sleep_duration:.2f} seconds")
                count += 1
                time.sleep(sleep_duration)

    async def post_async(self, endpoint, payload):
        patience = 8
        count = 0
        headers = self.get_headers()
        url = f"{self.api_url}{endpoint}"
        payload = self._get_payload(payload)
        while True:
            try:
                async with aiohttp.ClientSession(
                    connector=aiohttp.TCPConnector(ssl=False)
                ) as session:
                    async with session.post(url, json=payload, headers=headers) as resp:
                        if resp.status >= 400:
                            j = await resp.json()
                            message = j["message"]
                            if 500 > resp.status:
                                raise CapabilitiesClientError(message)
                            else:
                                raise CapabilitiesServerError(message)
                        return await resp.json()
            except CapabilitiesServerError as e:
                if count >= patience:
                    raise e
                sleep_duration = 2.0**count
                logger.exception(e)
                logger.info(f"retrying after sleeping for {sleep_duration:.2f} seconds")
                count += 1
                await asyncio.sleep(sleep_duration)


CONFIG = Config()
