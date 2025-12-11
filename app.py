# https://dictionaryapi.dev/
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import requests

# -------------------- API FUNCTION --------------------
def getWord(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()

    allDef = []
    allSpeech = []
    allExample = []

    for meaning in data[0].get("meanings", []):
        pos = meaning.get("partOfSpeech", "")
        allSpeech.append(pos)

        for d in meaning.get("definitions", []):
            definition = d.get("definition", "")
            allDef.append(definition)

            example = d.get("example")
            if example:
                allExample.append(example)

    return allDef, allSpeech, allExample


#tkinter app
root = tk.Tk()
root.title("XIYANGS amazing dictionary")
root.geometry("1000x1000")
entry = tk.Entry(root, width=50)

def search():
    word = entry.get().strip()

    if not word:
        messagebox