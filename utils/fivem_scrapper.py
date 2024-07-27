import os
import requests
import json
import time
import re
import uuid
import csv
import asyncio
from fake_useragent import UserAgent
import aiohttp


cfx_code_pattern = re.compile(r'\u0006([a-z0-9]{6})')

def extract_cfx_codes(data):
    matches = cfx_code_pattern.findall(data)
    cfx_codes = [code for code in matches if code != 'locale']
    return cfx_codes

async def scrape_cfx_ids():
    print("Scraping des IDs des serveurs FiveM...")
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get('https://servers-frontend.fivem.net/api/servers/streamRedir/') as response:
                response.raise_for_status()
                data = await response.read()
                cfx_codes = extract_cfx_codes(data.decode('latin-1'))
                os.makedirs('fivem_scrapper', exist_ok=True)
                with open('fivem_scrapper/cfxid.sql', 'w', encoding='utf-8') as file:
                    for code in cfx_codes:
                        file.write(f"{code}\n")
                    print("Toutes les ID des serveurs FiveM (CFXID) ont été mises dans fivem_scrapper/cfxid.sql !")
        except aiohttp.ClientError as err:
            print(f"Erreur lors de la récupération des données: {err}")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def clean_filename(hostname):
    return re.sub(r'^([0-9])', '', re.sub(r'[/:"*?<>|]', '', hostname)).replace('^0', '').replace('^1', '').replace('^2', '').replace('^3', '').replace('^4', '').replace('^5', '').replace('^6', '').replace('^7', '').replace('^8', '').replace('^9', '')

def check_if_player_exists(filename, player_data, added_players):
    if not os.path.exists(filename):
        return False

    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        try:
            existing_player = json.loads(line)
        except json.JSONDecodeError:
            continue

        if existing_player.get('fivem') == player_data.get('fivem'):
            fields_to_check = ['ip', 'steam', 'name', 'live', 'xbl', 'license', 'license2', 'name']
            fields_match = True

            for field in fields_to_check:
                existing_field_value = existing_player.get(field)
                new_field_value = player_data.get(field)

                if (existing_field_value is not None or new_field_value is not None) and existing_field_value != new_field_value:
                    fields_match = False
                    break

            if fields_match:
                return True

    if player_data['identifiers'] in added_players:
        return True

    return False

def check_if_server_id_exists(server_id, filename):
    if not os.path.exists(filename):
        return False

    with open(filename, 'r') as f:
        lines = f.readlines()

    server_id = str(server_id)
    for line in lines:
        if line.strip() == server_id:
            return True

    return False

def remove_server_id_from_proxy(server_id, proxy_file):
    with open(proxy_file, 'r') as f:
        lines = f.readlines()

    with open(proxy_file, 'w') as f:
        for line in lines:
            if line.strip() != server_id:
                f.write(line)

def get_server_info(server_id, proxy, added_players):
    url = f'https://servers-frontend.fivem.net/api/servers/single/{server_id}'
    user_agent = UserAgent()
    headers = {
        'User-Agent': user_agent.random,
        'method': 'GET'
    }

    try:
        response = requests.get(url, headers=headers, proxies=proxy)

        if response.status_code == 200:
            server_data = response.json()
            hostname = clean_filename(str(uuid.uuid4()))

            try:
                hostname = clean_filename(server_data['Data']['hostname'])[:100]
            except Exception as err:
                print(err)

            try:
                if len(server_data['Data']['vars']['sv_projectName']) >= 10:
                    hostname = clean_filename(server_data['Data']['vars']['sv_projectName'])[:100]
            except:
                pass

            directories = ['fivem_scrapper/txt', 'fivem_scrapper/csv', 'fivem_scrapper/sql']
            for directory in directories:
                if not os.path.exists(directory):
                    os.makedirs(directory)

            filename_sql = f'fivem_scrapper/sql/{hostname}.sql'
            filename_txt = f'fivem_scrapper/txt/{hostname}.txt'
            filename_csv = f'fivem_scrapper/csv/{hostname}.csv'

            for player in server_data['Data']['players']:
                player_data = json.dumps(player, ensure_ascii=False)
                player_identifiers = player['identifiers']

                if not check_if_player_exists(filename_sql, player, added_players):
                    with open(filename_sql, 'a', encoding='utf-8') as file_sql:
                        file_sql.write(player_data)
                        file_sql.write('\n')

                    with open(filename_txt, 'a', encoding='utf-8') as file_txt:
                        file_txt.write(player_data)
                        file_txt.write('\n')

                    with open(filename_csv, 'a', newline='', encoding='utf-8') as file_csv:
                        writer = csv.writer(file_csv)
                        writer.writerow(player.values())

                    print(f'Scrapped - {player["name"]} a été ajouté !')
                    added_players.append(player_identifiers)

            print(f'\nAuthor - discord.gg/toolsfr\nInfo - CFX ID : {server_id}\nInfo - Scrap Effectue : {filename_sql}\n')

        else:
            print(f'\nError - Message d\'erreur ({server_id}: {response.status_code})\n')

    except Exception as e:
        print(f'Erreur: {str(e)}')

def process_servers(server_ids, proxies, added_players):
    for server_id, proxy in zip(server_ids, proxies):
        if not check_if_server_id_exists(server_id, 'fivem_scrapper/proxy.sql'):
            get_server_info(server_id, proxy, added_players)
            remove_server_id_from_proxy(server_id, 'fivem_scrapper/proxy.sql')
            time.sleep(0.5)
        else:
            print(f'Server ID {server_id} already scrapped, skipping.')

def option_1():
    with open('fivem_scrapper/cfxid.sql', 'r') as server_file:
        french_server_ids = [line.strip() for line in server_file.readlines()]

    with open('fivem_scrapper/proxy.sql', 'r') as proxy_file:
        proxy_list = [{'http': f'socks5://{proxy.strip()}'} for proxy in proxy_file]

    added_players = []

    half_length = len(french_server_ids) // 2
    first_half = french_server_ids[:half_length]
    second_half = french_server_ids[half_length:]

    process_servers(first_half, proxy_list, added_players)
    process_servers(second_half, proxy_list, added_players)

def option_2():
    asyncio.run(scrape_cfx_ids())

def main_menu():
    clear()
    while True:
        print("\n1 - Capturer des IDs\n2 - Scrapper des serveurs\n3 - Quitter\n")
        
        choice = input("Choisissez une option : ")

        if choice == '1':
            option_2()
        elif choice == '2':
            option_1()
        elif choice == '3':
            break
        else:
            print("Option invalide. Réessayez.")
            time.sleep(2)


if __name__ == '__main__':
    main_menu()
