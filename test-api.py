import requests

# Hardcoded API key (intentional vulnerability for testing)
API_KEY = "sk-1234567890abcdef"

def get_data():
    response = requests.get(
        "https://api.example.com/data",
        headers={"Authorization": f"Bearer {API_KEY}"}
    )
    return response.json()
