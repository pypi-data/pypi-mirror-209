from typing import Callable
from sigmaconsolemenu.page import Page


class Pointer:
    def __init__(self, page: Page, go_to_page: Callable[[int], None]) -> None:
        self.page = page
        self.options = self.page.options
        self.position = 0
        self.options_len = len(self.options)
        self.go_to_page = go_to_page

    def go_up(self) -> None:
        self.position -= 1
        if self.position < 0:
            self.position = self.options_len - 1

    def go_down(self) -> None:
        self.position += 1
        if self.position > self.options_len - 1:
            self.position = 0

    def action(self) -> None:
        action = self.options[self.position].action
        if isinstance(action, int):
            self.go_to_page(action)
        if isinstance(action, Callable):
            action()
