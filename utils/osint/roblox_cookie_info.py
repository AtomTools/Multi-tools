import requests
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_roblox_info(cookie):
    url = "https://www.roblox.com/mobileapi/userinfo"
    try:
        response = requests.get(url, cookies={".ROBLOSECURITY": cookie})
        response.raise_for_status()
        info = response.json()
        status = "Valid"
    except requests.RequestException as e:
        print(f"An error occurred while retrieving the information: {e}")
        return {
            "status": "Invalid",
            "username": "None",
            "user_id": "None",
            "robux": "None",
            "premium": "None",
            "avatar": "None",
            "builders_club": "None"
        }

    return {
        "status": status,
        "username": info.get('UserName', "None"),
        "user_id": info.get("UserID", "None"),
        "robux": info.get("RobuxBalance", "None"),
        "premium": info.get("IsPremium", "None"),
        "avatar": info.get("ThumbnailUrl", "None"),
        "builders_club": info.get("IsAnyBuildersClubMember", "None")
    }

def main():
    clear()
    cookie = input("Cookie: ")

    user_info = get_roblox_info(cookie)

    print(f"
Status: {user_info['status']}
Username: {user_info['username']}
Id: {user_info['user_id']}
Robux: {user_info['robux']}
Premium: {user_info['premium']}
Builders Club: {user_info['builders_club']}
Avatar: {user_info['avatar']}
")

if __name__ == "__main__":
    main()
