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

#Update
def update_ticket(tickets):
    lire_tickets(tickets)
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
    index = int(input("Entrez le numero du ticket a supprimer")) - 1
    ticket =tickets.pop(index)
    print(f'Ticket {ticket["titre"]} a été supprimé')