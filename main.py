import os
import sys
import time
import threading
import subprocess
import json
from utils.theme import set_theme, get_current_theme, theme_banner, themes

if os.name == 'nt':
    import msvcrt
else:
    import tty
    import termios

def read_requirements(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip() and not line.startswith('#')]

def read_tools_info(json_path):
    with open(json_path, 'r') as file:
        data = json.load(file)
    return data


try:
    import pkg_resources
    import fade
    from blessed import Terminal
    from pystyle import Add, Anime, Center, Colorate, Colors, Cursor, Write
except Exception as e:
    print(e)

term = Terminal()

def get_choice_windows(prompt):
    print(prompt, end='', flush=True)

    choice = ""
    
    while True:
        char = msvcrt.getch()
        
        if char == b'\x1b':
            next1, next2 = msvcrt.getch(), msvcrt.getch()
            if next1 == b'[':
                if next2 == b'C':
                    return 'next'
                elif next2 == b'D':
                    return 'prev'
        elif char in [b'\r', b'\n']:
            print()
            return choice.strip()
        elif char == b'>':
            return 'next'
        elif char == b'<':
            return 'prev'
        elif char == b'?':
            return '?'
        elif char == b'=':
            return '='
        elif char == b'\x08':
            if choice:
                choice = choice[:-1]
                sys.stdout.write('\b \b')
                sys.stdout.flush()
        elif char == b'\x03':  # Ctrl+C
            raise KeyboardInterrupt
        elif char == b'\x04':  # Ctrl+D
            raise EOFError
        elif char == b'\x1a':  # Ctrl+Z
            raise KeyboardInterrupt
        else:
            choice += char.decode()
            sys.stdout.write(char.decode())
            sys.stdout.flush()

def get_choice_unix(prompt):
    print(prompt, end='', flush=True)

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    
    try:
        tty.setraw(sys.stdin.fileno())
        choice = ""
        
        while True:
            char = sys.stdin.read(1)
            
            if char == '\x1b':
                next1, next2 = sys.stdin.read(1), sys.stdin.read(1)
                if next1 == '[':
                    if next2 == 'C':
                        return 'next'
                    elif next2 == 'D':
                        return 'prev'
            elif char in ['\r', '\n']:
                print()
                return choice.strip()
            elif char == '>':
                return 'next'
            elif char == '<':
                return 'prev'
            elif char == '?':
                return '?'
            elif char == '=':
                return '='
            elif char == '\x7f':
                if choice:
                    choice = choice[:-1]
                    sys.stdout.write('\b \b')
                    sys.stdout.flush()
            elif char == '\x03':  # Ctrl+C
                raise KeyboardInterrupt
            elif char == '\x04':  # Ctrl+D
                raise EOFError
            elif char == '\x1a':  # Ctrl+Z
                raise KeyboardInterrupt
            else:
                choice += char
                sys.stdout.write(char)
                sys.stdout.flush()
    except (KeyboardInterrupt, EOFError):
        return 'exit'
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def clear():
    system = os.name
    if system == 'nt':
        os.system('cls')
    elif system == 'posix':
        os.system('clear')
    else:
        print('\n'*120)
    return

def animated_text(text, delay=0.05):
    for line in text.split('\n'):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        sys.stdout.write('\n')
        sys.stdout.flush()
        time.sleep(delay)


def get_scripts():
    scripts = []
    for root, _, files in os.walk('utils'):
        for file in files:
            if file.endswith('.py') and root != 'utils':
                category = os.path.basename(root)
                script_name = os.path.splitext(file)[0].replace('_', ' ').title()
                scripts.append((script_name, category))
    return scripts

def calculate_total_length(entry_number, entry_script, entry_category):
    return len(entry_number) + len(entry_script) + len(entry_category)

def add_spaces(entry, total_length, target_length):
    return entry + ' ' * (target_length + total_length)

