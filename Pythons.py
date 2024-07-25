import requests

# Função para perguntar sobre a transmissão do jogo
def get_game_transmission_info():
    # URL do endpoint da API do Gemini (exemplo fictício)
    api_url = "https://api.gemini.example.com/getTransmissionInfo"
    
    # Parâmetros da requisição
    params = {
        'team': 'Corinthians',
        'type': 'transmission'
    }
    
    # Chave de API (se necessário)
    headers = {
        'Authorization': 'Bearer YOUR_API_KEY'
    }
    
    # Fazer a requisição para a API
    response = requests.get(api_url, params=params, headers=headers)
    
    # Verificar se a resposta foi bem-sucedida
    if response.status_code == 200:
        # Processar e retornar a informação
        data = response.json()
        return data['transmissionInfo']
    else:
        # Tratar erro
        return "Não foi possível obter as informações de transmissão."

# Função chamada ao clicar no botão
def on_button_click():
    info = get_game_transmission_info()
    print(info)  # Ou qualquer outra ação que você queira realizar
