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
def search():
    word = entry.get().strip()

    if not word:
        messagebox.showwarning("Missing word", "Please enter a word to search.")
        return
    
    get = getWord(word)

    if get == None:
        messagebox.showwarning("Not found",f"Could not find {word}")
        return

    definitions, speech, examples = get
    
    if get:
        text_to_show = ""
        for d in definitions:
            text_to_show += f"• {d}\n\n"
        deflabel.config(text=text_to_show)

#ui
root = tk.Tk()
root.title("XIYANGS amazing dictionary")
root.geometry("1920x1080")

entry = tk.Entry(root, width=50, font=("Arial", 14))
entry.pack(pady=5)

searchBt = tk.Button(root, width=20, text="Search", command=search)
searchBt.pack(pady=10)

deflabel = tk.Label(root, width=40, text="", wraplength=400, justify=LEFT, font=("Arial", 14))
deflabel.pack(pady=40)

root.mainloop