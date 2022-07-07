import enchant
from difflib import SequenceMatcher

from src.utils.word_tools.correct_words_ref import correct_words_ref


def correct_spelling(message: str) -> list[str]:
    """Correct the spelling of the words based on percent difference.

    Arguments:
    message: str -- message or string.

    Returns list of presumably corrected strings.
    """

    suggest: object = enchant.Dict("en_US")

    # annotations
    perc_diff: float; msg: str; word: str; word_ref: str

    def word_suggest(word: str, suggest_: object) -> list[str] | bool:
        """Find a word replacement for the incorrect word."""

        for word_ref in next(correct_words_ref()):
            if (perc_diff := SequenceMatcher(word_ref, word)) > 0.75:
                suggest.check(word)
                suggestions: list[str]
                if (suggestions := suggest.suggest(word)) is not None:
                    return suggestions

                return False

    msg_arr: list[str] = message.split(" ")

    corrected_words: list[str] = []
    for msg in msg_arr:
        suggestions: list[str] | bool = word_suggest()
        if isinstance(suggestions, bool):
            continue

        for word in suggestions:
            if (perc_diff := SequenceMatcher(word, msg)) > 0.85:
                corrected_words.append(word)
            else:
                corrected_words.append(msg)
            break

    return corrected_words
