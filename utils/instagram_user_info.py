import instaloader
import os
from pystyle import Colors

loader = instaloader.Instaloader()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def handle_error(message):
    print(f"{Colors.red}Error: {message}{Colors.reset}")

def get_profile_info(username):
    try:
        profile = instaloader.Profile.from_username(loader.context, username)

        print(f"{Colors.red}Username: {profile.username}{Colors.reset}")
        print(f"{Colors.red}Name: {profile.full_name}{Colors.reset}")
        print(f"{Colors.red}Bio: {profile.biography}{Colors.reset}")
        print(f"{Colors.red}Followers: {profile.followers}{Colors.reset}")
        print(f"{Colors.red}Following: {profile.followees}{Colors.reset}")
        print(f"{Colors.red}Posts: {profile.mediacount}{Colors.reset}")
        print(f"{Colors.red}Profile Picture URL: {profile.profile_pic_url}{Colors.reset}")

        for post in profile.get_posts():
            print(f"{Colors.red}Post URL:{Colors.reset} {post.url}")
            print(f"{Colors.red}Caption:{Colors.reset} {post.caption[:100]}")  
            print(f"{Colors.red}Likes:{Colors.reset} {post.likes}")
            print(f"{Colors.red}Comments:{Colors.reset} {post.comments}")
            print()

    except instaloader.exceptions.InstaloaderException as e:
        handle_error(str(e))

if __name__ == "__main__":
    clear()
    username = input(f"{Colors.red}Enter Instagram username: {Colors.reset}")
    get_profile_info(username)
