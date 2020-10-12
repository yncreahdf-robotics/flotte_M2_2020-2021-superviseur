*Lire la documentation technique pour plus de détails*

## Dossier envoi ordres (superviseur vers robot)

*Permet d'envoyer un ordre de déplacement (pour l'instant un carré) au robot*

Placer le fichier heronReception.py sur le bureau d'un robot (penser à mettre à jour le bon path)
Ajouter le fichier bash superviseur.sh au même endroit que le script python

*Lancer heronReception.py & superviseurEnvoi : Vous recevez bien l'ordre de déplacement du superviseur*

## Dossier réception données (robots vers superviseur)

*Permet de recevoir les données du robot (pour l'instant la batterie) sur le superviseur*

Placer le fichier heronEnvoi.py sur le bureau de ce même robot
Mettre le fichier superviseurReception.py sur le bureau du superviseur

*Lancer heronEnvoi.py & superviseurReception.py : Vous recevez bien les données du robot*

## Dossier services

*Permet de faire démarrer automatiquement tous ces scripts (et roscore) au boot de chaque robot*

Mettre tous les fichiers services dans le chemin /etc/systemd/system de votre système, sauf le fichier roscoreservice.sh
Placer ce dernier fichier dans /usr/local/bin
Activer les services grâces aux commandes suivantes pour chacun de vos services :

```
$ sudo systemctl daemon-reload
$ sudo systemctl enable <nomduservice>.service
$ sudo systemctl start <nomduservice>.service
```

Enfin, pour finir, faites un reboot : les services sont actifs.
