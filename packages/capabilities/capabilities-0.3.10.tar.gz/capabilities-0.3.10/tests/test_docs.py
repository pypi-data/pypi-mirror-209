from capabilities import Capability
from pydantic import BaseModel
from capabilities import llm

""" Tests of the examples given in tutorials at docs.blazon.ai """

EXAMPLE_PASSAGE = """\
Wide-scale production is credited to Edward Goodrich Acheson in 1890.[11] Acheson was attempting to prepare artificial diamonds when he heated a mixture of clay (aluminium silicate) and powdered coke (carbon) in an iron bowl. He called the blue crystals that formed carborundum, believing it to be a new compound of carbon and aluminium, similar to corundum. Moissan also synthesized SiC by several routes, including dissolution of carbon in molten silicon, melting a mixture of calcium carbide and silica, and by reducing silica with carbon in an electric furnace. Acheson patented the method for making silicon carbide powder on February 28, 1893.[12] Acheson also developed the electric batch furnace by which SiC is still made today and formed the Carborundum Company to manufacture bulk SiC, initially for use as an abrasive.[13] In 1900 the company settled with the Electric Smelting and Aluminum Company when a judge's decision gave "priority broadly" to its founders "for reducing ores and other substances by the incandescent method".[14] It is said that Acheson was trying to dissolve carbon in molten corundum (alumina) and discovered the presence of hard, blue-black crystals which he believed to be a compound of carbon and corundum: hence carborundum. It may be that he named the material "carborundum" by analogy to corundum, which is another very hard substance (9 on the Mohs scale). The first use of SiC was as an abrasive. This was followed by electronic applications. In the beginning of the 20th century, silicon carbide was used as a detector in the first radios.[15] In 1907 Henry Joseph Round produced the first LED by applying a voltage to a SiC crystal and observing yellow, green and orange emission at the cathode. The effect was later rediscovered by O. V. Losev in the Soviet Union in 1923.[16]\
"""


def test_summarize():
    print(Capability("blazon/summarize")(EXAMPLE_PASSAGE))


def test_structured():
    class WordTranslation(BaseModel):
        source: str
        target: str

    class TranslationOutput(BaseModel):
        translation: str
        word_translations: list[WordTranslation]

    @llm
    def translate(input_text: str) -> TranslationOutput:
        """Given the input `text`, produces a `french_translation`
        which translates the `text` into French.
        Also produce a word-level translation called `word_translations`,
        which is a list of (english word, french transliteration) pairs.
        """
        ...

    # create an input instance
    inp = "Understand: I'll slip quietly away through twilit meadows with only this one dream - you come too."

    # print the task to console
    translation_output = translate(inp)
    print(translation_output)


def test_structured_old_demo():
    from pydantic import BaseModel
    from capabilities import Capability

    # define the input and output models
    class InputText(BaseModel):
        text: str

    class WordTranslation(BaseModel):
        source: str
        target: str

    class TranslationOutput(BaseModel):
        translation: str
        word_translations: list[WordTranslation]

    # create an input instance
    inp = InputText(
        text="Understand: I'll slip quietly away through twilit meadows with only this one dream - you come too."
    )

    # provide some instructions
    instructions = "Given the input `text`, produce a `french_translation` which translates the `text` into French. Also produce a word-level translation called `word_translations`, which is a list of (english word, french transliteration) pairs."

    # print the task to console
    c = Capability("blazon/structured")
    translation_output: TranslationOutput = c(
        InputText, TranslationOutput, instructions, inp
    )
    print(translation_output)


def test_document_qa():
    c = Capability("blazon/document_qa")
    question = "Who formed the Carborundum Company?"
    answer = c(EXAMPLE_PASSAGE, question)
    print("Result: ", answer)
    print(
        "Formatted result: ",
        "- " + "\n- ".join(bp["bullet_point"] for bp in answer["answer"]["claims"]),
    )


def test_tutorial():
    class PrimeFactor(BaseModel):
        prime: int
        exponent: int

    class PrimeFactorization(BaseModel):
        factors: list[PrimeFactor]

    @llm
    def factor_primes(number: int) -> PrimeFactorization:
        """
        Return a prime factorization of the `number` as a list of pairs of a `prime`s and `exponent`s.
        """
        ...

    def check_result(number: int, fac: PrimeFactorization):
        product = 1

        for prime_factor in fac.factors:
            product *= prime_factor.prime**prime_factor.exponent

        return number == product

    n = 85
    result = factor_primes(n)
    print(result, check_result(n, result))


def test_fruits():
    @llm
    def fruit_emojis(n: int) -> list[str]:
        """Generates a list of fruit emojies of the given length.

        Example:
            >>> fruit_emojis(4) == ['🍎', '🍏', '🍊', '🍋']
        """
        ...

    for n in [0, 1, 2, 4, 10]:
        result = fruit_emojis(n)
        assert len(result) == n
        print(result)


if __name__ == "__main__":
    test_summarize()
    test_structured()
    test_document_qa()
    test_tutorial()
