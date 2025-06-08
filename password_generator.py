import random #importe module pour générer des valeurs aléatoires
import string #importe le module contenant des ensembles de caractères utile

def generate_password(length=12, use_digits=True, use_symbols=True):
    characters = string.ascii_lowercase #commence avec les lettres minuscules
    if use_digits:
        characters += string.digits #ajoutes les chiffres si demandés
    if use_symbols:
        characters += string.punctuation #ajoutes les symboles si demandés
    characters += string.ascii_uppercase #ajoutes toujours les lettres majuscules

    #crée un mot de passe en selectionnant au hasard des caractères
    password = ''.join(random.choice(characters) for _ in range(length))
    return password #retourne le mot de passe généré

if __name__ == "__main__":
    print("Generateur de mot de passe sécurisé") #affiche un titre

    #demande la longueur du mot de passe (avec valeur par défaut à 12)
    length = int(input("Longueur du mot de passe (ex:12) : ") or 12)

    #demande à l'utilisateur siu il veut des chiffres
    use_digits = input("Inclure des chiffres ? (o/n) :").lower() != "n"

    #demande à l'utilisateur s'il veut de ssymboles
    use_symbols = input("Inclure des symboles ? (o/n)").lower() != "n"

    #appelle la fonction pour générer le mot de passe avec les options choisies
    pwd = generate_password(length, use_digits, use_symbols)

    # Affiche le mot de passe généré
    print(f"\n mot de passe généré : {pwd}")
