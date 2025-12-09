# https://dictionaryapi.dev/
import tkinter as tk
from tkinter import messagebox
import requests

selected_index = -1

# ---------------- API FUNCTION ----------------
def get_word(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()

    definitions = []
    speeches = []
    sentences = []

    for meaning in data[0]["meanings"]:
        speeches.append(meaning["partOfSpeech"])

        for d in meaning["definitions"]:
            definitions.append(d.get("definition", ""))

            # sentence tied to THIS definition
            example = d.get("example", "No example available.")
            sentences.append(example)

    return definitions, speeches, sentences

# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("XIYANG'S Amazing Dictionary")
root.geometry("700x500")

# ---------------- SCREENS ----------------
main_frame = tk.Frame(root)
detail_frame = tk.Frame(root)
speech_frame = tk.Frame(root)
sentence_frame = tk.Frame(root)

main_frame.pack(fill="both", expand=True)

# ---------------- MAIN SCREEN ----------------
tk.Label(main_frame, text="Enter a word:", font=("Arial", 14)).grid(row=0, column=0, padx=10, pady=30)

entry = tk.Entry(main_frame, width=30, font=("Arial", 14))
entry.grid(row=0, column=1, padx=10)

definitions_list = []
speech_list = []
sentence_list = []

def lookup_word():
    global definitions_list, speech_list, sentence_list

    word = entry.get().strip()
    listbox.delete(0, tk.END)

    if not word:
        messagebox.showwarning("Input required", "Please enter a word.")
        return

    result = get_word(word)
    if result is None:
        listbox.insert(tk.END, "No definitions found.")
        return

    definitions_list, speech_list, sentence_list = result

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

# ---------------- NAVIGATION HANDLING ----------------
def switch_to(frame):
    """Hide all frames and show the selected one."""
    for f in (main_frame, detail_frame, speech_frame, sentence_frame):
        f.pack_forget()
    frame.pack(fill="both", expand=True)

# ---------------- DETAIL SCREEN ----------------
detail_label = tk.Label(detail_frame, text="", wraplength=650, justify="left", font=("Arial", 14))
detail_label.pack(pady=40)

def detail(text):
    detail_label.config(text=text)
    switch_to(detail_frame)

def on_select(event):
    global selected_index

    index = listbox.nearest(event.y)

    if index < 0 or index >= listbox.size():
        return

    selected_index = index
    detail(listbox.get(index))

listbox.bind("<Double-Button-1>", on_select)

# DETAIL SCREEN BUTTONS
tk.Button(detail_frame, text="Part of Speech", font=("Arial", 12),
          command=lambda: [update_speech_screen(), switch_to(speech_frame)]
         ).pack()

tk.Button(detail_frame, text="Example Sentences", font=("Arial", 12),
          command=lambda: [update_sentence_screen(), switch_to(sentence_frame)]
         ).pack()

tk.Button(detail_frame, text="Back", font=("Arial", 12),
          command=lambda: switch_to(main_frame)).pack()

# ---------------- SPEECH SCREEN ----------------
speech_label = tk.Label(speech_frame, text="", wraplength=650, justify="left", font=("Arial", 14))
speech_label.pack(pady=40)

tk.Button(speech_frame, text="Back", font=("Arial", 12),
          command=lambda: switch_to(detail_frame)).pack()

def update_speech_screen():
    if speech_list:
        text = "Parts of Speech:\n\n" + "\n".join(f"- {s}" for s in speech_list)
    else:
        text = "No part of speech info available."
    speech_label.config(text=text)

# ---------------- SENTENCE SCREEN ----------------
sentence_label = tk.Label(sentence_frame, text="", wraplength=650, justify="left", font=("Arial", 14))
sentence_label.pack(pady=40)

tk.Button(sentence_frame, text="Back", font=("Arial", 12),
          command=lambda: switch_to(detail_frame)).pack()

def update_sentence_screen():
    if 0 <= selected_index < len(sentence_list):
        sentence_label.config(text="Example Sentence:\n\n- " + sentence_list[selected_index])
    else:
        sentence_label.config(text="No example available.")

# ---------------- COLORS ----------------
main_frame.config(bg="#6dafe6")
detail_frame.config(bg="#eb7373")
speech_frame.config(bg="#d6aaff")
sentence_frame.config(bg="#ffdf9e")

# ---------------- RUN APP ----------------
root.mainloop()