from hashlib import sha256
from os import getenv
from os.path import dirname, exists
from dotenv import load_dotenv


def verify(log: object, console: object) -> bool:
    """Compare the sha256 sum of the filename to the given in .env file"""

    BASE_PATH: str = "/".join(dirname(__file__).split("/")[:-2])
    TD_BASE_PATH: str = f"{BASE_PATH}/training_data"
    TD_PERSONALITY_PATH: str = f"{BASE_PATH}/training_data/personalities"

    load_dotenv(f"{BASE_PATH}/sha256sums.env")

    training_data: list[str] = [
            f"{TD_BASE_PATH}/scripts.json",
            f"{TD_PERSONALITY_PATH}/dandere.json",
            f"{TD_PERSONALITY_PATH}/himedere.json",
            f"{TD_PERSONALITY_PATH}/normal.json",
            f"{TD_PERSONALITY_PATH}/phrases.json",
            f"{TD_PERSONALITY_PATH}/tsundere.json",
            f"{TD_PERSONALITY_PATH}/yandere.json",
        ]
    passed: bool = False

    for data in training_data:
        if not exists(data):
            log.logger(
                "error", f"Training data: {data} does not exists. Aborting."
            )
            return False

        try:
            file_name: str = data.split("/")[-1][:-5]
            shasum: str = getenv(file_name.upper())
            sha256hash = sha256()

            with open(data, "rb") as file:
                while True:
                    chunk = file.read(sha256hash.block_size)
                    if not chunk:
                        break
                    sha256hash.update(chunk)
        except (PermissionError, OSError, SystemError) as Err:
            log.logger("error", f"Exception: {Err} occured. Aborting.")
            return False

        if shasum == sha256hash.hexdigest():
            log.logger(
                "Pinfo", f"Sucessfully verified the integrity of {file_name}."
            )
            passed: bool = True
        else:
            log.logger(
                "Finfo",
                "Failed to verify the integrity of "
                + f"{file_name}, SHA256 sum didn't matched."
            )

    if passed:
        return True

    return False
