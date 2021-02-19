<?php
/*Fonction php appelée à chaque connexion vers la base de données, on test la connexion avec différents profils*/

/*Connexion BDD profil ihm depuis pc perso, si ne fonctionne pas, test la connexion depuis pc Superviseur*/
	try{
		$bdd = new PDO('mysql:host=192.168.1.5;dbname=flotte_db', 'ihm', 'password', array(PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION));
	}
	catch(Exception $e){
		try{
		$bdd = new PDO('mysql:host=172.19.0.3;dbname=flotte_db', 'root', 'root', array(PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION));
	}
		catch(Exception $e){
			die('Erreur : '.$e->getMessage());
		}
	}

?>
