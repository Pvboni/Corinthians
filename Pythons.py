import os
import requests
import json

def consultar_gemini(prompt):
    """Envia uma consulta ao modelo Gemini e retorna a resposta."""
    api_key = os.getenv('API_KEY')  # Obtém a chave da API a partir da variável de ambiente
    if not api_key:
        raise ValueError("A chave da API não está configurada.")
    
    model_id = "Generative_Language_Client"  # ID do modelo
    project_id = "297539322373"  # Número do projeto
    url = f"https://aiplatform.googleapis.com/v1/projects/{project_id}/locations/us-central1/models/{model_id}:predict"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    data = {
        "instances": [{"prompt": prompt}]  # Dados de entrada para o modelo
    }
    
    try:
        print(f"Enviando requisição para: {url}")  # Adiciona uma mensagem de diagnóstico
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Verifica se a requisição foi bem-sucedida
        
        # Verifica se o conteúdo da resposta é JSON
        try:
            response_json = response.json()
            print(f"Status Code: {response.status_code}")  # Adiciona uma mensagem de diagnóstico
            return response_json.get("predictions", [{}])[0].get("content", "Resposta não encontrada.")
        except json.JSONDecodeError:
            print("Erro ao decodificar a resposta. A resposta não é JSON ou está vazia.")
            print(f"Conteúdo da resposta: {response.text}")
    except requests.exceptions.HTTPError as errh:
        response_text = response.text
        print(f"HTTP Error: {errh} - Conteúdo da resposta: {response_text}")
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
