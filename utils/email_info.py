import subprocess
from emailrep import EmailRep
import re


def main():
    pass

def check_email_with_holehe(email):
    try:
        result = subprocess.run(['holehe', email, '--only-used'], capture_output=True, text=True)
        if result.returncode != 0:
            print("An error occurred while running holehe")
            return

        output_lines = result.stdout.split('\n')

        print(f"\nResults from Holehe for email: {email}\n")
        for line in output_lines:

            match = re.match(r"\[\+\] Email used: .* on (.*)", line)
            if match:
                print(match.group(1))

    except Exception as e:
        print(f"Error executing holehe: {str(e)}")

def get_email_information_with_emailrep(email):
    api = EmailRep()
    try:
        response = api.query(email)
        if response:
            print("\nResults from EmailRep.io:")
            print(f"Email: {email}")
            if 'reputation' in response:
                print(f"Reputation: {response['reputation']}")
            else:
                print("Reputation: N/A")
                
            if 'details' in response:
                print(f"Details: {response['details']}")
                if 'sources' in response['details']:
                    print(f"Sources: {response['details']['sources']}")
                else:
                    print("Sources: N/A")
                print(f"Account creation date: {response['details'].get('date_creation', 'N/A')}")
                print(f"Last seen: {response['details'].get('last_seen', 'N/A')}")
                print(f"Days since last seen: {response['details'].get('days_since_last_seen', 'N/A')}")
                print(f"Blacklist status: {response['details'].get('blacklisted', 'N/A')}")
                print(f"Malicious status: {response['details'].get('malicious_activity', 'N/A')}")
            else:
                print("Details: N/A")
        else:
            print(f"No information found for {email}")
    except Exception as e:
        print(f"Error querying EmailRep.io: {str(e)}")

if __name__ == "__main__":
    email = input("Enter the email address: ")
    check_email_with_holehe(email)
    get_email_information_with_emailrep(email)

if __name__ == "__main__":
    main()