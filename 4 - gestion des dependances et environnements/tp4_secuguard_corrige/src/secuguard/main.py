from .analyzer import analyser_mot_de_passe
from .generator import generer_mot_de_passe

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Générer et Analyzer des mots de passe")

    parser.add_argument("--check", "-c", type=str, help="mot de passe à analyser")
    parser.add_argument("--length", "-l", type=int, default=12, help="longeur de mot de passe à générer")
    parser.add_argument("--no-digits", action="store_false", dest="avec_chiffres", help="Mot de passe sans chiffres")
    parser.add_argument("--no-symbols", action="store_false", dest="avec_symboles", help="Mot de passe sans symboles")

    args = parser.parse_args()

    if args.check is not None:
        analyser_mot_de_passe(args.check)

    else:
        mot_de_passe = generer_mot_de_passe(args.length, args.avec_chiffres, args.avec_symboles)
        print(mot_de_passe)