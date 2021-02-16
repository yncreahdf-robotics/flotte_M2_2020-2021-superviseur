<?php

	/*Récupération des données envoyées par le formulaire d'ajout de type de robot*/
	$type_robot = $_POST["type_robot"];
	$role = $_POST["role"];
	$weight_capacity = $_POST["weight_capacity"];

	/*Connexion à la base de données avec le fichier connexion.php*/
	include("connexion.php");

	/*Création de la requète qui va ajouter le type de robot dans la table Type_tb, le premier champ prend la valeur de la première variable, le deuxième champ prend la valeur de la deuxième variable, etc...*/
	$requete = $bdd->prepare('INSERT INTO Type_tb(TypeName, Role, WeightCapacity) VALUES(:type_robot, :role, :weight_capacity)');

	/*On associe les variables de la requète avec les variables récupérées du formulaire*/
	$requete->execute(array(
		'type_robot' => $type_robot,
		'role' => $role,
		'weight_capacity' => $weight_capacity
	));

	/*On renvoit l'utilsateur sur la page IHM_Liste_Robots.php*/
	header('Location: IHM_Liste_Robots.php');
?>