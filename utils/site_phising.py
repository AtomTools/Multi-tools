import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re
from pystyle import Colors

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def css_and_js(html_content, base_url):
    soup = BeautifulSoup(html_content, 'html.parser')

    print("Recovering CSS...")
    css_links = soup.find_all('link', rel='stylesheet')
    if css_links:
        all_css = ""
        for link in css_links:
            css_url = urljoin(base_url, link['href'])
            try:
                css_response = requests.get(css_url)
                if css_response.status_code == 200:
                    all_css += css_response.text + "\n"
                else:
                    print(f"Error retrieving CSS from {css_url}.")
            except Exception as e:
                print(f"Error retrieving CSS from {css_url}. Exception: {e}")
        
        if all_css:
            style_tag = soup.new_tag('style')
            style_tag.string = all_css
            soup.head.append(style_tag)
            for link in css_links:
                link.decompose()
    else:
        print("No CSS links found.")

    print("Recovering JavaScript...")
    script_links = soup.find_all('script', src=True)
    if script_links:
        all_js = ""
        for script in script_links:
            js_url = urljoin(base_url, script['src'])
            try:
                js_response = requests.get(js_url)
                if js_response.status_code == 200:
                    all_js += js_response.text + "\n"
                else:
                    print(f"Error retrieving JavaScript from {js_url}.")
            except Exception as e:
                print(f"Error retrieving JavaScript from {js_url}. Exception: {e}")
        
        if all_js:
            script_tag = soup.new_tag('script')
            script_tag.string = all_js
            soup.body.append(script_tag)
            for script in script_links:
                script.decompose()
    else:
        print("No JavaScript links found.")

    return soup.prettify()

def main():
    pass

    clear()
    website_url = input(f"{Colors.red}Website URL : ")
    if "https://" not in website_url and "http://" not in website_url:
        website_url = "https://" + website_url

    try:
        print("Recovering HTML...")
        response = requests.get(website_url, timeout=5)
        if response.status_code == 200:
            html_content = response.text
            soup = BeautifulSoup(html_content, 'html.parser')
            file_name = re.sub(r'[\\/:*?"<>|]', '-', soup.title.string if soup.title else 'page_sans_titre')

            output_folder = 'PhishingAttack'
            os.makedirs(output_folder, exist_ok=True)  

            file_html_relative = os.path.join(output_folder, f'{file_name}.html')
            file_html = os.path.abspath(file_html_relative)

            final_html = css_and_js(html_content, website_url)

            with open(file_html, 'w', encoding='utf-8') as file:
                file.write(final_html)
            print(f"{Colors.red}Phishing attack successful. The file is located in the folder \"{file_html_relative}\"")
        else:
            print(f"Error with URL. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
