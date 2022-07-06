import logging
from typing import Optional

from rich.logging import RichHandler


class Logger:
    """Custom logger."""

    def __init__(self) -> None:
        logging.basicConfig(
            format="%(message)s",
            level=logging.INFO,
            datefmt="[%X]",
            handlers=[RichHandler()]
        )
        RichHandler.KEYWORDS = [
                "!>>",
                "+>>",
                "[!]",
                "[>]"
            ]
        self.log: object = logging.getLogger("rich")
        file_log: object = logging.FileHandler(filename="iota-2.log")

        file_log.setLevel(logging.INFO)
        file_log.setFormatter(logging.Formatter("%(levelname)s %(message)s"))
        self.log.addHandler(file_log)

    def logger(self, exception_: str, message: str) -> None:
        """Log the proccesses using passed message and exception_ variable.

        Arguments:
        exception_: str, determines what type of log level to use
            (a.) "error" for major error that crashed the program
            (b.) "Finfo" for failed subprocesses
            (c.) "subinfo" to simply log the happening subprocesses
            (d.) "proc_info" for major processes
            (e.) "info" for information about the process
        message: str, message to be logged.
        """

        match exception_:
            case "error": # for major error
                self.log.error(f"[!] {message}")
            case "Finfo":
                # for failed subprocesses, but handled by exception
                self.log.warning(f"!>> {message}")
            case "subinfo": # normal subprocess information
                self.log.info(f">>> {message}")
            case "proc_info": # for major processes
                self.log.info(f"[>] {message}")
            case "info": # to print information in the terminal
                self.log.info(f"[=] {message}")
