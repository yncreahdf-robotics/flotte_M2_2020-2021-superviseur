<?php
	$type_robot = $_POST["type_robot"];
	$role = $_POST["role"];
	$weight_capacity = $_POST["weight_capacity"];

	
	include("connexion.php");


	$requete = $bdd->prepare('INSERT INTO Type_tb(TypeName, Role, WeightCapacity) VALUES(:type_robot, :role, :weight_capacity)');
	$requete->execute(array(
		'type_robot' => $type_robot,
		'role' => $role,
		'weight_capacity' => $weight_capacity
	));

	header('Location: IHM_Liste_Robots.php');
?>