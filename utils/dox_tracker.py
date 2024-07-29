import webbrowser
from pystyle import Colors

def handle_error(error_message):
    print(f"{Colors.red}Error: {error_message}{Colors.reset}")

def display_search_options():
    options = f"""
{Colors.red}1 - Username
2 - Last Name, First Name
3 - General Search{Colors.reset}
    """
    print(options)

def get_search_input(search_type):
    if search_type in ['1', '01']:
        return input(f"{Colors.red}Enter Username: {Colors.reset}")
    elif search_type in ['2', '02']:
        last_name = input(f"{Colors.red}Enter Last Name: {Colors.reset}")
        first_name = input(f"{Colors.red}Enter First Name: {Colors.reset}")
        return last_name, first_name
    elif search_type in ['3', '03']:
        return input(f"{Colors.red}Enter Search Query: {Colors.reset}")
    else:
        raise ValueError(f"{Colors.red}Invalid search type{Colors.reset}")

def display_site_options():
    options = f"""
{Colors.red}1 - Facebook.com
2 - Youtube.com
3 - Twitter.com
4 - Tiktok.com
5 - Peekyou.com
6 - Tumblr.com
7 - PagesJaunes.fr{Colors.reset}
    """
    print(options)

def generate_search_url(site, search_type, search_terms):
    base_urls = {
        '1': "https://www.facebook.com/search/top/?init=quick&q=",
        '2': "https://www.youtube.com/results?search_query=",
        '3': "https://twitter.com/search?f=users&vertical=default&q=",
        '4': "https://www.tiktok.com/search?q=",
        '5': "https://www.peekyou.com/",
        '6': "https://www.tumblr.com/search/",
        '7': "https://www.pagesjaunes.fr/pagesblanches/recherche?quoiqui="
    }
    
    if search_type == '2':
        last_name, first_name = search_terms
        query = f"{last_name} {first_name}"
    else:
        query = search_terms
    
    url = base_urls.get(site, '') + query
    if site == '5':
        url = f"{url}{query.replace(' ', '_')}"
    
    webbrowser.open(url)

def main():
    try:
        display_search_options()
        search_type = input(f"{Colors.red}Select Search Type: {Colors.reset}")
        
        search_terms = get_search_input(search_type)
        
        while True:
            display_site_options()
            site_choice = input(f"{Colors.red}Select Site: {Colors.reset}")
            
            if site_choice in ['1', '2', '3', '4', '5', '6', '7']:
                generate_search_url(site_choice, search_type, search_terms)
            else:
                print(f"{Colors.red}Invalid site choice. Please select a valid option.{Colors.reset}")
    
    except Exception as e:
        handle_error(e)

if __name__ == "__main__":
    main()
