import requests
import json
import os

def consultar_gemini(prompt):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("A chave da API não está configurada.")
    
    url = "https://aiplatform.googleapis.com/v1/projects/297539322373/locations/us-central1/models/Generative_Language_Client:predict"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = json.dumps({
        "instances": [
            {"content": prompt}
        ]
    })

    try:
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()
        response_json = response.json()
        return response_json.get("predictions", [{}])[0].get("content", "Resposta não encontrada.")
    except requests.exceptions.HTTPError as errh:
        response_json = response.json()
        error_message = response_json.get("error", {}).get("message")
        print(f"HTTP Error: {errh} - {error_message}")
        return "Erro ao consultar o modelo."
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")
        return "Erro ao consultar o modelo."
    except json.decoder.JSONDecodeError:
        print("Erro ao decodificar a resposta JSON.")
        return "Erro ao consultar o modelo."

def main():
    prompt = "Onde posso assistir ao jogo do Corinthians hoje?"
    resposta = consultar_gemini(prompt)
    print(resposta)

if __name__ == "__main__":
    main()
