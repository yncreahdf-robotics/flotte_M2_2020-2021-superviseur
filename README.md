# Pour avoir le git en local sur son pc :

Se positionner ou on veut sur le pc :

`cd <Arborescence>`
  
Cloner le git :

`git clone https://github.com/yncreahdf-robotics/flotte_M2_2020-2021-superviseur`


# A lire avant d'uploader quelque chose :

## Avant de commencer une nouvelle fonctionnalité :

Se positionner dans le git sur le pc :

`cd <Arborescence>`

Recuperer les nouveaux fichiers du serveur sur son pc :

`git pull`

Se placer sur la branche develop :

`git checkout develop`

Créer une nouvelle branche feature avec le nom de votre fonctionnalité comme suit :

`git checkout -b feature/<NomDeLaFeature>`

Uploader la nouvelle branche sur le serveur en definissant son origine :

`git push --set-upstream origin feature/<NomDeLaFeature>`


## Pour Uploader des changements dans une branche :

Se positionner dans le git sur le pc :

`cd <Arborescence>`

Recuperer les nouveaux fichiers du serveur sur son pc :

`git pull`

Se placer sur sa branche de feature :

`git checkout develop`

Aller dans le repertoire de travail :

`cd workspace`

Si il y a des nouveaux fichiers, les ajouter :

`git add <NomDuFichier>`

Faire un commit avec un message :

`git commit -m "<MessageDeDescriptionDesChangements>"`

Push les changements :

`git push`
