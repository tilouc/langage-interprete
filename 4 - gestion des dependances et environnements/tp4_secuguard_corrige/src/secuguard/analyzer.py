from colorama import Fore, Style, init

init(autoreset=True)

def analyser_mot_de_passe ( mot_de_passe : str ) -> str:
    longueur = len(mot_de_passe)

    contient_lettre = False
    contient_chiffre = False
    contient_symboles = False

    for c in mot_de_passe:
        if c.isalpha():
            contient_lettre = True
            break

    for c in mot_de_passe:
            if c.isdigit():
                contient_chiffre = True
                break

    for c in mot_de_passe:
            if not c.isalnum():
                contient_symboles = True
                break

    if longueur >= 12 and contient_lettre and contient_chiffre and contient_symboles:
        print(Fore.GREEN + "[FORT] Mot de passe tres solide")

    elif longueur>=8 and (contient_lettre and contient_chiffre) or (contient_lettre and contient_symboles) or \
        (contient_symboles and contient_chiffre):
        print(Fore.YELLOW + "[MOYEN] Mot de passe acceptable")
    else:
        print(Fore.RED + "[FAIBLE] Mot de passe trop court et prévisible")