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