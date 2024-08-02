import os
import base64
from pystyle import Colors

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    pass

clear()
userid = input(f"{Colors.red}Discord ID : ")
encodedBytes = base64.b64encode(userid.encode("utf-8"))
encodedStr = str(encodedBytes, "utf-8")
print(f'\n{Colors.red}FIRST PART : {encodedStr}')

if __name__ == "__main__":
    main()