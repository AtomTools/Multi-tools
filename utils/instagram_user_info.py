import instaloader
import os

loader = instaloader.Instaloader()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_profile_info(username):
    try:
        profile = instaloader.Profile.from_username(loader.context, username)
        
        print(f"Username: {profile.username}")
        print(f"Name: {profile.full_name}")
        print(f"Bio: {profile.biography}")
        print(f"Followers: {profile.followers}")
        print(f"Following: {profile.followees}")
        print(f"Posts: {profile.mediacount}")
        print(f"Profile Picture URL: {profile.profile_pic_url}")

        print("\nPosts:")
        for post in profile.get_posts():
            print(f"Post URL: {post.url}")
            print(f"Caption: {post.caption[:100]}")  
            print(f"Likes: {post.likes}")
            print(f"Comments: {post.comments}")
            print()

    except instaloader.exceptions.InstaloaderException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    clear()
    username = input("Enter Instagram username: ")
    get_profile_info(username)
