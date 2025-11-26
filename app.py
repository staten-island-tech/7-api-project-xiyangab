import requests

def getPoke(poke):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    return {
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"],
        "types": [t["type"]["name"] for t in data["types"]]
    }

""" pokemon = getPoke("Bulbasaur")
for key, value in pokemon.items():
    print(key, "→", value)
 """
import tkinter as tk
from tkinter import ttk

# -----------------------------
# Tkinter GUI (UI ONLY — no logic)
# -----------------------------

def run_gui():
    root = tk.Tk()
    root.title("Pokémon Viewer")
    root.geometry("700x600")

    # ---------- Search Bar ----------
    top_frame = tk.Frame(root)
    top_frame.pack(pady=10)

    tk.Label(top_frame, text="Search Pokémon:").pack(side="left", padx=5)

    search_entry = tk.Entry(top_frame, width=30)
    search_entry.pack(side="left", padx=5)

    search_button = tk.Button(top_frame, text="Search", command=lambda: on_search(search_entry.get()))
    search_button.pack(side="left", padx=5)

    # ---------- Buttons Row ----------
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    tk.Button(button_frame, text="List by Type", width=15, command=on_type_button).pack(side="left", padx=5)
    tk.Button(button_frame, text="List by Generation", width=15, command=on_gen_button).pack(side="left", padx=5)
    tk.Button(button_frame, text="Sort Pokémon", width=15, command=on_sort_button).pack(side="left", padx=5)

    # ---------- Scrollable Results Area ----------

    results_frame = tk.Frame(root)
    results_frame.pack(fill="both", expand=True, pady=10)

    canvas = tk.Canvas(results_frame)
    scroll_y = tk.Scrollbar(results_frame, orient="vertical", command=canvas.yview)

    scroll_frame = tk.Frame(canvas)

    scroll_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
    canvas.configure(yscrollcommand=scroll_y.set)

    canvas.pack(side="left", fill="both", expand=True)
    scroll_y.pack(side="right", fill="y")

    # Save reference so logic can update UI later
    root.scroll_frame = scroll_frame

    root.mainloop()


# -----------------------------
# Placeholder functions (YOU will fill these later)
# -----------------------------

def on_search(pokemon_name):
    print("[LOGIC GOES HERE] Search for:", pokemon_name)
    # You will fetch from PokeAPI here
    # Then update GUI results
    
    pokemon = getPoke(pokemon_name)
    for key, value in pokemon.items():
        print(key, "→", value)

def on_type_button():
    print("[LOGIC GOES HERE] List Pokémon by type")


def on_gen_button():
    print("[LOGIC GOES HERE] List Pokémon by generation")


def on_sort_button():
    print("[LOGIC GOES HERE] Sort Pokémon")


# -----------------------------
# Run GUI (for testing)
# -----------------------------

if __name__ == "__main__":
    run_gui()
