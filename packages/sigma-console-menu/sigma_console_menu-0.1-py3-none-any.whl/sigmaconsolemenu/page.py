from sigmaconsolemenu.menu_option import MenuOption


class Page:
    def __init__(self, id: int, title: str = "") -> None:
        self.id = id
        self.title = title
        self.options: dict[int, MenuOption] = {}

    def add_options(self, *options: MenuOption):
        for option in options:
            self.options[len(list(self.options))] = option
