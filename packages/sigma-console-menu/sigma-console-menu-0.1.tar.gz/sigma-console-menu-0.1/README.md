## Sigma console menu

A simple menu for console apps in Python

Quick tutorial

```python
# Create a new menu
ui = SigmaConsoleMenu()

# Create a new page
# Page has `id` and `title`, `id` is needed to connect them together
page1 = Page(0, "Menu 1")

# Next step is to create options that you want to display
# Option has `text` and `action`
# `action` can be int or function
# If action is int then it is `id` of page that you want to link
# Otherwise is calling a passed function
option1 = MenuOption("Go to menu 2", 1)
option2 = MenuOption("Something 1", lambda: print("Something 1 was called"))
option3 = MenuOption("Something 2", lambda: print("Something 2 was called"))

# Then you have to add options to the page
page1.add_options(option1, option2, option3)

# Creating 2nd page
page2 = Page(1, "Menu 2")
o1 = MenuOption("Something on page 2", lambda: print("Something on page 2 was called"))

# You can link pages in a circular motion
o2 = MenuOption("Back to Menu 1", 0)

page2.add_options(o1, o2)

# And then add pages to the main menu
ui.add_pages(page1, page2)

ui.run()
```
