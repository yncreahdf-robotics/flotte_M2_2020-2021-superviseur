DOSSIER ENVOI ORDRES (SUPERVISEUR VERS ROBOT)

Placer le fichier heronReception sur le bureau d'un robot.
Ajouter le fichier bash superviseur.sh au même endroit.

DOSSIER RECEPTION DONNEES (SUPERVISEUR VERS ROBOT)

Placer le fichier heronEnvoi sur le bureau de ce même robot.
Mettre le fichier superviseurReception sur le bureau du superviseur.

DOSSIER SERVICES

Mettre tous les fichiers services dans le chemin /etc/systemd/system sauf le fichier roscoreservice.sh.
Placer ce dernier fichier dans /usr/local/bin.
