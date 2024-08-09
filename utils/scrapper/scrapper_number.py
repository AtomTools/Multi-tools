import random
import string
import phonenumbers
from phonenumbers import NumberParseException
from pystyle import Colors
import os

operators = {
    "France": [("06", "Orange"), ("07", "SFR"), ("07", "Bouygues"), ("07", "Free")],
}

def generate_phone_number(prefix, length=8):
    number = ''.join(random.choice(string.digits) for _ in range(length))
    return f"{prefix}{number}"

def generate_phone_numbers_with_operators(country):
    prefix, operator = random.choice(operators[country])
    phone_number = generate_phone_number(prefix)
    return {
        "country": country,
        "phone_number": phone_number,
        "operator": operator
    }

def is_valid_phone_number(phone_number, country):
    try:
        parsed_number = phonenumbers.parse(phone_number, country)
        return phonenumbers.is_valid_number(parsed_number)
    except NumberParseException:
        return False

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear()
    
    folder_name = "phone_number_data"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    country = "France"  
    
    valid_file_path = os.path.join(folder_name, "valid_phone_numbers.txt")
    invalid_file_path = os.path.join(folder_name, "invalid_phone_numbers.txt")

    with open(valid_file_path, "a") as valid_file, open(invalid_file_path, "a") as invalid_file:
        try:
            while True:
                entry = generate_phone_numbers_with_operators(country)
                phone_number = entry['phone_number']
                is_valid = is_valid_phone_number(phone_number, "FR")
                 # For terminal output with color
                status_color = f"{Colors.green}Valid" if is_valid else f"{Colors.red}Invalid"
                result_color = f"{status_color}{Colors.reset} | {phone_number} ({entry['operator']})"

                # For file output without color
                status_text = "Valid" if is_valid else "Invalid"
                result_text = f"{status_text} | {phone_number} ({entry['operator']})\n"

                if is_valid:
                    valid_file.write(result_text)
                else:
                    invalid_file.write(result_text)

                print(result_color.strip()) 

        except KeyboardInterrupt:
            print("\nExiting...")

if __name__ == "__main__":
    main()
