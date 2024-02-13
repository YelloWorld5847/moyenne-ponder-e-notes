import cgi

form = cgi.FieldStorage()
notes_entrees = form.getvalue("notes")

# Appelez vos fonctions pour calculer la moyenne pondérée ici
def ranger_notes_et_coefficient(entrée):
    # Remplacer toutes les virgules par des points
    entrée = entrée.replace(',', '.')

    notes_et_coefficient = {}
    notes_coefficient_liste = entrée.split(';')
    for note_coefficient in notes_coefficient_liste:
        note, coefficient = note_coefficient.split(':')
        notes_et_coefficient[float(note)] = float(coefficient)
    return notes_et_coefficient

def calculer_moyenne_pondérée(notes_coefficients):
    # Initialiser la somme des produits et la somme des coefficients
    somme_produits = 0
    somme_coefficients = 0

    # Parcourir les notes et coefficients dans le dictionnaire
    for note, coefficient in notes_coefficients.items():
        # Calculer le produit de la note par son coefficient
        produit = note * coefficient
        # Ajouter le produit à la somme des produits
        somme_produits += produit
        # Ajouter le coefficient à la somme des coefficients
        somme_coefficients += coefficient

    # Calculer la moyenne pondérée
    moyenne_pondérée = somme_produits / somme_coefficients

    return moyenne_pondérée


notes_coefficient_dict = ranger_notes_et_coefficient(notes_entrees)

moyenne = calculer_moyenne_pondérée(notes_coefficient_dict)
print("La moyenne pondérée est :", moyenne)
print("Content-type: text/html\n")
print(f"La moyenne pondérée est : {moyenne}")
