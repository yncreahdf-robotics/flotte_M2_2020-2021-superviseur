<?php
/*Fonction php appelée par le formulaire de déplacement de robot de la page IHM_Deplacer_Robot.php, elle permet de déplacer le robot sélectionné depuis le formulaire à une position enregistrée*/

	/*Récupération des données envoyées par le formulaire pour choisir le robot et la position d'arrivée*/
	$Robot = $_POST["Robot"];
	$Position = $_POST["Position"];

	/*Appel du fichier python qui va gérer le déplacement du robot*/
	$command = "python3 CommandeRobot.py ".$Robot." ".$Position;
	shell_exec($command);
	#echo $output;
    
    /*On renvoit l'utilisateur sur la page IHM_Deplacer_Robot.php*/
	header('Location: IHM_Deplacer_Robot.php');
?>
