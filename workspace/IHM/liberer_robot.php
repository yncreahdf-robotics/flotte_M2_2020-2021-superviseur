<?php
/*Fonction qui permet de libérer le robot sélectionné*/
	$robot_liberer = $_POST["robot_liberer"];

	/*Connexion à la base de données avec le fichier connexion.php*/
	include("connexion.php");

	/*Création de la requète qui va libérer le robot*/
	$requete = $bdd->prepare('
		UPDATE Robot_tb
		SET Etat = \'Idle\', ActiveCommandNbr = 0
		WHERE RobotIP = :robot_liberer
	');
	/*On associe les variables de la requète avec les variables récupérées du formulaire*/
	$requete->execute(array(
		'robot_liberer' => $robot_liberer
	));

	/*On renvoit l'utilisateur sur la page IHM_Liste_Robots.php*/
	header('Location: IHM_Liste_Robots.php');
?>