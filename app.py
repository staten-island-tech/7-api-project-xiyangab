# https://dictionaryapi.dev/
import tkinter as tk
from tkinter import messagebox
import requests

# ---------------- API FUNCTION ----------------
def get_word(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()
    definitions = []
    speeches = []

    for meaning in data[0]["meanings"]:
        speeches.append(meaning["partOfSpeech"])
        for d in meaning["definitions"]:
            definitions.append(d["definition"])

    return definitions, speeches

# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("XIYANG'S Amazing Dictionary")
root.geometry("700x500")

# ---------------- THREE SCREENS ----------------
main_frame = tk.Frame(root)
detail_frame = tk.Frame(root)
speech_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=True)

# ---------------- MAIN SCREEN UI ----------------
tk.Label(main_frame, text="Enter a word:", font=("Arial", 14)).grid(row=0, column=0, padx=10, pady=30)

entry = tk.Entry(main_frame, width=30, font=("Arial", 14))
entry.grid(row=0, column=1, padx=10)

definitions_list = []
speech_list = []

def lookup_word():
    global definitions_list, speech_list

    word = entry.get().strip()
    listbox.delete(0, tk.END)

    if not word:
        messagebox.showwarning("Input required", "Please enter a word.")
        return

    result = get_word(word)
    if result is None:
        listbox.insert(tk.END, "No definitions found.")
        return

    definitions_list, speech_list = result

    for i, d in enumerate(definitions_list, start=1):
        listbox.insert(tk.END, f"{i}. {d}")

btn = tk.Button(main_frame, text="Look Up", font=("Arial", 12), command=lookup_word)
btn.grid(row=0, column=2, padx=10)

# Listbox
listbox = tk.Listbox(main_frame, height=20, font=("Arial", 12), bg="#ffc383")
listbox.grid(row=1, column=0, columnspan=3, pady=40, padx=50, sticky="nsew")

main_frame.grid_rowconfigure(1, weight=1)
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=1)
main_frame.grid_columnconfigure(2, weight=1)

# ---------------- SWITCHING SCREENS ----------------
def detail(text):
    detail_label.config(text=text)
    main_frame.pack_forget()
    speech_frame.pack_forget()
    detail_frame.pack(fill="both", expand=True)

def on_select(event):
    index = listbox.nearest(event.y)

    # Prevent clicks outside actual items
    if index < 0 or index >= listbox.size():
        return

    value = listbox.get(index)
    detail(value)

listbox.bind("<Double-Button-1>", on_select)

# ---------------- DETAIL SCREEN UI ----------------
detail_label = tk.Label(detail_frame, text="", wraplength=650, justify="left", font=("Arial", 14))
detail_label.pack(pady=40)

def show_main():
    speech_frame.pack_forget()
    detail_frame.pack_forget()
    main_frame.pack(fill="both", expand=True)

def show_speech():
    detail_frame.pack_forget()
    speech_frame.pack(fill="both", expand=True)
    update_speech_screen()

def show_detail():
    speech_frame.pack_forget()

partOfSpeech_btn = tk.Button(detail_frame, text="Part of Speech", font=("Arial", 12), command=show_speech)
partOfSpeech_btn.pack()

back_button = tk.Button(detail_frame, text="Back", font=("Arial", 12), command=show_main)
back_button.pack()

main_frame.config(bg="#6dafe6")
detail_frame.config(bg="#eb7373")
speech_frame.config(bg="#d6aaff")

# ---------------- SPEECH SCREEN -----------------
speech_label = tk.Label(speech_frame, text="", wraplength=650, justify="left", font=("Arial", 14))
speech_label.pack(pady=40)

speech_back = tk.Button(speech_frame, text="Back", font=("Arial", 12), command=show_detail)
speech_back.pack()

def update_speech_screen():
    if speech_list:
        text = "Parts of Speech:\n\n" + "\n".join(f"- {s}" for s in speech_list)
    else:
        text = "No part of speech data available."
    speech_label.config(text=text)

# ---------------- RUN APP ----------------
root.mainloop()