# https://dictionaryapi.dev/
import tkinter as tk
from tkinter import messagebox
import requests

def getWord(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()

    allDef = []

    for meaning in data[0]["meanings"]:
        for d in meaning["definitions"]:
            allDef.append(d["definition"])

    return allDef

word = getWord("punch")

print(word[2])