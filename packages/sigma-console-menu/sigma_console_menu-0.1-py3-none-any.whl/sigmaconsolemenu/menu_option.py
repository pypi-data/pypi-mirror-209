from typing import Callable


class MenuOption:
    def __init__(self, text: str, action: Callable | int) -> None:
        self.text = text
        self.action = action
