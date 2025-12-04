#https://dictionaryapi.dev/
import tkinter as tk
from tkinter import messagebox
import requests

# ---------------- API FUNCTION ----------------
def get_definitions(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()
    definitions = []

    for meaning in data[0]["meanings"]:
        for d in meaning["definitions"]:
            definitions.append(d["definition"])

    return definitions


# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("Dictionary Lookup")
root.geometry("700x500")


# ---------------- TWO SCREENS (FRAMES) ----------------
main_frame = tk.Frame(root)
detail_frame = tk.Frame(root)

main_frame.pack(fill="both", expand=True)


# ---------------- MAIN SCREEN UI ----------------
tk.Label(main_frame, text="Enter a word:", font=("Arial", 14)).grid(row=0, column=0, padx=10, pady=30)

entry = tk.Entry(main_frame, width=30, font=("Arial", 14))
entry.grid(row=0, column=1, padx=10)

def lookup_word():
    word = entry.get().strip()
    listbox.delete(0, tk.END)

    if not word:
        messagebox.showwarning("Input required", "Please enter a word.")
        return

    defs = get_definitions(word)
    if defs is None:
        listbox.insert(tk.END, "No definitions found.")
        return

    for i, d in enumerate(defs, start=1):
        listbox.insert(tk.END, f"{i}. {d}")

btn = tk.Button(main_frame, text="Look Up", font=("Arial", 12), command=lookup_word)
btn.grid(row=0, column=2, padx=10)

# Listbox for definitions
listbox = tk.Listbox(main_frame, height=20, font=("Arial", 12))
listbox.grid(row=1, column=0, columnspan=3, pady=40, padx=50, sticky="nsew")
listbox.config(bg="#ffc383")

main_frame.grid_rowconfigure(1, weight=1)
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=1)
main_frame.grid_columnconfigure(2, weight=1)

# ---------------- DETAIL SCREEN UI ----------------
detail_label = tk.Label(detail_frame, text="", wraplength=650, justify="left", font=("Arial", 14))
detail_label.pack(pady=40)

def show_main():
    detail_frame.pack_forget()
    main_frame.pack(fill="both", expand=True)

def show_speech():
    
partOfSpeech = tk.Button(detail_frame, text="Part of Speech", font=("Arial", 12), bg="#f3f160", padx=30, pady=30)
partOfSpeech.pack()
back_button = tk.Button(detail_frame, text="Back", font=("Arial", 12), command=show_main)
back_button.pack()


main_frame.config(bg="#6dafe6")
detail_frame.config(bg="#eb7373")

# ---------------- SWITCHING SCREENS ----------------
def show_detail(text):
    detail_label.config(text=text)
    main_frame.pack_forget()
    detail_frame.pack(fill="both", expand=True)


def on_select(event):
    # Find index of clicked row
    index = listbox.nearest(event.y)

    # Ignore clicks outside real items
    if index < 0 or index >= listbox.size():
        return

    value = listbox.get(index)
    show_detail(value)


# Bind click event
listbox.bind("<Double-Button-1>", on_select)


# ---------------- RUN APP ----------------
root.mainloop()
