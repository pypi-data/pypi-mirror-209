# By MrHacker-X
# https://github.com/MrHacker-X/

import argparse
import requests

def get_github_user_profile(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    
    if response.status_code == 200:
        profile_data = response.json()
        return profile_data
    else:
        return None

def get_repository_names(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    
    if response.status_code == 200:
        repositories = response.json()
        repository_names = []
        
        for repo in repositories:
            repository_names.append((repo['name'], repo['html_url']))
            
        return repository_names
    else:
        return None
    
def main():
    print()

print('\033[1;32m')

bnr = """\033[1;32m╭━━━╮╭╮╭━━━╮╱╱╱╱╱╱╭━╮╭━╮
┃╭━╮┣╯╰┫╭━╮┃╱╱╱╱╱╱╰╮╰╯╭╯
┃┃╱╰╋╮╭┫╰━━┳━━┳╮╱╭╮╰╮╭╯
┃┃╭━╋┫┃╰━━╮┃╭╮┃┃╱┃┃╭╯╰╮
┃╰┻━┃┃╰┫╰━╯┃╰╯┃╰━╯┣╯╭╮╰╮
╰━━━┻┻━┻━━━┫╭━┻━╮╭┻━╯╰━╯
╱╱╱╱╱╱╱╱╱╱╱┃┃╱╭━╯┃╱╱╱╱╱
╱╱╱╱╱╱╱╱╱╱╱╰╯╱╰━━╯╱╱╱ \033[1;33mV:0.1.3
\033[1;32m╱╱╱╱╱╱╱\033[1;33mMrHacker X\033[1;32m╱╱╱╱╱╱"""


# Set up command-line argument parser
parser = argparse.ArgumentParser(description="GitHub User Profile Details")
parser.add_argument('-u', '--username', help='GitHub username')
parser.add_argument('-v', '--version', action='store_true', help='Show script version')
parser.add_argument('-d', '--developer', action='store_true', help='Show developer name')
parser.add_argument('-o', '--output', help='Output file name')
args = parser.parse_args()

# Check if the user requested version or developer details
if args.version:
    print("\033[1;32m\nGitSpyX Version: 0.1.3\n")

elif args.developer:
    print("\033[1;32m\nTool By MrHacker X")
    print("\033[1;32mOwner name: Alex Butler\n")
    
else:
    if not args.username:
        parser.error('GitHub username is required.')

    # Get user profile
    profile = get_github_user_profile(args.username)

    if profile:
        print(f"{bnr}\n")
        print(f"\033[1;32m<>════[\033[1;33mProfile Details of {args.username}\033[1;32m]════<>\n")
        print(f"\033[1;32m[+]\033[1;33m Name:\033[1;32m {profile['name']}")
        print(f"\033[1;32m[+]\033[1;33m Username:\033[1;32m {args.username}")
        print(f"\033[1;32m[+]\033[1;33m Bio:\033[1;32m {profile['bio']}")
        print(f"\033[1;32m[+]\033[1;33m Location:\033[1;32m {profile['location']}")
        print(f"\033[1;32m[+]\033[1;33m Public Repositories:\033[1;32m {profile['public_repos']}")
        print(f"\033[1;32m[+]\033[1;33m Followers:\033[1;32m {profile['followers']}")
        print(f"\033[1;32m[+]\033[1;33m Followings:\033[1;32m {profile['following']}")
        print(f"\033[1;32m[+]\033[1;33m ID:\033[1;32m {profile['id']}")
        print(f"\033[1;32m[+]\033[1;33m Public Gist:\033[1;32m {profile['public_gists']}")
        print(f"\033[1;32m[+]\033[1;33m Site Admin:\033[1;32m {profile['site_admin']}")
        print(f"\033[1;32m[+]\033[1;33m Type:\033[1;32m {profile['type']}")
        print(f"\033[1;32m[+]\033[1;33m Twitter Username:\033[1;32m {profile['twitter_username']}")
        print(f"\033[1;32m[+]\033[1;33m Blog:\033[1;32m {profile['blog']}")
        print(f"\033[1;32m[+]\033[1;33m Email:\033[1;32m {profile['email']}")
        print(f"\033[1;32m[+]\033[1;33m Profile Logo:\033[1;32m {profile['avatar_url']}")
        print(f"\033[1;32m[+]\033[1;33m Hireable:\033[1;32m {profile['hireable']}")
        print(f"\033[1;32m[+]\033[1;33m Created At:\033[1;32m {profile['created_at']}")
        print(f"\033[1;32m[+]\033[1;33m Updated At:\033[1;32m {profile['updated_at']}")

        # Add any additional profile details you want to display
        if args.output:
            with open(args.output, 'w') as f:
                f.write(f"<>════[Profile Details of {args.username}]════<>\n\n")
                f.write(f"[+] Name: {profile['name']}\n")
                f.write(f"[+] Username: {args.username}\n")
                f.write(f"[+] Bio: {profile['bio']}\n")
                f.write(f"[+] Location: {profile['location']}\n")
                f.write(f"[+] Public Repositories: {profile['public_repos']}\n")
                f.write(f"[+] Followers: {profile['followers']}\n")
                f.write(f"[+] Followings: {profile['following']}\n")
                f.write(f"[+] ID: {profile['id']}\n")
                f.write(f"[+] Public Gist: {profile['public_gists']}\n")
                f.write(f"[+] Site Admin: {profile['site_admin']}\n")
                f.write(f"[+] Type: {profile['type']}\n")
                f.write(f"[+] Twitter Username: {profile['twitter_username']}\n")
                f.write(f"[+] Blog: {profile['blog']}\n")
                f.write(f"[+] Email: {profile['email']}\n")
                f.write(f"[+] Profile Logo: {profile['avatar_url']}\n")
                f.write(f"[+] Hireable: {profile['hireable']}\n")
                f.write(f"[+] Created At: {profile['created_at']}\n")
                f.write(f"[+] Updated At: {profile['updated_at']}\n")
    else:
        print("\n\033[1;31m[✗] User profile not found.\n")

    # Get repository names and links

    # Get repository names and links
    repositories = get_repository_names(args.username)

    if repositories:
        print("\n\033[1;32m<>════[\033[1;33mRepository Details]\033[1;32m════<>\n")
        if args.output:
            with open(args.output, 'a') as f:
                f.write("\n<>════[Repository Details]════<>\n\n")
                for repo_name, repo_link in repositories:
                    print(f"\033[1;32m[+]\033[1;33m Repository:\033[1;32m {repo_name}")
                    print(f"\033[1;32m[+]\033[1;33m Link:\033[1;32m {repo_link}")
                    print()
                    f.write(f"[+] Repository: {repo_name}\n")
                    f.write(f"[+] Link: {repo_link}\n")
                    f.write("\n")
            print(f'\033[1;32m[✔] \033[1;33mOutput saved in \033[1;32m{args.output}')
        else:
            for repo_name, repo_link in repositories:
                print(f"\033[1;32m[+]\033[1;33m Repository:\033[1;32m {repo_name}")
                print(f"\033[1;32m[+]\033[1;33m Link:\033[1;32m {repo_link}")
                print()
    else:
        print("\n\033[1;31m[✗] Repositories not found.\n")
