def classe_ticket(ticket: str):
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


