import matplotlib.pyplot as plt

mois = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin",
        "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]

visiteurs = [1200, 1350, 1600, 1450, 1800,
             2100, 1950, 1700, 2200, 2400, 2600, 3000]

plt.plot(mois, visiteurs)

plt.title("evolution du nombre de visiteurs au fil des mois")
plt.xlabel("mois")
plt.ylabel("visiteurs")

plt.show()