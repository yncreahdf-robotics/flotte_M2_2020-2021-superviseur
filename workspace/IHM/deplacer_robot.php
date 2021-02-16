<?php
	$Robot = $_POST["Robot"];
	$Position = $_POST["Position"];
	$command = "python3 CommandeRobot.py ".$Robot." ".$Position;
	shell_exec($command);
	#echo $output;
    
	header('Location: IHM_Deplacer_Robot.php');
?>
