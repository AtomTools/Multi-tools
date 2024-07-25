from pystyle import Colors, Colorate

themes = {
    "default": {
        "primary": Colors.red,
        "secondary": Colors.white,
        "reset": Colors.reset
    },
    "blue_theme": {
        "primary": Colors.blue,
        "secondary": Colors.white,
        "reset": Colors.reset
    },
    "green_theme": {
        "primary": Colors.green,
        "secondary": Colors.white,
        "reset": Colors.reset
    },
    "purple_theme": {
        "primary": Colors.purple,
        "secondary": Colors.white,
        "reset": Colors.reset
    },
    "cyan_theme": {
        "primary": Colors.cyan,
        "secondary": Colors.white,
        "reset": Colors.reset
    },
    "yellow_theme": {
        "primary": Colors.yellow,
        "secondary": Colors.white,
        "reset": Colors.reset
    },
    "gray_theme": {
        "primary": Colors.gray,
        "secondary": Colors.white,
        "reset": Colors.reset
    },
}

current_theme = themes["default"]

def set_theme(theme_name):
    global current_theme
    if theme_name in themes:
        current_theme = themes[theme_name]
    else:
        print(f"{Colors.red}Theme '{theme_name}' not found. Using default theme.{Colors.reset}")
        current_theme = themes["default"]

def get_current_theme():
    return current_theme
