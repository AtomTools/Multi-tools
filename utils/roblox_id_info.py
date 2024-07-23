import requests
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        clear()
        print("Atom Tools - Roblox User Lookup by ID")
        try:
            user_id = input("\nEnter the user ID (or 'exit' to quit): ")

            if user_id.lower() == 'exit':
                break

            try:
                user_info_response = requests.get(f"https://users.roblox.com/v1/users/{user_id}")
                user_info = user_info_response.json()

                if user_info_response.status_code != 200:
                    ErrorId()
                else:
                    userid = format_value(user_info.get('id'))
                    display_name = format_value(user_info.get('displayName'))
                    username = format_value(user_info.get('name'))
                    description = format_value(user_info.get('description'), "Not available")
                    created_at = format_value(user_info.get('created'))
                    is_banned = format_value(user_info.get('isBanned'))
                    external_app_display_name = format_value(user_info.get('externalAppDisplayName'), "Not available")
                    has_verified_badge = format_value(user_info.get('hasVerifiedBadge'))
                    join_date = format_value(user_info.get('created'))

                    groups_response = requests.get(f"https://groups.roblox.com/v2/users/{user_id}/groups/roles")
                    groups_info = groups_response.json().get('data', [])
                    groups = ", ".join([group['group']['name'] for group in groups_info]) or "No groups"

                    favorites_response = requests.get(f"https://games.roblox.com/v2/users/{user_id}/favorite/games")
                    favorites_info = favorites_response.json().get('data', [])
                    favorite_games = ", ".join([game['name'] for game in favorites_info]) or "No favorite games"

                    info_text = f"""
Username: {username}
Id: {userid}
Display Name: {display_name}
Description: {description}
Created: {created_at}
Banned: {is_banned}
External Name: {external_app_display_name}
Verified Badge: {has_verified_badge}
Join Date: {join_date}
Groups: {groups}
Favorite Games: {favorite_games}
"""

                    print(info_text)
                    input("Press Enter to continue...")
            
            except Exception as e:
                Error(e)
        
        except Exception as e:
            Error(e)

def Reset():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def Error(e):
    print(f"An error occurred: {e}\n")

def ErrorId():
    print("Invalid user ID or unable to retrieve information.\n")

def format_value(value, default="Unknown"):
    if value is None:
        return default
    elif isinstance(value, bool):
        return "Yes" if value else "No"
    return value

if __name__ == "__main__":
    main()