def display_ascii_art(page_scripts, page_number, total_pages, tools_info, current_theme):
    developers = " x ".join(tools_info['developers'])
    version = tools_info['version']

    entries_per_page = 30
    total_entries = len(page_scripts)
    lines_per_page = (total_entries + 2) // 3

    text_color = f"{current_theme['primary']}AA{current_theme['reset']}{current_theme['secondary']}BBBBBBBBBB{current_theme['reset']}{current_theme['primary']}CCCCCCCCC{current_theme['reset']}"
    add_color = len(text_color)
    line_width = add_color

    split = f"                            "
    bar_old = f"                            ─────────────────────────────────────────────────────────────────────────────────────────────────────────" 
    lbar = "─" * 105
    bar = f"{split}{lbar}"

    art = theme_banner(f"""
                                         ▄▄▄· ▄▄▄▄▄      • ▌ ▄ ·.     • ▌ ▄ ·. ▄• ▄▌▄▄▌  ▄▄▄▄▄▪      ▄▄▄▄▄            ▄▄▌  .▄▄ · 
                                        ▐█ ▀█ •██  ▪     ·██ ▐███▪    ·██ ▐███▪█▪██▌██•  •██  ██     •██  ▪     ▪     ██•  ▐█ ▀. 
                                        ▄█▀▀█  ▐█.▪ ▄█▀▄ ▐█ ▌▐▌▐█·    ▐█ ▌▐▌▐█·█▌▐█▌██▪   ▐█.▪▐█·     ▐█.▪ ▄█▀▄  ▄█▀▄ ██▪  ▄▀▀▀█▄
                                        ▐█ ▪▐▌ ▐█▌·▐█▌.▐▌██ ██▌▐█▌    ██ ██▌▐█▌▐█▄█▌▐█▌▐▌ ▐█▌·▐█▌     ▐█▌·▐█▌.▐▌▐█▌.▐▌▐█▌▐▌▐█▄▪▐█
                                         ▀  ▀  ▀▀▀  ▀█▄▀▪▀▀  █▪▀▀▀    ▀▀  █▪▀▀▀ ▀▀▀ .▀▀▀  ▀▀▀ ▀▀▀     ▀▀▀  ▀█▄▀▪ ▀█▄▀▪.▀▀▀  ▀▀▀▀ 
""")

    art += f"""{current_theme["primary"]}
                                                          Developers : {current_theme['reset']}{current_theme["secondary"]}{developers}{current_theme['reset']}{current_theme["primary"]}
{bar}
                                                                         Version : {current_theme['reset']}{current_theme["secondary"]}{version}{current_theme['reset']}{current_theme["primary"]}
{bar}
"""

    for i in range(lines_per_page):
        line = ""
        for j in range(3):
            if(total_entries < 30):
             index = i * 3 + j
            else:
             if j == 0:
                index = i
             elif j == 1:
                index = i + 10
             elif j == 2:
                index = i + 20
            if index < total_entries:
                total_lenght = ""
                spaces2 =  " " * 15
                script, category = page_scripts[index]
                script_number = (page_number - 1) * entries_per_page + index + 1
                entry_number = f"{current_theme['primary']}{script_number}{current_theme['reset']}"
                entry_script = f"{current_theme['secondary']}{script}{current_theme['reset']}"
                entry_category = f"{current_theme['primary']}({category.title()}){current_theme['reset']}"

                total_length = calculate_total_length(entry_number, entry_script, entry_category)
                spaces_to_add = total_length - line_width
                spaces = ""
                if spaces_to_add < 0:
                 spaces = " " * abs(spaces_to_add)
                elif spaces_to_add > 0:
                 spaces2 = spaces2[:-spaces_to_add]

                if j == 0:
                 line += f"                            {entry_number} {entry_script} {entry_category}{spaces}{spaces2}"
                elif j == 1:
                 line += f"{entry_number} {entry_script} {entry_category}{spaces}{spaces2}"
                else:
                 line += f"{entry_number} {entry_script} {entry_category}"

            else:
                line += " " * line_width

        art += line + "\n"

    if art.endswith("\n"):
        art = art[:-1]

    art += f"""
{current_theme["primary"]}{bar}
                                                                          Page : {current_theme['reset']}{current_theme["secondary"]}{page_number}{current_theme['reset']}{current_theme["primary"]}-{current_theme['reset']}{current_theme["secondary"]}{total_pages}{current_theme['reset']}{current_theme["primary"]}
{bar}{current_theme["reset"]}\n"""

    art += f"                            "
    if page_number > 1:
         art += f"\t\t    {current_theme['primary']}<{current_theme['reset']} {current_theme['secondary']}Prev{current_theme['reset']}   "
    art += f"\t\t\t{current_theme['primary']}={current_theme['reset']} {current_theme['secondary']}Theme{current_theme['reset']}\t\t\t  {current_theme['primary']}?{current_theme['reset']} {current_theme['secondary']}Info{current_theme['reset']}\t\t"
    if page_number < total_pages:
        art += f"    {current_theme['primary']}>{current_theme['reset']} {current_theme['secondary']}Next{current_theme['reset']}"
    
    animated_text(art, delay=0)

