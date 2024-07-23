import random
import string
import os

def luhn(n):
    r = [int(ch) for ch in str(n)][::-1]
    return (sum(r[0::2]) + sum(sum(divmod(d*2, 10)) for d in r[1::2])) % 10 == 0

def generate_random_iban():
    country_code = "FR"
    check_digits = ''.join(random.choice(string.digits) for _ in range(2))
    bank_code = ''.join(random.choice(string.digits) for _ in range(5))
    branch_code = ''.join(random.choice(string.digits) for _ in range(5))
    account_number = ''.join(random.choice(string.digits) for _ in range(11))
    iban = f"{country_code}{check_digits}{bank_code}{branch_code}{account_number}"
    return iban

def is_valid_iban(iban):
    return iban.startswith("FR") and len(iban) == 27 and luhn(iban[4:])

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear()

    folder_name = "iban_data"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    valid_file_path = os.path.join(folder_name, "valid_ibans.txt")
    invalid_file_path = os.path.join(folder_name, "invalid_ibans.txt")

    with open(valid_file_path, "a") as valid_file, open(invalid_file_path, "a") as invalid_file:
        try:
            while True:
                iban = generate_random_iban()
                is_valid = is_valid_iban(iban)
                status = "Valid" if is_valid else "Invalid"
                result = f"{status} - {iban}\n"

                if is_valid:
                    valid_file.write(result)
                else:
                    invalid_file.write(result)

                print(result.strip())

        except KeyboardInterrupt:
            print("\nExiting...")

if __name__ == "__main__":
    main()
