from ticket import classe_ticket

tickets = []

#Creer
def creer_ticket(tickets):
    titre_ticket = input("Titre de la requête :")
    description_ticket = input("Description de la requête :")
    classe = classe_ticket(titre_ticket + " " + description_ticket)
    nouveau_ticket = {"classe": classe, "titre": titre_ticket, "description": description_ticket, "état": "Ouvert"}

    tickets.append(nouveau_ticket)

    print(nouveau_ticket)

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