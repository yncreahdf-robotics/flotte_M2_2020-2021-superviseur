#Dossier envoi ordres (superviseur vers robot)

## Comment envoyer un ordre de déplacement du superviseur vers le robot ?

Placer le fichier heronReception sur le bureau d'un robot.
Ajouter le fichier bash superviseur.sh au même endroit.

#Dossier réception données (robots vers superviseur)

## Comment lire les données de batterie du robot vers le superviseur ?

Placer le fichier heronEnvoi sur le bureau de ce même robot.
Mettre le fichier superviseurReception sur le bureau du superviseur.

#Dossier services

## Comment faire démarrer automatiquement tous ces scripts (et roscore) au boot de chaque robot ?

Mettre tous les fichiers services dans le chemin /etc/systemd/system sauf le fichier roscoreservice.sh.
Placer ce dernier fichier dans /usr/local/bin.
