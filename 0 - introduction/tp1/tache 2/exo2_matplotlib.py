import matplotlib.pyplot as plt

mois = [
    "Janvier",
    "Février",
    "Mars",
    "Avril",
    "Mai",
    "Juin",
    "Juillet",
    "Août",
    "Septembre",
    "Octobre",
    "Novembre",
    "Décembre",
]

visiteurs = [
    1200,
    1350,
    1600,
    1450,
    1800,
    2100,
    1950,
    1700,
    2200,
    2400,
    2600,
    3000,
]

x = mois
y = visiteurs

plt.plot(x, y)

plt.title("courbe representant l'evolution du nombre de visiteurs au fil des mois")
plt.xlabel("mois")
plt.ylabel("visiteurs")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('image.png')

plt.show()