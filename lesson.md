# 🧠 Lesson: Catching Pokémon with Python 

### SWBAT (Students Will Be Able To):

* Explain what the `requests` library does and why we use it
* Use list comprehensions to make new lists quickly
* Use `.items()` to loop through key-value pairs in a dictionary

---

## 🕹️ Step 1: What’s happening in our code?

```python
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

pokemon = getPoke("Bulbasaur")
print(pokemon)
```

---

## 🧩 Step 2: Understanding `requests`

Imagine your Python program as a **trainer** 👩‍💻 sending a message to a **Pokémon Center** 🏥 (the internet).

When you do:

```python
requests.get("https://pokeapi.co/api/v2/pokemon/bulbasaur")
```

you’re saying:

> “Hey Pokémon Center! Please send me all the information you have on Bulbasaur!”

The center sends back a **big package** 📦 of data.
That package is called a **response**.

We open the box using:

```python
data = response.json()
```

Now we can see everything inside — names, types, height, weight, etc.
It’s like opening a Pokédex entry!

---

## 🧠 Step 3: What is a Dictionary?

A **dictionary** in Python is like a **backpack with labeled pockets** 🎒.

Example:

```python
pokemon = {
    "name": "Bulbasaur",
    "type": "grass",
    "weight": 69
}
```

Each pocket has:

* A **key** (the label) → `"name"`, `"type"`, `"weight"`
* A **value** (what’s inside) → `"Bulbasaur"`, `"grass"`, `69`

So when you ask:

```python
print(pokemon["type"])
```

Python looks for the pocket labeled `"type"` and gives you `"grass"` 🌿.

---

## 🔍 Step 4: Looping with `.items()`

What if you want to look inside **every pocket** in your backpack?

You can use:

```python
for key, value in pokemon.items():
    print(key, "→", value)
```

Output:

```
name → Bulbasaur
type → grass
weight → 69
```

Analogy:

> `.items()` lets you say, “Show me *each pocket label* and *what’s inside it*.”

---

## ⚡ Step 5: What’s that weird `[t["type"]["name"] for t in data["types"]]` thing?

That’s called a **list comprehension** — a short way to make a new list.

The long way would be:

```python
types = []
for t in data["types"]:
    types.append(t["type"]["name"])
```

The short version:

```python
types = [t["type"]["name"] for t in data["types"]]
```

Analogy:

> Think of it like making a tray of cookies 🍪.
> You take each dough ball (`t`) and shape it into a cookie (`t["type"]["name"]`).
> When you’re done, you have a whole new tray (a new list).

---

## 🧠 Step 6: Putting it all together

After your function runs, you get something like:

```python
{
  'name': 'bulbasaur',
  'height': 7,
  'weight': 69,
  'types': ['grass', 'poison']
}
```

Now you can use `.items()` to print it nicely:

```python
pokemon = getPoke("Bulbasaur")

for key, value in pokemon.items():
    print(f"{key.title()}: {value}")
```

Output:

```
Name: bulbasaur
Height: 7
Weight: 69
Types: ['grass', 'poison']
```

---

## 🧠 Recap

| Concept            | What it does                   | Analogy                                |
| ------------------ | ------------------------------ | -------------------------------------- |
| `requests.get()`   | Gets info from a website       | Sending a letter to the Pokémon Center |
| `.json()`          | Opens the package              | Opening your data box                  |
| Dictionary         | Stores info as key:value       | Backpack with labeled pockets          |
| `.items()`         | Loops through both key + value | Checking every pocket                  |
| List comprehension | Builds new lists quickly       | Cookie cutter for data                 |

---