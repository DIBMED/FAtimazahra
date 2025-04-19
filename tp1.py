class Livre:
    def __init__(self, titre, auteur, annee_publication):
        self.titre = titre
        self.auteur = auteur
        self.annee_publication = annee_publication
        self.disponible = True  # Statut : disponible par défaut

    def afficher(self):
        statut = "Disponible" if self.disponible else "Emprunté"
        print(f"{self.titre} de {self.auteur}, publié en {self.annee_publication} ({statut})")

class Bibliotheque:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)

    def emprunter_livre(self, titre):
        for livre in self.livres:
            if livre.titre == titre:
                if livre.disponible:
                    livre.disponible = False
                    return f"Vous avez emprunté '{titre}'."
                else:
                    raise Exception(f"Le livre '{titre}' est déjà emprunté.")
        raise Exception(f"Le livre '{titre}' n'existe pas dans la bibliothèque.")

    def rendre_livre(self, titre):
        for livre in self.livres:
            if livre.titre == titre:
                if not livre.disponible:
                    livre.disponible = True
                    return f"Vous avez rendu '{titre}'."
                else:
                    raise Exception(f"Le livre '{titre}' est déjà disponible.")
        raise Exception(f"Le livre '{titre}' n'existe pas dans la bibliothèque.")

    def afficher_livres_disponibles(self):
        return [livre.afficher() for livre in self.livres if livre.disponible]
ma_bibliotheque=Bibliotheque()
# Créer des instances de Livre
livre1 = Livre("1984", "George Orwell", 1949)
livre2 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 1943)
livre3 = Livre("Les Misérables", "Victor Hugo", 1862)

# Ajouter les livres à la bibliothèque
ma_bibliotheque.ajouter_livre(livre1)
ma_bibliotheque.ajouter_livre(livre2)
ma_bibliotheque.ajouter_livre(livre3)
print(ma_bibliotheque.afficher_livres_disponibles())