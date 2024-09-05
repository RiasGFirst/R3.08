
class Tasse:
    matiere: str = "céramique"

    def __init__(self, couleur: str, contenance: int, marque: str):
        self.couleur = couleur
        self.contenance = contenance
        self.marque = marque

    def __str__(self):
        return f"La tasse de matiere {self.matiere}, de couleur {self.couleur} et de marque {self.marque} a une contenance de {self.contenance} ml."

    def remplir(self, contenu: str):
        self.contenu = contenu

    def boire(self):
        del self.contenu