def execute_script(script_name):
    try:
        if "utils" in script_name:
            script_path = script_name
        else:
            script_path = os.path.join('utils', script_name)
        subprocess.run([sys.executable, script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running the script {script_path}: {e}")

def display_icon(icon_text):
    icon_lines = icon_text.splitlines()
    total_lines = len(icon_lines)
    display_time = 1.5
    interval = display_time / total_lines

    for line in icon_lines:
        animated_text(Colors.green + line + Colors.reset + "\n", delay=0.01)
        time.sleep(interval)

def blink_warning_centered():
    Cursor.HideCursor()
    ascii_art = """
██     ██  █████  ██████  ███    ██ ██ ███    ██  ██████  
██     ██ ██   ██ ██   ██ ████   ██ ██ ████   ██ ██       
██  █  ██ ███████ ██████  ██ ██  ██ ██ ██ ██  ██ ██   ███ 
██ ███ ██ ██   ██ ██   ██ ██  ██ ██ ██ ██  ██ ██ ██    ██ 
 ███ ███  ██   ██ ██   ██ ██   ████ ██ ██   ████  ██████ 
"""

    orange_text = Colors.orange + ascii_art + Colors.reset

    text_width = max(len(line) for line in ascii_art.splitlines())
    text_height = len(ascii_art.splitlines())

    with term.cbreak(), term.hidden_cursor():
        x = (term.width // 2) - (text_width // 2)
        y = (term.height // 2) - (text_height // 2)
        
        for _ in range(4):
            for i, line in enumerate(orange_text.splitlines()):
                print(term.move_xy(x, y + i) + line, end='', flush=True)
            time.sleep(0.25)
            for i in range(text_height):
                print(term.move_xy(x, y + i) + ' ' * text_width, end='', flush=True)
            time.sleep(0.25)
        
        print(term.clear(), end='', flush=True)
        print(term.move_xy(0, 0), end='', flush=True)


def warning_animation():
    icon_text = f"""
      ____               
     /___/\_     
    _\   \/_/\__  
  __\       \/_/\  
  \   __    __ \ \  
 __\  \_\   \_\ \ \  __  
/_/\\   __   __  \ \_/_/\          
\_\/_\__\/\__\/\__\/_\_\/             
   \_\/_/\       /_\_\/
      \_\/       \_\/

"""
    

    warning_message = """The use of these tools can have significant
risks and consequences. By using this software, you
agree that we are not responsible for any damage or
issues that may arise from the use of these tools.
Please use responsibly and at your own risk.

"""

    blink_warning_centered()

    combined_message = Add.Add(icon_text, warning_message, 3)
    
    Write.Print(Center.Center(combined_message),get_current_theme()['primary'], interval=0.0025)
    Write.Input("Press Enter to continue...", get_current_theme()['fade'], interval=0.1)
    
def main():
    clear()

    current_theme = get_current_theme()

    warning_animation()
    
    username = os.getlogin()
    scripts = get_scripts()
    tools_info = read_tools_info('utils/tools.json')
    page_size = 30
    total_pages = (len(scripts) + page_size - 1) // page_size
    current_page = 1

    while True:
        clear()
        current_theme = get_current_theme()
        page_scripts = scripts[(current_page-1)*page_size:current_page*page_size]
        display_ascii_art(page_scripts, current_page, total_pages, tools_info, current_theme)

        prompt = f"""
{current_theme["primary"]}╭─── {current_theme["secondary"]}{username}@Atom
{current_theme["primary"]}│
{current_theme["primary"]}╰─$ {current_theme["reset"]} """
        Cursor.ShowCursor()
        if os.name == 'nt':
         choice = get_choice_windows(prompt)
        else:
         choice = get_choice_unix(prompt)
        
        if choice.isdigit():
            script_index = int(choice) - 1
            if 0 <= script_index < len(page_scripts):
                script_name, category = page_scripts[script_index]
                script_path = os.path.join('utils', category, script_name.replace(' ', '_').lower() + '.py')
                execute_script(script_path)
        elif choice == '?':
            execute_script("tools_info.py")
        elif choice == '=':
            execute_script("theme_page.py")
        elif choice == ':':
            print("\nAvailable themes:")
            for i, theme_name in enumerate(themes.keys(), 1):
                print(f"{themes[theme_name]['primary']}{i}. {theme_name}{themes[theme_name]['reset']}")
            theme_choice = input("Choose a theme by number: ").strip()
            theme_names = list(themes.keys())
            try:
                theme_index = int(theme_choice) - 1
                if 0 <= theme_index < len(theme_names):
                    set_theme(theme_names[theme_index])
                    clear()
                else:
                    print(f"{get_current_theme()['primary']}Invalid choice. No theme changed.{get_current_theme()['reset']}")
            except ValueError:
                print(f"{get_current_theme()['primary']}Invalid input. Please enter a number.{get_current_theme()['reset']}")
        elif choice == 'next' and current_page < total_pages:
            Cursor.HideCursor()
            clear()
            display_ascii_art(page_scripts, current_page, total_pages, tools_info, current_theme)
            Cursor.ShowCursor()
            current_page += 1
        elif choice == 'prev' and current_page > 1:
            Cursor.HideCursor()
            clear()
            display_ascii_art(page_scripts, current_page, total_pages, tools_info, current_theme)
            Cursor.ShowCursor()
            current_page -= 1
        elif choice == 'exit':
            print('\n')
            break
        else:
            print(f"\n{get_current_theme()['primary']}Invalid choice. Please try again.{get_current_theme()['reset']}")
            time.sleep(0.5)

if __name__ == "__main__":
    main()
    