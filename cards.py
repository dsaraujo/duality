import json
import textwrap

JSON_FILE_PATH = 'cards.json'
    
try:
  with open(JSON_FILE_PATH, 'r', encoding='utf-8') as f:
    all_cards_data = json.load(f)
except FileNotFoundError:
  print(f"FATAL ERROR: The card data file '{JSON_FILE_PATH}' was not found.")
  print("Please make sure this script is in the same directory as the JSON file.")
  exit()
except json.JSONDecodeError:
  print(f"FATAL ERROR: Could not read the data from '{JSON_FILE_PATH}'.")
  print("The file might be corrupted or not a valid JSON.")
  exit()
  
print(f"Loaded {len(all_cards_data)} cards from '{JSON_FILE_PATH}'.")


def get_card_by_name(card_name: str):
  c = find_card(card_name)
  if c:
    return format_card(c[0])
  return "No card found with that name."

def format_card(card: dict):
  """Formats and prints a single card dictionary in a readable way."""

  wrapped_text = card.get("ability_text", "No description available.")

  # Build the output string
  output = f"""

**{card.get("ability_name", "Unknown Card").upper()}** | {card.get("domain", "N/A")} {card.get("level", "?")} | {card.get("recall_cost", "?")} ⚡| *{card.get("type", "N/A")}*

{wrapped_text}
"""
  return(output)


def find_card(search_term: str):
  """Searches for cards by ability name, case-insensitive."""
  if not search_term:
    return

  # Make the search case-insensitive
  search_term = search_term.lower()
  
  found_cards = [
    card for card in all_cards_data
    if search_term in card.get("ability_name", "").lower()
  ]

  return found_cards