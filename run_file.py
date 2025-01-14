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
        " | \_\ \\",
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
    "D": [
        "    .___",
        "  __| _/",
        " / __ | ",
        "/ /_/ | ",
        "\____ | ",
        "     \/ ",
    ],
    "E": [
        "        ",
        "  ____  ",
        "_/ __ \ ",
        "\  ___/ ",
        " \___  >",
        "     \/ ",
    ],
    "F": [
        "___________",
        "\_   _____/",
        " |    __)  ",
        " |     \   ",
        " \___  /   ",
        "     \/    ",
    ],
    "G": [
        "  ________ ",
        " /  _____/ ",
        "/   \  ___ ",
        "\    \_\  \\",
        " \______  /",
        "        \/ ",
    ],
    "H": [
        "  ___ ___ ",
        " /   |   \  ",
        "/    ~    \\",
        "\    Y    / ",
        " \___|_  /  ", 
        "       \/   ",       
    ],
    "I": [
        ".___ ",
        "|   |",
        "|   |",
        "|   |",
        "|___|",
        "     ",
    ],
    "J": [
        "     ____.",
        "    |    |",
        "    |    |",
        "/\__|    |",
        "\________|",
        "          ",
    ],
    "K": [
        " ____  __.",
        "|    |/ _|",
        "|      <  ",
        "|    |  \ ",
        "|____|__ \\",
        "        \/",
    ],
    "L": [
        ".____     ",
        "|    |    ",
        "|    |    ",
        "|    |___ ",
        "|_______ )",
        "        \/",
    ],
    "M": [
        "   _____   ",
        "  /     \  ",
        " /  \ /  \ ",
        "/    Y    \\",
        "\____|__  /",
        "        \/ ",
    ],
    "N": [
        " _______   ",
        " \      \  ",
        " /   |   \ ",
        "/    |    \\",
        "\____|__  /",
        "        \/ ",
    ],
    "O": [
        "________   ",
        "\_____  \  ",
        " /   |   \ ",
        "/    |    \\",
        "\_______  /",
        "        \/ ",
    ],
    "P": [
        "__________ ",
        "\______   \\",
        " |     ___/",
        " |    |    ",
        " |____|    ",
        "           ",
    ],
    "Q": [
        "________   ",
        "\_____  \  ",
        " /  / \  \ ",
        "/   \_/.  \\",
        "\_____\ \_/",
        "       \__>",
    ],
    "R": [
        "__________ ",
        "\______   \\",
        " |       _/",
        " |    |   \\",
        " |____|_  /",
        "        \/ ",
    ],
    "S": [
        "  _________",
        " /   _____/",
        " \_____  \ ",
        " /        \\",
        "/_______  /",
        "        \/ ",
    ],
    "T": [
        "___________",
        "\__    ___/",
        "  |    |   ",
        "  |    |   ",
        "  |____|   ",
        "           ",
    ],
    "U": [
        " ____ ___ ",
        "|    |   \\",
        "|    |   /",
        "|    |  / ",
        "|______/  ",
        "          ",
    ],
    "V": [
        "____   ____",
        "\   \ /   /",
        " \   Y   / ",
        "  \     /  ",
        "   \___/   ",
        "           ",
    ],
    "W": [
        " __      __ ",
        "/  \    /  \\",
        "\   \/\/   /",
        " \        / ",
        "  \__/\  /  ",
        "       \/   ",
    ],
    "X": [
        "____  ___",
        "\   \/  /",
        " \     / ",
        " /     \ ",
        "/___/\  \\",
        "      \_/",
    ],
    "Y": [
        "_____.___.",
        "\__  |   |",
        " /   |   |",
        " \____   |",
        " / ______|",
        " \/       ",
    ],
    "Z": [
        "__________",
        "\____    /",
        "  /     / ",
        " /     /_ ",
        "/_______ \\",
        "        \/",
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
