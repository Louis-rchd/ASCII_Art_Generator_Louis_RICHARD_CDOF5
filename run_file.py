# Définir un dictionnaire pour les lettres en ASCII Art
ASCII_ART_MAP = {
    "A": [
        "        ",
        "_____   ",
        "\__  \  ",
        " / __ \_",
        "(____  /",
        "     \/ ",
    ],
    "B": [
        "___.    ",
        "\_ |__  ",
        " | __ \ ",
        " | \_\ \"",
        " |___  /",
        "     \/ ",
    ],
    "C": [
        "        ",
        "  ____  ",
        "_/ ___\ ",
        "\  \___ ",
        " \___  >",
        "     \/ ",
    ],
}

def generate_ascii_art(text):
    """
    Génère de l'ASCII Art pour le texte donné.
    """
    text = text.upper()  # Convertir le texte en majuscules
    lines = [""] * 6  # Chaque caractère prend 6 lignes d'ASCII Art

    for char in text:
        if char in ASCII_ART_MAP:
            # Ajouter l'ASCII Art du caractère à chaque ligne
            for i in range(6):
                lines[i] += ASCII_ART_MAP[char][i] + "  "  # Ajout d'un espace entre les lettres
        else:
            # Si le caractère n'est pas dans le dictionnaire, ajoutez un espace vide
            for i in range(6):
                lines[i] += " " * 8

    return "\n".join(lines)


# Programme principal
if __name__ == "__main__":
    print("Bienvenue dans le générateur d'ASCII Art !")
    user_input = input("Entrez un texte (A-Z uniquement) : ")
    ascii_art = generate_ascii_art(user_input)
    print("\nVoici votre ASCII Art :\n")
    print(ascii_art)
