import json

FICHIER = "tickets.json"  
def sauvegarder_tickets(tickets):
    with open(FICHIER, "w") as f:
        json.dump(tickets, f, indent=4)
    print(f"{len(tickets)} ticket(s) sauvegardé(s) dans {FICHIER}.")

def charger_tickets():
    try:
        with open(FICHIER, "r") as f:
            tickets = json.load(f)
        return tickets
    except FileNotFoundError:
        return []
