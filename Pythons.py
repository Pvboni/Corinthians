import requests
import json

def consultar_gemini(prompt, api_key):
    """Envia uma consulta ao modelo Gemini e retorna a resposta."""
    url = "https://language.googleapis.com/v1/models/YOUR_MODEL:generateText"  # Substitua YOUR_MODEL pelo nome do seu modelo Gemini
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + api_key
    }
    data = {
        "prompt": prompt,
        # Adicione outros parâmetros como necessário, por exemplo:
        # "temperature": 0.7,
        # "maxTokens": 150,
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Verifica se ocorreu algum erro na requisição
        return response.json().get("response", "Resposta não encontrada.")  # Adapte conforme a estrutura da resposta
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
    api_key = "sua_chave_api_do_gemini"  # Substitua pela sua chave de API real
    prompt = "Onde posso assistir ao jogo do Corinthians hoje?"
    resposta = consultar_gemini(prompt, api_key)
    print(resposta)

if __name__ == "__main__":
    main()
