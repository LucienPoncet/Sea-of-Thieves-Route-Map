# Sea-of-Thieves-Route-Map

A quick exercice I made in my first attempt to use python, with just a single file to calculate the distance and travel time between two islands in the videogame Sea of Thieves.

## FR

En utilisant la carte du jeu vidéo Sea of Thieves, basée comme un échiquier avec des coordonnées de type A1 ou K8 (les lettres en abscisse, donc correspondant à la longitude d'est en ouest, et les nombres en ordonnées, donc correspondant à la latitude du nord au sud), j'ai souhaité calculer la distance et le temps de trajet entre différentes îles selon les trois bâteaux différents proposés dans le jeu. J'ai donc transformé la carte en repère orthonormé, me permettant grâce aux coordonnées des îles données sur internet de pouvoir seulement en précisant le nom de l'île de départ, celui de l'île d'arrivée, et le type de bateau, de pouvoir avoir un résultat immédiat d'une fourchette du temps de trajet dans le jeu (selon la trajectoire du vent dans les voiles), mais aussi la direction à prendre (selon l'angle dans le repère orthonormé), et une courte description de l'île d'arrivée (type de structure, région sur la carte, et autres types de la même structure dans la même région).
