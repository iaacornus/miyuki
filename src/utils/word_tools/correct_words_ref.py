from io import TextIOWrapper
from os.path import dirname
from typing import Generator
from json import load


def correct_words_ref(log: object) -> Generator:
    """Fetch the correct words retrived from dictionary.

    Returns a generator.
    """

    BASE_DIR: str = "/".join(dirname(__file__).split("/")[:-3])
    PATH: str = f"{BASE_DIR}/database/word_database.json"

    try:
        word_db_: TextIOWrapper
        with open(PATH, "r", encoding="utf-8") as word_db_:
            word_db: dict[str, list[str]] = load(word_db_)
    except (
            FileNotFoundError,
            IOError,
            PermissionError,
            SystemExit
        ) as exception:
        log.logger("error", f"Exception: {exception} raised, aborting ...")
        raise SystemExit
    else:
        word: str
        for word in word_db.values():
            yield word.lower()
