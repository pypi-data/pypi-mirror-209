import logging
import keyboard

from sigmaconsolemenu.helpers import cls
from sigmaconsolemenu.page import Page
from sigmaconsolemenu.pointer import Pointer


class SigmaConsoleMenu:
    def __init__(self) -> None:
        self.pages: dict[int, Page] = {}
        self.page_number: int = 0
        self.pointer: Pointer = None
        keyboard.on_press(self._handle_input)
        pass

    def _go_to_page(self, page_number: int) -> None:
        self.page_number = page_number
        self.pointer = Pointer(self.pages[self.page_number], self._go_to_page)
        self._render_page()

    def _handle_input(self, event: keyboard.KeyboardEvent) -> None:
        if self.pointer is None:
            return
        if event.name == "up":
            self.pointer.go_up()
        elif event.name == "down":
            self.pointer.go_down()
        elif event.name == "enter":
            self.pointer.action()
            return
        else:
            return
        self._render_page()

    def _render_page(self) -> None:
        cls()
        print(self.pages[self.page_number].title)
        for id, option in self.pages[self.page_number].options.items():
            print(option.text, end="")
            if id == self.pointer.position:
                print("   <---")
            else:
                print("")

    def _validate(self):
        if len(list(self.pages)) < 1:
            raise Exception("No page was added!")
        for page in self.pages.values():
            for option in page.options.values():
                if isinstance(option.action, int):
                    if option.action not in self.pages.keys():
                        raise Exception("Option go to not existing page!")

    def add_pages(self, *pages: Page):
        for page in pages:
            if page.id in self.pages.keys():
                raise Exception("Can not add page with the same id!")
            self.pages[page.id] = page

    def run(self) -> None:
        self._validate()
        self.pointer = Pointer(self.pages[list(self.pages)[0]], self._go_to_page)
        self._render_page()
        keyboard.wait("esc")
        logging.info("App exited!")
