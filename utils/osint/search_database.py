import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def search_in_file(file_path, search_term):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, start=1):
                if search_term in line:
                    return line_number, line.strip().replace(search_term, f"\033[93m{search_term}\033[0m")
    except UnicodeDecodeError:
        try:
            with open(file_path, 'r', encoding='latin-1') as file:
                for line_number, line in enumerate(file, start=1):
                    if search_term in line:
                        return line_number, line.strip().replace(search_term, f"\033[93m{search_term}\033[0m")
        except Exception as e:
            print(f"Error reading file '{file_path}': {e}")
    except Exception as e:
        print(f"Error reading file '{file_path}': {e}")
    return None, None

def search_directory(directory, search_term):
    total_files = 0
    found_results = False

    for root, dirs, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            result_line_number, result_line = search_in_file(file_path, search_term)
            total_files += 1
            
            if result_line_number:
                found_results = True
                print(f"File: {file_name}")
                print(f"Result: {result_line}")
                print()

    return total_files, found_results

def main():
    clear()
    folder_path = "Database"
    absolute_path = os.path.abspath(folder_path)
    
    search_term = input("Enter search term: ").strip()

    if not search_term:
        print("Search term cannot be empty.")
        return

    try:
        total_files, found_results = search_directory(absolute_path, search_term)
        if not found_results:
            print(f"No matches found for '{search_term}'.")
        print(f"Total files checked: {total_files}")
    except Exception as e:
        print(f"An error occurred during the search: {e}")

if __name__ == "__main__":
    main()
