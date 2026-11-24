# langage interprete

# notes de cours

notes du module « langage interprété » (junia isen lille, 1ère année cycle ingénieur, 2026-2027, enseignant : abderrahmane kasmi).

je les écris au fur et à mesure que j'avance, chapitre par chapitre, avec mes mots et des analogies simples. le but : pouvoir tout relire en une fois avant un examen et tout comprendre sans les slides.

## sommaire

| chapitre | sujet | statut |
|---|---|---|
| 0 | [introduction au module](#chapitre-0--le-cadre-du-module) | ✅ |
| 1 | [langages interprétés et écosystèmes modernes](#chapitre-1--langages-interprétés-et-écosystèmes-modernes) | ✅ |
| 2 | structures de données et écriture idiomatique | ⏳ |
| 3 | modularisation et organisation de projet | ⏳ |
| 4 | gestion des dépendances et environnements | ⏳ |
| 5 | manipulation de données structurées | ⏳ |
| 6 | communication avec des services | ⏳ |
| 7 | programmation objet en langage dynamique | ⏳ |
| 8 | automatisation avec python | ⏳ |
| 9 | qualité logicielle | ⏳ |

---

## chapitre 0 — le cadre du module

### ce que ce cours n'est pas

le cours part du principe qu'on sait déjà programmer. il n'est **pas** fait pour :

- apprendre les bases de l'algorithmique ou de la programmation ;
- découvrir la programmation orientée objet ;
- apprendre la syntaxe de python.

python, c'est juste le support.

### ce que ce cours est

trois objectifs :

1. découvrir les spécificités d'un **langage interprété moderne** et de son **écosystème** ;
2. savoir **organiser un projet logiciel** ;
3. prendre les réflexes de l'**ingénierie logicielle** et des **environnements devops**.

> **l'analogie.** tu sais déjà cuisiner. ce cours ne t'apprend pas à faire une omelette : il t'apprend à tenir la cuisine d'un restaurant. ranger, étiqueter, écrire des recettes que n'importe quel cuisinier peut refaire à l'identique, et livrer sans surprise.

autrement dit : pas « écrire une boucle », mais « livrer un projet python propre, que quelqu'un d'autre peut installer et lancer sur sa machine ».

### organisation et notes

- 10 séances de cours et 6 séances de projet, de 2 h chacune ;
- note finale : **30 %** tp et projet, **30 %** épreuve intermédiaire, **40 %** épreuve finale ;
- le module se termine par un projet en groupe de 4 (l'outil en ligne de commande « vélo »).

> la slide d'intro annonce 8 séquences, avec « 08 qualité logicielle ». en réalité, le cours en compte 9 : le chapitre 8 est l'automatisation, et la qualité logicielle passe au chapitre 9.

---

## chapitre 1 — langages interprétés et écosystèmes modernes

### 1. de la machine jusqu'à python

un processeur ne comprend qu'une seule langue : le **langage machine**, des suites de 0 et de 1 propres à son architecture. personne n'écrit ça à la main. tous les langages sont des couches posées par-dessus, du plus bas niveau au plus haut :

```text
langage machine  →  assembleur  →  langages compilés  →  langages interprétés
   (binaire)        (x86, mips)        (c, c++)          (python, javascript)
   bas niveau                                                   haut niveau
```

plus on monte, plus c'est lisible pour un humain ; plus on descend, plus on est collé au matériel. l'assembleur, c'est le langage machine écrit avec des mots au lieu de chiffres : il dépend donc du processeur (x86 pour les pc, mips pour d'autres puces).

> **l'analogie.** pense à un immeuble. au sous-sol, les machines parlent en 0 et 1. plus tu montes, plus les étages sont confortables pour les humains. python est au dernier étage.

c et python sont tous les deux de haut niveau. ce qui les distingue, c'est **comment le code finit par tourner sur le processeur**.

### 2. la compilation

deux temps bien séparés : d'abord on compile, ensuite on exécute.

```bash
gcc hello.c -o hello   # 1. compilation : un fichier binaire "hello" est créé
./hello                # 2. exécution : on lance directement le binaire
```

le compilateur lit **tout** le code d'un coup, avant que quoi que ce soit ne tourne. il fait trois choses :

1. il **traduit** le code en langage machine ;
2. il **vérifie certaines erreurs** (syntaxe, typage…) ;
3. il **optimise** le code pour la machine visée.

une fois le binaire produit, on n'a plus besoin du compilateur pour le lancer.

> **l'analogie.** c'est la traduction d'un livre. le traducteur traduit tout le roman avant la publication, corrige les fautes au passage, et on imprime la version traduite. le lecteur lit directement la traduction, vite, sans attendre personne.

### 3. l'interprétation

une seule commande, et aucun binaire n'est créé :

```bash
python hello.py
```

l'**interpréteur** lit le code et l'exécute au fur et à mesure :

- la traduction se fait **en temps réel**, pendant l'exécution ;
- les erreurs sont découvertes **à l'exécution**, au moment où l'interpréteur tombe sur la ligne fautive.

c'est pour ça qu'un script python peut tourner dix minutes puis planter sur une faute de frappe à la ligne 300. en c, la même faute aurait bloqué la compilation : le programme n'aurait jamais démarré.

> **l'analogie.** c'est l'interprète d'une conférence, qui traduit phrase par phrase pendant que l'orateur parle. ça marche partout et tout de suite, mais c'est plus lent. et si l'orateur dit une phrase incompréhensible, l'interprète ne s'en rend compte qu'au moment où elle arrive.

### 4. compilé contre interprété : le tableau à savoir par cœur

| critère | compilation | interprétation |
|---|---|---|
| **traduction** | tout le code, en une fois, avant l'exécution | ligne par ligne, au lancement |
| **vitesse** | très rapide : le binaire est optimisé pour le processeur | plus lente : on traduit en même temps qu'on exécute |
| **erreurs** | détectées à la compilation (elles bloquent la création du binaire) | détectées à l'exécution (le programme s'arrête sur la ligne fautive) |
| **portabilité** | faible : le binaire dépend de l'os et de l'architecture | élevée : le même code tourne partout, **si l'interpréteur est installé** |
| **cycle de dev** | plus lent : modifier → recompiler → relancer | plus rapide : on modifie et on teste tout de suite |

**pourquoi le compilé va plus vite ?** pas parce qu'il est « plus proche » de la machine : le binaire **est** du langage machine. toute la traduction a été faite une fois pour toutes, avant l'exécution, et optimisée pour le processeur. en interprété, ce travail de traduction se refait pendant l'exécution, et c'est lui qui coûte du temps.

**le piège de la portabilité.** ce qui n'est pas portable en compilé, c'est le **binaire** : un `.exe` compilé sous windows ne tourne pas sous linux. pour le faire tourner ailleurs, il faut récupérer le **code source** (`.c`) et le recompiler sur la nouvelle machine. le `.exe` lui-même ne se recompile pas.

### 5. python : en vrai, un peu des deux

on range python dans les langages interprétés, mais `python hello.py` cache deux étapes :

```text
code source  →  compilateur (cpython)  →  code intermédiaire  →  interpréteur (pvm)  →  exécution
  (.py)                                       (bytecode)
```

1. **cpython** (l'implémentation officielle de python, écrite en c) **compile** le code source en **code intermédiaire**, aussi appelé **bytecode**. ce n'est pas du langage machine : ce sont des instructions simples, faites pour une machine qui n'existe pas physiquement ;
2. la **pvm** (python virtual machine) est l'**interpréteur** : elle lit le bytecode instruction par instruction et le fait exécuter par le vrai processeur. elle ne fabrique aucun fichier en code machine.

pourquoi ce détour ? parce que le bytecode est bien plus rapide à interpréter que du texte brut, et qu'il est **identique sur toutes les machines**.

> **l'analogie.** le bytecode, c'est une partition de musique. la même partition se joue partout dans le monde : il suffit d'un musicien sur place (la pvm) pour la jouer sur l'instrument local (le processeur). le code machine, lui, c'est un enregistrement fait pour un seul lecteur bien précis.

**à voir dans tes projets :** les dossiers `__pycache__` contiennent des fichiers `.pyc`, c'est-à-dire le bytecode de tes modules mis en cache. au lancement suivant, si le fichier n'a pas changé, python saute l'étape de compilation.

les trois formes d'un programme :

| | code source | code machine | code intermédiaire |
|---|---|---|---|
| **s'adresse à** | l'humain | le processeur | la pvm |
| **lisible** | oui | non | ? (pas fait pour être lu, sans être du binaire) |
| **portable** | oui | non | oui |
| **prêt pour l'exécution** | non | oui | oui |

le code intermédiaire cumule le meilleur des deux : **portable** comme le code source, et **prêt pour l'exécution** comme le code machine. il est portable parce qu'il ne vise aucun processeur : il vise la pvm, et une pvm existe pour chaque système (windows, linux, mac, arm, x86…).

### 6. l'écosystème

un langage moderne ne se résume pas à sa syntaxe. sa force, c'est tout ce qui existe autour : l'**écosystème**. il repose sur trois piliers :

| pilier | définition | pour python |
|---|---|---|
| **bibliothèques tierces** | du code écrit par d'autres, réutilisable par tout le monde | numpy, requests, pillow… |
| **dépôts centralisés** | l'endroit où ces bibliothèques sont stockées | **pypi** (python package index) |
| **outils** | tout ce qui facilite le travail des développeurs | pip, uv… |

> **l'analogie.** c'est l'app store de ton téléphone. les apps, ce sont les bibliothèques tierces ; l'app store, c'est le dépôt centralisé (pypi) ; et le bouton « installer », c'est l'outil (pip).

l'écosystème se voit aussi en trois couches, de ton code vers l'extérieur :

1. **le code du développeur** : tes propres fichiers `.py` ;
2. **la bibliothèque standard** : les modules livrés avec python. rien à installer, un `import` suffit : `math`, `os`, `sys`, `datetime`, `json`, `random`, `string`, `argparse`… ;
3. **les bibliothèques tierces** : faites par la communauté, à installer avant de les importer : `numpy`, `pandas`, `matplotlib`, `requests`, `pillow`, `qrcode`…

> **l'analogie.** ta cuisine : ce que tu cuisines (ton code), le placard de base livré avec la maison (la bibliothèque standard), et ce que tu dois acheter au supermarché avant de t'en servir (les bibliothèques tierces).

**le réflexe pour classer une bibliothèque :** faut-il un `pip install` avant de l'importer ? si oui, elle est tierce. sinon, elle est standard.

### 7. le gestionnaire de paquets : pip

le gestionnaire de paquets fait le lien entre ton projet et le dépôt. il sert à :

- **installer** des bibliothèques tierces ;
- **gérer les versions** et les **mettre à jour** ;
- **désinstaller** des bibliothèques.

le gestionnaire historique de python, c'est **pip** :

```bash
python --version                 # version de python
pip --version                    # version de pip
pip list                         # bibliothèques tierces installées dans l'environnement
pip install pillow               # installer depuis pypi
pip install --upgrade pillow     # mettre à jour
pip uninstall pillow             # désinstaller
pip freeze > requirements.txt    # exporter les bibliothèques installées, avec leurs versions
pip install -r requirements.txt  # tout réinstaller à partir du fichier
```

**pourquoi `json` ou `os` n'apparaissent pas dans `pip list` ?** parce que `pip list` n'affiche que les bibliothèques **tierces** installées. les modules standard font partie de python lui-même.

**`ModuleNotFoundError: No module named 'numpy'`** veut dire que la bibliothèque n'est pas installée dans l'environnement utilisé. la solution : `pip install numpy`, puis relancer.

### 8. le fichier requirements.txt

dans un projet, il faut lister les bibliothèques tierces nécessaires **et leurs versions exactes**, pour garantir la **reproductibilité** : un autre développeur doit pouvoir recréer exactement le même environnement que toi.

```text
matplotlib==3.11.2
pillow==12.3.0
qrcode==8.2
```

> **l'analogie.** une liste de courses précise : pas « du lait », mais « lait demi-écrémé, telle marque, 1 litre ». celui qui fait les courses à ta place revient avec exactement les mêmes produits.

- `pip freeze` liste ce qui est installé, au format `nom==version` ;
- le `>` est une **redirection** du terminal : au lieu d'afficher le résultat à l'écran, il l'écrit dans le fichier. si le fichier existe déjà, il est **écrasé** (`>>` ajouterait à la fin) ;
- attention : `pip freeze` liste **tout**, y compris les bibliothèques installées par tes bibliothèques (`matplotlib` amène `numpy`) et, si tu utilises le python global de ta machine, celles de tes autres projets. c'est ce problème que règlent les environnements virtuels (chapitre 4).

### 9. lire une documentation

utiliser une bibliothèque tierce, c'est d'abord savoir lire sa documentation.

**où la trouver :**

- sur le **dépôt centralisé** (la page pypi de la bibliothèque) ;
- sur le **site dédié** (pillow.readthedocs.io, matplotlib.org…) ;
- sur le **dépôt github** du projet ;
- dans le **code source** lui-même.

**les quatre types de documentation :**

| type | ce qu'on y trouve |
|---|---|
| **readme** | la présentation du projet, comment l'installer, un premier exemple |
| **documentation officielle (api reference)** | la description complète de chaque fonction, classe et paramètre |
| **guides / tutoriels** | des pas-à-pas vers un objectif (le « quick start guide » de matplotlib, par exemple) |
| **docstrings** | la documentation écrite directement dans le code |

> **l'analogie.** un meuble ikea : le readme, c'est l'étiquette sur le carton ; l'api reference, la liste exhaustive des pièces ; le tutoriel, la notice de montage pas à pas ; et la docstring, la petite étiquette collée directement sur chaque pièce.

une **docstring** est une chaîne entre triples guillemets placée juste sous la ligne `def` (ou `class`). python la garde en mémoire, et on l'affiche avec `help()` :

```python
def celsius_vers_fahrenheit(c):
    """Convertit une température de degrés Celsius en degrés Fahrenheit."""
    return (c * 9 / 5) + 32

help(celsius_vers_fahrenheit)   # affiche la docstring
```

### 10. pillow et le recadrage d'image

**le nom d'installation n'est pas toujours le nom d'import :** on installe `pillow`, mais on écrit `from PIL import Image`. même chose avec `pyyaml`, qui s'importe en `yaml`.

**le repère de pillow :** l'origine `(0, 0)` est **en haut à gauche** de l'image. x augmente vers la droite, y augmente **vers le bas** (l'inverse des maths).

**`crop((gauche, haut, droite, bas))` :** les quatre nombres sont des **coordonnées**, pas une largeur et une hauteur. ce sont deux coins du rectangle qu'on garde :

- `(gauche, haut)` : le coin en haut à gauche ;
- `(droite, bas)` : le coin en bas à droite.

> **l'analogie.** pour découper une photo, tu ne dis pas « coupe 300 de large » : tu poses le doigt sur le coin en haut à gauche de la zone, puis sur le coin en bas à droite.

exemple sur une image de 800 × 600 (800 de large, 600 de haut) :

```text
(0,0) ─────────────────────── (800,0)
  │         moitié haute         │
(0,300) ───────────────────── (800,300)
  │         moitié basse         │
(0,600) ───────────────────── (800,600)
```

```python
from PIL import Image

image = Image.open("photo.png")
print(image.size)                          # (800, 600) : (largeur, hauteur)

haut = image.crop((0, 0, 800, 300))        # moitié haute
bas = image.crop((0, 300, 800, 600))       # moitié basse
bas.save("photo_bas.png")
```

**pour vérifier :** la taille du résultat vaut `(droite - gauche, bas - haut)`. ici, (800, 300).

### à retenir du chapitre 1

- **compilé** : tout traduit avant l'exécution, rapide, erreurs à la compilation, binaire peu portable, cycle lent ;
- **interprété** : traduit ligne par ligne au lancement, plus lent, erreurs à l'exécution, portable si l'interpréteur est là, cycle rapide ;
- **python** : code source → compilateur cpython → bytecode → interpréteur pvm → exécution ;
- **écosystème** : 3 piliers (bibliothèques tierces, dépôts centralisés, outils) et 3 couches (ton code, bibliothèque standard, bibliothèques tierces) ;
- **gestionnaire de paquets** : installer, gérer les versions et mettre à jour, désinstaller ;
- **requirements.txt** : bibliothèques et versions exactes, pour la reproductibilité ;
- **documentation** : 4 endroits (dépôt, site dédié, github, code source) et 4 types (readme, api reference, guides, docstrings) ;
- **pillow** : origine en haut à gauche, `crop((gauche, haut, droite, bas))` avec deux coins.

### pièges classiques en qcm

- le bytecode s'adresse à la **pvm**, pas au processeur ;
- dans le schéma du cours, cpython est le **compilateur** et la pvm l'**interpréteur** ;
- « python ne fait aucune compilation » est **faux** ;
- il n'y a **pas** de fichier en code machine produit entre la pvm et l'exécution ;
- la portabilité élevée de l'interprété suppose que **l'interpréteur soit installé** ;
- ce qui n'est pas portable en compilé, c'est le **binaire**, pas le code source ;
- le compilateur n'est plus nécessaire pour lancer un binaire déjà produit ;
- `pip freeze` ne « gèle » et ne bloque rien : il **liste** les bibliothèques et leurs versions ;
- `crop` prend des **coordonnées**, pas une largeur et une hauteur.