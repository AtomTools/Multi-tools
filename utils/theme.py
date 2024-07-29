import os
from pystyle import Colors, Colorate

themes = {
    "default": {
        "primary": Colors.red,
        "secondary": Colors.white,
        "reset": Colors.reset
    },
    "Fire": {
        "primary": Colors.yellow,
        "secondary": Colors.red,
        "reset": Colors.reset
    },
    "Ocean": {
        "primary": Colors.blue,
        "secondary": Colors.cyan,
        "reset": Colors.reset
    },
    "Toxic": {
        "primary": Colors.green,
        "secondary": Colors.white,
        "reset": Colors.reset
    },
}

THEME_FILE = os.path.join('utils', 'theme.txt')

def save_current_theme(theme_name):
    with open(THEME_FILE, 'w') as f:
        f.write(theme_name)

def load_current_theme():
    if os.path.exists(THEME_FILE):
        with open(THEME_FILE, 'r') as f:
            theme_name = f.read().strip()
            if theme_name in themes:
                return themes[theme_name]
    return themes["default"]

current_theme = load_current_theme()

def set_theme(theme_name):
    global current_theme
    if theme_name in themes:
        current_theme = themes[theme_name]
        save_current_theme(theme_name)
    else:
        print(f"Theme '{theme_name}' not found. Using default theme.")
        current_theme = themes["default"]
        save_current_theme("default")

def get_current_theme():
    return current_theme

# Example usage
if __name__ == "__main__":
    print("Current theme:", get_current_theme())
    set_theme("default")
    print("Theme after change:", get_current_theme())