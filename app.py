#https://dictionaryapi.dev/
import tkinter as tk
from tkinter import messagebox
import requests

# --- API FUNCTION ---
def get_definitions(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)

    if response.status_code != 200:
        return None  # Word not found or API error

    data = response.json()
    definitions = []

    for meaning in data[0]["meanings"]:
        for d in meaning["definitions"]:
            definitions.append(d["definition"])

    return definitions


# --- TKINTER APP ---
def lookup_word():
    word = entry.get().strip()
    listbox.delete(0, tk.END)

    if not word:
        messagebox.showwarning("Input required", "Please enter a word.")
        return

    defs = get_definitions(word)

    if defs is None:
        listbox.insert(tk.END, "No definitions found.")
    else:
        for i, d in enumerate(defs, start=1):
            listbox.insert(tk.END, f"{i}. {d}")
            listbox.bind("<<ListboxSelect>>", on_select)
                def on_select(event):
                    selection = listbox.curselection()
                    if not selection:
                        return
                    
                    index = selection[0]
                    value = listbox.get(index)
                    messagebox.showinfo("Definition clicked", value)


# --- WINDOW SETUP ---
root = tk.Tk()
root.title("xiyangs super amazing dictionary")

# Input frame
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Enter a word:").grid(row=0, column=0, padx=5)
entry = tk.Entry(frame, width=30)
entry.grid(row=0, column=1, padx=5)

btn = tk.Button(frame, text="Look Up", command=lookup_word)
btn.grid(row=0, column=2, padx=5)

# Listbox for definitions
listbox = tk.Listbox(root, width=80, height=15)
listbox.pack(pady=10)

# Optional scrollbar
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

root.mainloop()