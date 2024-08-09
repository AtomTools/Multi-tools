import os
import sys
import time
import threading
from pystyle import Add, Center, Cursor

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.theme import set_theme, get_current_theme, total_themes, themes

python_version = sys.version_info

Cursor.HideCursor()

def clear():
    system = os.name
    if system == 'nt':
        os.system('cls')
    elif system == 'posix':
        os.system('clear')
    else:
        print('\n'*120)
    return

def count_digits(number):
    return len(str(abs(number))) 

tc = count_digits(total_themes)
prev = 0

def execute_choice(user_input):
    global prev
    try:
        theme_index = int(user_input) - 1
        theme_names = list(themes.keys())
        if 0 <= theme_index < len(theme_names):
            set_theme(theme_names[theme_index])
            clear()
            main()
        else:
            print(f"\n{get_current_theme()['primary']}Invalid choice. No theme changed.{get_current_theme()['reset']}")
            time.sleep(2)
            clear()
            main()
    except ValueError:
        if prev == 1:
            stop_event.set()
            clear()
        print(f"\n{get_current_theme()['primary']}Invalid input. Please enter a number.{get_current_theme()['reset']}")
        time.sleep(2)
        clear()
        main()

if tc == 1:
    dury = 0.5
else:
    dury = 1.5

def input_with_timeout(timeout=dury):
    def timeout_function():
        time.sleep(timeout)
        if not input_ready.is_set():
            input_ready.set()
    
    input_ready = threading.Event()
    timer_thread = threading.Thread(target=timeout_function)
    timer_thread.start()

    user_input = ""
    try:
        user_input = input(f"\nEnter your choice (timeout in {timeout} seconds): ")
        input_ready.set()
    except KeyboardInterrupt:
        pass  # Allow user to interrupt input with Ctrl+C
    
    input_ready.set()
    timer_thread.join()

    return user_input

def main():
    clear()
    current_theme = get_current_theme()
    icon = f"""
{current_theme["primary"]}                            ████████████           ████              
{current_theme["primary"]}                     █████▒░░░░░░░░░░░░▒██        ██▓▓██             
{current_theme["primary"]}                  █▓▒▒░░░░░░░░░░░░░░░░░░▓██     ███▓▒▒▒▓██           
{current_theme["primary"]}               ███░░░░░░░░░░░░░░░░░░░▒███    ████▓▓▒▒▒▒▒▒███         
{current_theme["primary"]}             ██▓░░░▓█████▒░░░░░░░░▒███      ██▓▓▓▓▒▒▒▒▒▒▒▒███        
{current_theme["primary"]}           ███░░░▓█▒░░░░░▓█▒░░░░░▓██       ██▓▓▓▓▓▒▒▒▒▒▒▒▒▓██        
{current_theme["primary"]}          ██▓░░░░██░░░░░░▒█▓░░░░▒██        ██▓▓▓▓▓▒▒▒▒▒▒▒▒▓██        
{current_theme["primary"]}         ██▒░░░░░░▓█▓▒▒▒▓█▓░░░░░░▓██        ███▓▓▓▒▒▒▒▒▒▒▓██         
{current_theme["primary"]}         █▓░░░░░░░░░░░░░░░░░░░░░░░▒▓██████  ███████████████          
{current_theme["primary"]}        ██▒░░░░▒█████▓░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒░████▓▓▓▓██▓██         
{current_theme["primary"]}        ██▒░░▒█▓▒▒▒▒▒▒█▓░░░░░░░░░░░░░░░░░░░░░░░▓███▓▓▓▓██▒▒██        
{current_theme["primary"]}        ██▒░░▒█▓▒▒▒▒▒▒██░░░░░░░░░░░░░░░░░░░░░░▒████▓▓▓▓██░▒██        
{current_theme["primary"]}         █▓░░░▒██▓▓▓██▓░░░░░░░░░░░░░░░░░░░░░▓████▓▓▒▒▒▒██░▓█         
{current_theme["primary"]}         ██▒░░░░░░░░░░░▒▓▓█▓▒░░░░░░░░░░░░░░░▓████▓▒░░░▒█▓▓██         
{current_theme["primary"]}          ██▒░░░░░░░░▓█▓▒▒▒▒▓█▓░░░░░░▒▒▒░░░░░▒▓██▓▒░░░▒████          
{current_theme["primary"]}           ██▓░░░░░░▒█▓▒▒▒▒▒▒▓█▒░░▓█▓▒▒▒▓██░░░░░▓█▒░░░▓███           
{current_theme["primary"]}             ██▓░░░░░▒██▓▒▒▒▓█▓░░▓█▒▒▒▒▒▒▒█▓░░░░▓█▒▒░░▓█             
{current_theme["primary"]}               ███░░░░░░▒▒▒▒░░░░░▒█▓▒▒▒▒▒▒▒░░░░░▒█▒▒░▒██             
{current_theme["primary"]}                 ████▒░░░░░░░░░░░░░░▓███▓░░░░░░▒██▓▒░▒██             
{current_theme["primary"]}                     ████▓▒░░░░░░░░░░░░░░░▒▓██████▓▒░▒██             
{current_theme["primary"]}                           ███████████████       ███████ 
{current_theme["reset"]}"""
    themes_text = f"\nAvailable themes:" + "\n" * 2
    for i, theme_name in enumerate(themes.keys(), 1):
        if themes[theme_name]['primary'] == current_theme['primary']:
            theme_name_display = f"{theme_name.upper()} (Current)"
        else:
            theme_name_display = theme_name.upper()
        themes_text += f"{themes[theme_name]['primary']}{i}. {theme_name_display}{themes[theme_name]['reset']}\n"
    if tc == 1:
        info = "(Press ENTER to exit)"
        timeout_duration = 0.5
    else:
        info = "(PRESS ENTER to finish)"
        timeout_duration = 1.5
    themes_text += "\n" * 2 + f"Choose a theme by number {current_theme['secondary']}{info}{current_theme['reset']}".strip()
    combined_message = Add.Add(icon, themes_text, 2)
    
    centered_message = Center.Center(combined_message)
    print(centered_message, end='')

    # Capture input with timeout
    user_input = input_with_timeout(timeout=timeout_duration)

    if user_input:
        execute_choice(user_input)
    else:
        print("\nNo input received in the given time. Exiting...")
        clear()

if __name__ == "__main__":
    main()
    clear()
