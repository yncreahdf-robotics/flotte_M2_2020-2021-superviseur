<?php
	$type_robot = $_POST["type_robot"];
	$role = $_POST["role"];
	$weight_capacity = $_POST["weight_capacity"];

	try{
		$bdd = new PDO('mysql:host=172.19.0.3;dbname=flotte_db', 'root', 'root', array(PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION));
	}
	catch(Exception $e){
		die('Erreur : '.$e->getMessage());
	}

	$requete = $bdd->prepare('INSERT INTO Type_tb(TypeName, Role, WeightCapacity) VALUES(:type_robot, :role, :weight_capacity)');
	$requete->execute(array(
		'type_robot' => $type_robot,
		'role' => $role,
		'weight_capacity' => $weight_capacity
	));

	header('Location: IHM_Liste_Robots.php');
?>