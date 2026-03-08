import requests

JOKE_API = "https://official-joke-api.appspot.com/random_joke"

def fetch_joke():

    response = requests.get(JOKE_API)
    data = response.json()

    return {
        "setup": data["setup"],
        "punchline": data["punchline"]
    }