import requests
import json
import os

def consultar_gemini(prompt):
    """Envia uma consulta ao modelo Gemini e retorna a resposta."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("A chave da API não está configurada.")
    
    url = "https://aiplatform.googleapis.com/v1/projects/297539322373/locations/us-central1/models/Generative_Language_Client:predict"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = json.dumps({
        "prompt": prompt,
        # Outros parâmetros específicos do modelo, se necessário
    })
    
    print(f"Enviando requisição para: {url}")  # Mensagem de depuração
    try:
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()  # Verifica se houve um erro HTTP
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
        print(f"Conteúdo da resposta: {response.text}")
        raise
    except requests.exceptions.RequestException as err:
        print(f"Erro ao fazer a requisição: {err}")
        raise
    
    try:
        response_json = response.json()
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar o JSON: {e}")
        print(f"Conteúdo da resposta: {response.text}")
        raise
    
    return response_json.get("response", "Resposta não encontrada")  # Adapte conforme a estrutura da resposta do Gemini

def main():
    prompt = "Onde posso assistir ao jogo do Corinthians hoje?"
    try:
        resposta = consultar_gemini(prompt)
        print(resposta)
    except Exception as e:
        print(f"Erro na consulta ao modelo Gemini: {e}")

if __name__ == "__main__":
    main()
