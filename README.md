# Guess The Day

En fonction d'une date donnée, il est possible de trouver le jour de la semaine correspondant.
Cela peut paraitre compliqué à première vu mais c'est seulement une question d'entrainement. 

Le but de ce script est de permettre à l'utilisateur de s'entrainer à calculer le jour grâce à des génération de date au hasard.

## Principe du calcul

Pour calculer une date un des méthodes consiste à connaitre la liste des premiers lundi de chaque mois.
Cette liste peut être organisée par paquet de 3 pour faciliter la mémorisation. 

*Exemple pour 2021 :* **411 537 526 416**

Il suffit alors de :
- Cherche à l'indice du mois correspondant le jour **N** du premier Lundi.
- Rajouter +7 autant de fois que nécessaire pour trouver la date du Lundi le plus proche du jour voulu.
- Ajuster en faisant +1 ou -1 pour trouver le jour.

## Usage

Pour lancer le programme une fois télécharger 
(Les paramètres sont optionnels)
```
trainer.py [ITERATION] [DIFFICULTE] [INTERVALLE]
```

## Paramètres
- **ITERATION** : Nombre d'itération du programme.
- **DIFFICULTE** : Change le fonctionnement du programme en fonction du paramètre (0,1 ou 2).
- **INTERVALLE** : Le programme prendra une année aléatoire dans l'intervalle [ACTUELLE - INTERVALLE; ACTUELLE] 

## Difficultés 
- **Mode 0** : Affiche la liste des premiers lundi de chaque mois.
- **Mode 1** : N'affiche aucune indication.
- **Mode 2** : Change le format d'affichage en remplaçant le chiffre par le nom du mois.
