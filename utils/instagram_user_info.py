import instaloader
import os
from pystyle import Colors, Colorate

loader = instaloader.Instaloader()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def handle_error(message):
    print(f"{Colors.red}Error: {message}{Colors.reset}")

def get_profile_info(username):
    try:
        profile = instaloader.Profile.from_username(loader.context, username)

        print(f"{Colors.green}Username: {profile.username}{Colors.reset}")
        print(f"{Colors.green}Name: {profile.full_name}{Colors.reset}")
        print(f"{Colors.green}Bio: {profile.biography}{Colors.reset}")
        print(f"{Colors.green}Followers: {profile.followers}{Colors.reset}")
        print(f"{Colors.green}Following: {profile.followees}{Colors.reset}")
        print(f"{Colors.green}Posts: {profile.mediacount}{Colors.reset}")
        print(f"{Colors.green}Profile Picture URL: {profile.profile_pic_url}{Colors.reset}")

        print("\n{Colors.blue}Posts:{Colors.reset}")
        for post in profile.get_posts():
            print(f"{Colors.blue}Post URL:{Colors.reset} {post.url}")
            print(f"{Colors.blue}Caption:{Colors.reset} {post.caption[:100]}")  
            print(f"{Colors.blue}Likes:{Colors.reset} {post.likes}")
            print(f"{Colors.blue}Comments:{Colors.reset} {post.comments}")
            print()

    except instaloader.exceptions.InstaloaderException as e:
        handle_error(str(e))

if __name__ == "__main__":
    clear()
    username = input(f"{Colors.red}Enter Instagram username: {Colors.reset}")
    get_profile_info(username)
