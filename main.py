def afficher_menu():
    print("\n=== SYSTÈME DE TICKETS DE SUPPORT ===")
    print("1. Créer un ticket")
    print("2. Afficher les tickets")
    print("3. Modifier un ticket")
    print("4. Supprimer un ticket")
    print("5. Quitter")

def demander_choix():
    return input("Choisissez une option (1-5) : ")

def classe_ticket(ticket):
    mots_ticket = ticket.lower().removesuffix('.').replace(',', ' ').replace('.', ' ').split()
    mots_incident = ["plante", "arret", "hors", "ligne", "panne", "gelé"]
    mots_service = ["mot", "passe", "compte", "accès"]
    mots_changement = ["mise", "jour", "migration", "update", "changement"]
    mots_bug= ["bug", "bogue", "erreur", "code"]
    for mot in mots_ticket:
        if mot in mots_incident:
            classe = "incident"
            break
        elif mot in mots_service:
            classe = "demande_service"
            break
        elif mot in mots_changement:
            classe = "demande_changement"
            break
        elif mot in mots_bug:
            classe = "bug"
            break
        else:
            classe = "inconnu"
    return classe


from ticket import classe_ticket

tickets = []

#Creer
def creer_ticket():
    titre_ticket = input("Titre de la requête :")
    description_ticket = input("Description de la requête :")
    classe = classe_ticket(titre_ticket + " " + description_ticket)
    nouveau_ticket = {"classe": classe, "titre": titre_ticket, "description": description_ticket, "état": "Ouvert"}

    tickets.append(nouveau_ticket)

    print(nouveau_ticket)
    return tickets

#Read
def lire_tickets(tickets):
    if not tickets:
        print("Aucun ticket.")
        return
    print("====LISTE DE TICKETS====")
    for i, ticket in enumerate(tickets, 1):
        print(f"\nTicket # {i}")
        print(f'Classe : {ticket["classe"]}')
        print(f'Titre : {ticket["titre"]}')
        print(f'Description :\n{ticket["description"]}')
        print(f'État : {ticket["état"]}')

#Update
def update_ticket(tickets):
    # lire_tickets(tickets)
    if not tickets:
        return
    index = int(input("Entrez le numero du ticket a modifier : ")) - 1
    ticket = tickets[index]
    print("Laisser vide pour ne pas modifier")
    titre = input(f'titre actuel : {ticket["titre"]}\nNouveau titre: ')
    if titre:
        ticket["titre"] = titre
    description = input(f'Descrition actuel:\n{ticket["description"]}\nNouvelle description : ')
    if description:
        ticket["description"] = description
    etat = input(f'etat actuel : {ticket["état"]}\n(Ouvert / En Cours / Fermé): ')
    if etat:
        ticket["état"] = etat
    ticket["classe"] = classe_ticket(ticket["titre"] + " " + ticket["description"])
    print("\nTicket Modifié")

#Delete
def delete_ticket(tickets):
    lire_tickets(tickets)
    if not tickets:
        return
    index = int(input("Entrez le numero du ticket a supprimer:")) - 1
    ticket =tickets.pop(index)
    print(f'Ticket {ticket["titre"]} a été supprimé')

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

afficher_menu()
demander_choix()
creer_ticket()
lire_tickets(tickets)
update_ticket(tickets)
delete_ticket(tickets)
sauvegarder_tickets(tickets)
charger_tickets()