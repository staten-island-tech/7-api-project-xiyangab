import requests

def getWord(word):
    response = requests.get(f"https://wordsapiv1.p.mashape.com/words/{word.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    return {
        "word": data["word"]
    }