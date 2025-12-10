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
    allSpeech = []
    allExample = []

    for meaning in data[0]["meanings"]:
        allSpeech.append(meaning["partOfSpeech"])
        for d in meaning.get("definitions", []):
            allDef.append(d["definition"])

    return allDef, allSpeech, allExample

word = getWord("punch")

print(word)