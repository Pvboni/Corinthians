import requests

def get_game_transmission_info():
    print("Starting to fetch transmission info...")
    api_url = "https://api.gemini.example.com/getTransmissionInfo"
    params = {
        'team': 'Corinthians',
        'type': 'transmission'
    }
    headers = {
        'Authorization': 'Bearer YOUR_API_KEY'  # Substitua pela sua chave de API real
    }
    response = requests.get(api_url, params=params, headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(f"Transmission Info: {data.get('transmissionInfo', 'No info found')}")
        return data.get('transmissionInfo', 'No info found')
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return "Não foi possível obter as informações de transmissão."

def on_button_click():
    info = get_game_transmission_info()
    print(info)

if __name__ == "__main__":
    on_button_click()
