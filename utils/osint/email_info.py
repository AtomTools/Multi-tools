import subprocess
from emailrep import EmailRep
import re

def clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def handle_error(error_message):
    print(f"Error: {error_message}")

def check_email_with_holehe(email):
    try:
        result = subprocess.run(['holehe', email, '--only-used'], capture_output=True, text=True)
        if result.returncode != 0:
            handle_error("An error occurred while running holehe")
            return

        output_lines = result.stdout.split('\n')
        print(f"\nResults from Holehe for email: {email}\n")
        for line in output_lines:
            match = re.match(r"\[\+\] Email used: .* on (.*)", line)
            if match:
                print(match.group(1))

    except Exception as e:
        handle_error(f"Error executing holehe: {str(e)}")

def get_email_information_with_emailrep(email):
    api = EmailRep()
    try:
        response = api.query(email)
        if response:
            print(f"\nResults from EmailRep.io:")
            print(f"Email: {email}")

            reputation = response.get('reputation', 'N/A')
            details = response.get('details', {})

            print(f"> Reputation: {reputation}")

            if details:
                print(f"Sources: {details.get('sources', 'N/A')}")
                print(f"Account creation date: {details.get('date_creation', 'N/A')}")
                print(f"Last seen: {details.get('last_seen', 'N/A')}")
                print(f"Days since last seen: {details.get('days_since_last_seen', 'N/A')}")
                print(f"Blacklist status: {details.get('blacklisted', 'N/A')}")
                print(f"Malicious status: {details.get('malicious_activity', 'N/A')}")
            else:
                print("Details: N/A")

        else:
            print(f"No information found for {email}")

    except Exception as e:
        handle_error(f"Error querying EmailRep.io: {str(e)}")

def main():
    clear()
    email = input("Enter the email address: ").strip()
    check_email_with_holehe(email)
    get_email_information_with_emailrep(email)
    input("\nPress ENTER to exit...")

if __name__ == "__main__":
    main()
