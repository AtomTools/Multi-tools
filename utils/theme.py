from pystyle import Colors, Colorate

themes = {
    "default": {
        "primary": Colors.red,
        "secondary": Colors.white,
        "reset": Colors.reset
    },
    "fire": {
        "primary": Colors.yellow,
        "secondary": Colors.red,
        "reset": Colors.reset
    },
    "ocean": {
        "primary": Colors.blue,
        "secondary": Colors.cyan,
        "reset": Colors.reset
    },
    "toxic": {
        "primary": Colors.green,
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
        print(f"Theme '{theme_name}' not found. Using default theme.")
        current_theme = themes["default"]

def get_current_theme():
    return current_theme
