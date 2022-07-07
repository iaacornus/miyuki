from io import TextIOWrapper
from os.path import dirname
from os import walk
from json import load
from typing import NoReturn


def fetch_script(log: object) -> None | NoReturn:
    """Fetch the training data from the curated scripts stored in json file."""

    BASE_DIR: str = "/".join(dirname(__file__).split("/")[:-2])
    PATH: str = f"{BASE_DIR}/training_data"
    PATH_PERSONALITIES: str = f"{BASE_DIR}/training_data/personalities"

    log.logger("proc_info", f"Fetching scripts from {PATH} ...")

    try:
        training_data: dict[str, str] = {}
        scripts: TextIOWrapper
        with open(f"{PATH}/scripts.json", "r", encoding="utf-8") as scripts:
            script: dict[str, str] = load(scripts)

        for script_num, lines in script.items():
            training_data[f"general_script_{script_num}"] = lines

        training_data["general_responses"] = script["phrases"]

        for file in next(walk(PATH_PERSONALITIES))[2]:
            with open(
                    f"{PATH_PERSONALITIES}/{file}", "r", encoding="utf-8"
                ) as personality_script:
                script: dict[str, str] = load(personality_script)
                for i in range(len(script)):
                    training_data[
                            f"{file.split('.')[0]}_{i}"
                        ] = script[f"script_{i}"]
    except (
            FileNotFoundError,
            PermissionError,
            IOError,
            SystemError
        ) as exception:
        log.logger("error", f"Exception: {exception} raised, aborting ...")
        raise SystemExit
    else:
        log.logger("success", "Training data fetched successfully.")
        return training_data
