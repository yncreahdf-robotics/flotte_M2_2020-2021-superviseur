<?php
	/*Page qui permet de déplacer un robot à une position enregistrée en le sélectionnant et en choisissant sa position d'arrivée avec le formulaire. Ce formulaire va appeler deplacer_robot.php pour envoyer l'ordre au robot*/
?>

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
				/*Connexion à la base de données avec le fichier connexion.php*/
				include("connexion.php");


				$requete = $bdd->query('SELECT r.RobotIP, r.RobotType, r.Position, r.Etat, t.Role
					FROM Robot_tb r	/*Lecture table Robot depuis la bdd*/
					INNER JOIN Type_tb t
					ON r.RobotType = t.TypeName
				');
				$position = $bdd->query('SELECT PoseName FROM Pose_tb');
			?>
			
			<!-- Affichage de l'entete de la page avecle fichier entete.php -->
			<?php include("entete.php"); ?>
		
			<section>
				<h2>Choisir le robot à deplacer parmi les robots disponible</h2>
				<!-- Formulaire qui permet de choisir le robot à déplacer et la position d'arrivée -->
				<form method="post" action="deplacer_robot.php">
   					<p>
   						<?php
   						/*On affiche les robots mobiles qui sont libres*/
   							//Robot libre -> Etat = Idle
   							while($donnees = $requete->fetch()){
   								if($donnees['Role'] == 'Service' || $donnees['Role'] == 'Guide'){
   									echo "<input type=\"radio\" name=\"Robot\" value=\"".$donnees['RobotIP']."\" id=\"".$donnees['RobotIP']."\"/>
   									<label for=\"".$donnees['RobotIP']."\">IP : ".$donnees['RobotIP']." - Type : ".$donnees['RobotType']."</label>";
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
   					
   						<?php
   						/*On affiche les différentes positions enregistrées dans la base de données*/
   							while($donnees = $position->fetch()){		
   								echo "<input type=\"radio\" name=\"Position\" value=\"".$donnees['PoseName']."\" id=\"".$donnees['PoseName']."\"/>
   								<label for=\"".$donnees['PoseName']."\">".$donnees['PoseName']."</label>";
   						?>
       					<br />
       					<br />
       					<?php
       						}
       					?>
   					
   					<br />

   					<input type="submit" name="Deplacer" value="Deplacer" id="Deplacer" />

   					<br />
				</form>
			</section>

			<!-- Affichage du pied de page avec le fichier pied_de_page.php -->
			<?php include("pied_de_page.php"); ?>
		</div>

		<!-- Fonctions qui permettent de gérer les boutons présents sur la page -->

		<script src="http://code.jquery.com/jquery-3.3.1.min.js" integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8=" crossorigin="anonymous"></script>

		<script type="text/javascript">
			//Bouton de retour
			const elt_retour = document.getElementById('Retour');
			elt_retour.addEventListener('click', function retour(event){
				document.location = "IHM_Page_Proprietaire.php";
			})
		
	        function goPython(){
	            $.ajax({
	              url: "CommandeRobot.py",
	             context: document.body
	            }).done(function() {
	             alert('finished python script');;
	            });
	        }
	    
		</script>
	</body>
</html>