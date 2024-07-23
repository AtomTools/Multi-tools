import requests
import time
import threading


def get_headers(token):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
    }
    return headers


def main():
    print("Atom Tools")

def clear():
    print("\033c", end="")


def read_status_texts():
    print(f"\n 'Entrer le statut que vous voulez mettre et entrer FIN quand vous avez fini :")
    status_texts = []
    index = 1
    
    while True:
        line = input('Status {index} : ')
        
        if line.upper() == "FIN":
            break
        
        status_texts.append(line)
        index += 1
    
    return status_texts

def get_user_id(token):
    headers = get_headers(token)
    try:
        r = requests.get("https://discord.com/api/v6/users/@me", headers=headers)
        if r.status_code == 200:
            return r.json()['id']
        else:
            return None
    except Exception as e:
        return None



def change_status(token, text):
    headers = get_headers(token)
    setting = {
        'custom_status': {
            'text': text,
        },
    }
    try:
        r = requests.patch("https://discord.com/api/v6/users/@me/settings", headers=headers, json=setting)
        if r.status_code == 200:
            print(f'token={token[:20]}... [SUCCESS]')
        else:
            print(f"token={token[:20]}...') [ERROR] ({r.status_code})')")
    except Exception as e:
        pass

def status_changer():
    clear()
    
    token = input('Entrez le token: ')
    
    status_texts = read_status_texts()
    
    while True:
        try:
            time_frequency = int(input('Temps entre chaque changement de statut (en secondes) : '))
            break
        except ValueError:
            print('Veuillez entrer un nombre entier pour le temps.')
    
    user_id = get_user_id(token)
    if not user_id:
        print("Impossible de récupérer l'ID de l'utilisateur. Arrêt du programme.")
        return
        
    try:
        while True:
            for text in status_texts:
                thread = threading.Thread(target=change_status, args=(token, text))
                thread.start()
                thread.join()
                time.sleep(time_frequency)
    except KeyboardInterrupt:
        print(f"\nInterruption du changement de statut.")

if __name__ == "__main__":
    status_changer()