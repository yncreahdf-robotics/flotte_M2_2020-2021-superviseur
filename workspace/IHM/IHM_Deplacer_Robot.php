<!DOCTYPE html>		
<html>
	<head>
		<meta charset="utf-8" />
		<link rel="stylesheet" href="IHM.css" />
		<title>Deplacer un robot</title>
	</head>

	<body>
		<div id="bloc_page">
			<?php
				try{
					$bdd = new PDO('mysql:host=172.19.0.3;dbname=flotte_db', 'root', 'root', array(PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION));
				}
				catch(Exception $e){
					die('Erreur : '.$e->getMessage());
				}
				$requete = $bdd->query('SELECT r.RobotIP, r.RobotType, r.Position, r.Etat, t.Role
				FROM Robot_tb r	/*Lecture table Robot depuis la bdd*/
				INNER JOIN Type_tb t
				ON r.RobotType = t.TypeName');
				$position = $bdd->query('SELECT PoseName FROM Pose_tb');
			?>
			
			<?php include("entete.php"); ?>
		
			<section>
				<h2>Choisir le robot à deplacer parmi les robots disponible</h2>
				<form method="post" action="deplacer_robot.php">
   					<p>
   						<?php
   							//Robot libre -> Etat = Idle
   							while($donnees = $requete->fetch()){
   								if($donnees['Role'] == 'Service'){
   									echo "<input type=\"radio\" name=\"Robot\" value=\"".$donnees['RobotIP']."\" id=\"".$donnees['RobotIP']."\"/><label for=\"".$donnees['RobotIP']."\">IP : ".$donnees['RobotIP']." - Type : ".$donnees['RobotType']."</label>" ;
   						?>
       					<br />
       					<br />
       					<?php
       							}	
       						}
       					?>
   					</p>
				
					<br />

					<h2>Choisir la position d'arrivée du robot</h2>
   					<p>
   						<?php
   							//Robot libre -> Etat = Idle
   							while($donnees = $position->fetch()){		
   								echo "<input type=\"radio\" name=\"Position\" value=\"".$donnees['PoseName']."\" id=\"".$donnees['PoseName']."\"/><label for=\"".$donnees['PoseName']."\">".$donnees['PoseName']."</label>";
   						?>
       					<br />
       					<br />
       					<?php
       						}
       					?>
   					</p>
				</form>
				<p><br /><input type="submit" name="Deplacer" value="Deplacer" id="Deplacer" /><br /></p>
			</section>

			<?php include("pied_de_page.php"); ?>
		</div>
		<script src="//code.jquery.com/jquery-1.12.0.min.js"></script>
		<script type="text/javascript">
			//Bouton de retour
			const elt_retour = document.getElementById('Retour');
			elt_retour.addEventListener('click', function retour(event){
				event.preventDefault()
				document.location = "IHM_Page_Proprietaire.php";
			})
		</script>
	</body>
</html>