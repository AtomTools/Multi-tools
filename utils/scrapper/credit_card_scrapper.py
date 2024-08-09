import random
import string
import os

def generate_random_credit_card(brand):
    if brand == "Visa":
        card_number = '4' + ''.join(random.choice(string.digits) for _ in range(15))
    elif brand == "MasterCard":
        card_number = '5' + ''.join(random.choice(string.digits) for _ in range(15)) 
    return card_number

def generate_random_expiry_date():
    month = random.randint(1, 12)
    year = random.randint(2025, 2030)
    return f"{month:02}/{year}"

def generate_random_cvv():
    return ''.join(random.choice(string.digits) for _ in range(3))

def luhn(n):
    r = [int(ch) for ch in str(n)][::-1]
    return (sum(r[0::2]) + sum(sum(divmod(d*2, 10)) for d in r[1::2])) % 10 == 0

def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    folder_name = "credit_card_data"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    brands = ["Visa", "MasterCard"]

    valid_file_path = os.path.join(folder_name, "valid_credit_cards.txt")
    invalid_file_path = os.path.join(folder_name, "invalid_credit_cards.txt")

    with open(valid_file_path, "a") as valid_file, open(invalid_file_path, "a") as invalid_file:
        try:
            while True:
                brand = random.choice(brands)
                card_number = generate_random_credit_card(brand)
                expiry_date = generate_random_expiry_date()
                cvv = generate_random_cvv()
                is_valid = luhn(card_number)  
                status = "Valid" if is_valid else "Invalid"
                result = f"{status} - {card_number} ({brand}) - Exp: {expiry_date} - CVV: {cvv}\n"

                if is_valid:
                    valid_file.write(result)
                else:
                    invalid_file.write(result)

                print(result.strip())

        except KeyboardInterrupt:
            print("\nExiting...")

if __name__ == "__main__":
    main()
