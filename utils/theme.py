import os
import fade
from pystyle import Colors, Colorate

def redorange(text):
    faded = ""
    green = 0
    for line in text.splitlines():
        faded += f"\033[38;2;255;{green};0m{line}\033[0m\n"
        if green < 165:
            green += 15
            if green > 165:
                green = 165
    return faded

def yelloworange(text):
    faded = ""
    green = 255
    for line in text.splitlines():
        faded += f"\033[38;2;255;{green};0m{line}\033[0m\n"
        if green > 125:
            green -= 20
            if green < 125:
                green = 125
    return faded



def custom_gradient(start_color, end_color, steps):
    start_r, start_g, start_b = start_color
    end_r, end_g, end_b = end_color
    
    gradient = []
    
    for i in range(steps):
        r = int(start_r + (end_r - start_r) * (i / steps))
        g = int(start_g + (end_g - start_g) * (i / steps))
        b = int(start_b + (end_b - start_b) * (i / steps))
        gradient.append(f"\033[38;2;{r};{g};{b}")
    
    return gradient

orange = (255, 165, 0)
yellow = (255, 255, 0)
white = (255, 255, 255)
green_cyan = (6, 249, 167)
cyan = (6, 234, 253)
gray = (101, 101, 101)

yellow_to_white = custom_gradient(yellow, white, 25)
orange_to_white = custom_gradient(orange, white, 25)
gray_to_white = custom_gradient(gray, white, 25)
green_to_cyan = custom_gradient(green_cyan, cyan, 25)

cloudy_primary = f"\033[38;2;{gray[0]};{gray[1]};{gray[2]}m"
tropical_primary = f"\033[38;2;{green_cyan[0]};{green_cyan[1]};{green_cyan[2]}m"


themes = {
    "default": {
        "primary": Colors.red,
        "secondary": Colors.white,
        "fade": Colors.red_to_white,
        "reset": Colors.reset
    },
    "cheese": {
        "primary": Colors.yellow,
        "secondary": Colors.white,
        "fade": yellow_to_white,
        "reset": Colors.reset
    },
    "halloween": {
        "primary": Colors.orange,
        "secondary": Colors.yellow,
        "fade": orange_to_white,
        "reset": Colors.reset
    },
    "ocean": {
        "primary": Colors.blue,
        "secondary": Colors.cyan,
        "fade": Colors.blue_to_cyan,
        "reset": Colors.reset
    },
    "old": {
        "primary": cloudy_primary,
        "secondary": Colors.white,
        "fade": gray_to_white,
        "reset": Colors.reset
    },
    "toxic": {
        "primary": Colors.green,
        "secondary": Colors.white,
        "fade": Colors.green_to_white,
        "reset": Colors.reset
    },
    "tropical": {
        "primary": tropical_primary,
        "secondary": Colors.cyan,
        "fade": green_to_cyan,
        "reset": Colors.reset
    }
}

total_themes = len(themes)

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
    return load_current_theme()

def theme_banner(text):
    current = load_current_theme()
    if tropical_primary in current['primary']:
        return fade.greenblue(text)
    elif cloudy_primary in current['primary']:
        return fade.blackwhite(text)
    elif Colors.blue in current['primary']:
        return fade.water(text)
    elif Colors.green in current['primary']:
        return fade.brazil(text)
    elif Colors.orange in current['primary']:
        return fade.fire(text)
    elif Colors.red in current['primary']:
        return redorange(text)
    elif Colors.yellow in current['primary']:
        return yelloworange(text)
    else:
        no_fade = f"""{current['primary']}{text}{current['reset']}"""
        return no_fade

# Example usage
if __name__ == "__main__":
    print("Current theme:", get_current_theme())
    set_theme("default")
    print("Theme after change:", get_current_theme())