<?php


//Connexion BDD profil IHM depuis pc perso
	try{
		$bdd = new PDO('mysql:host=192.168.1.5;dbname=flotte_db', 'ihm', 'password', array(PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION));
	}
	catch(Exception $e){
		die('Erreur : '.$e->getMessage());
	}


//Connexion BDD profil root depuis pc Superviseur
	/*try{
		$bdd = new PDO('mysql:host=172.19.0.3;dbname=flotte_db', 'root', 'root', array(PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION));
	}
	catch(Exception $e){
		die('Erreur : '.$e->getMessage());
	}*/


?>