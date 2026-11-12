import datetime as dt

def entete():
    date = dt.datetime.now().strftime("%Y-%m-%d")
    return f"Convertisseur - {date}"

def formater(valeur, unite):
    return f"{valeur:.2f} {unite}"