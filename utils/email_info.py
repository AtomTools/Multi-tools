import subprocess
from emailrep import EmailRep
import re
from pystyle import Colors

def handle_error(error_message):
    print(f"{Colors.red}Error: {error_message}{Colors.reset}")

def check_email_with_holehe(email):
    try:
        result = subprocess.run(['holehe', email, '--only-used'], capture_output=True, text=True)
        if result.returncode != 0:
            handle_error("An error occurred while running holehe")
            return

        output_lines = result.stdout.split('\n')

        print(f"\n{Colors.red}Results from Holehe for email: {email}{Colors.reset}\n")
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
            print(f"\n{Colors.red}Results from EmailRep.io:{Colors.reset}")
            print(f"{Colors.red}Email:{Colors.reset} {email}")
            if 'reputation' in response:
                print(f"{Colors.red}Reputation:{Colors.reset} {response['reputation']}")
            else:
                print(f"{Colors.red}Reputation:{Colors.reset} N/A")
                
            if 'details' in response:
                print(f"{Colors.red}Details:{Colors.reset} {response['details']}")
                if 'sources' in response['details']:
                    print(f"{Colors.red}Sources:{Colors.reset} {response['details']['sources']}")
                else:
                    print(f"{Colors.red}Sources:{Colors.reset} N/A")
                print(f"{Colors.red}Account creation date:{Colors.reset} {response['details'].get('date_creation', 'N/A')}")
                print(f"{Colors.red}Last seen:{Colors.reset} {response['details'].get('last_seen', 'N/A')}")
                print(f"{Colors.red}Days since last seen:{Colors.reset} {response['details'].get('days_since_last_seen', 'N/A')}")
                print(f"{Colors.red}Blacklist status:{Colors.reset} {response['details'].get('blacklisted', 'N/A')}")
                print(f"{Colors.red}Malicious status:{Colors.reset} {response['details'].get('malicious_activity', 'N/A')}")
            else:
                print(f"{Colors.red}Details:{Colors.reset} N/A")
        else:
            print(f"{Colors.red}No information found for {email}{Colors.reset}")
    except Exception as e:
        handle_error(f"Error querying EmailRep.io: {str(e)}")

def main():
    email = input(f"{Colors.red}Enter the email address: {Colors.reset}")
    check_email_with_holehe(email)
    get_email_information_with_emailrep(email)

if __name__ == "__main__":
    main()
