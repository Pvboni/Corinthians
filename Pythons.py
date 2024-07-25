import os
import requests
import json

def consultar_gemini(prompt):
    """Envia uma consulta ao modelo Gemini e retorna a resposta."""
    api_key = os.getenv('API_KEY')  # Obtém a chave da API a partir da variável de ambiente
    if not api_key:
        raise ValueError("A chave da API não está configurada.")
    
    url = "https://api.gemini.example.com/v1/getTransmissionInfo"  # Substitua pelo URL correto da API Gemini
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "prompt": prompt,
    }
    try:
        print(f"Enviando requisição para: {url}")  # Adiciona uma mensagem de diagnóstico
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Verifica se a requisição foi bem-sucedida
        print(f"Status Code: {response.status_code}")  # Adiciona uma mensagem de diagnóstico
        return response.json().get("response", "Resposta não encontrada.")
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")
    return "Erro na consulta ao modelo Gemini."

def main():
    prompt = "Onde posso assistir ao jogo do Corinthians hoje?"
    resposta = consultar_gemini(prompt)
    print(resposta)

if __name__ == "__main__":
    main()
