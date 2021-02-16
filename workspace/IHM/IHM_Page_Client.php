<?php 
	session_start();	//On démarre une session pour utiliser un panier associé au client
	//include_once("fonctions-panier.php");

	$_SESSION['panier'] = array();
	$_SESSION['panier']['table'] = NULL;
	$_SESSION['panier']['nom_produit'] = array();
	$_SESSION['panier']['quantité_produit'] = array();
	$_SESSION['panier']['prix_produit'] = array();
?>

<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<link rel="stylesheet" href="IHM.css" />
		<title>Accueil Client</title>
	</head>

	<body>
		<?php
			
			/*Connexion à la base de données avec le fichier connexion.php*/
			include("connexion.php");
			
			/*Création de la requète qui va récupérer les informations des tables dans Table_tb*/
			$requete_commande = $bdd->query('SELECT * FROM Commande_tb');

			/*Création de la requète qui va récupérer les informations des articles dans Article_tb*/
			$requete_article = $bdd->query('
				SELECT ArticleID, ArticleName, ArticlePrice 
				FROM Article_tb
			');	
		?>

		<div id="bloc_page">
			
			<!-- Affichage de l'entete de la page avec le fichier entete.php -->
			<?php include("entete.php"); ?>
		
			<section>
				<h2>Menu Client</h2>

				<form action="" method="post">
					<!-- Formulaire qui permet au client d'indiquer la table à laquelle il se trouve et de saisir les articles qu'il veut commander -->
					<h3>Merci d'indiquer le numéro de la table où vous êtes assis</h3>
					<input type="radio" name="Choix_table" value="table1" /><label class="label-radio">Table 1</label>
					<br />
					<input type="radio" name="Choix_table" value="table2" /><label class="label-radio">Table 2</label>
					<br />
					<input type="radio" name="Choix_table" value="table3" /><label class="label-radio">Table 3</label>
					<br />
					<br />
		        	
					<h2>Liste des articles :</h2>
					
					<ul>
						<?php
						/*On récupère les informations depuis requete_article et on les affiches dans une liste. Chaque article va créer une entrée dans la liste. Cette liste permet au client d'indiquer combien de quantité de chaque article il veut commander*/
							while($donnees = $requete_article->fetch()){
						?>
							<li>
								<?php echo $donnees['ArticleName'];?> - Quantité : <input type="number" step="1" value="0" min="0" max="8"> - Prix unitaire : <?php echo $donnees['ArticlePrice'];?> €
							</li>
							<br />
						<?php
							}
						?>
					</ul>
				</form>
				<p>
					 Prix total : €
				</p>

				<!-- Création de boutons permettant de pré-valider la commande ou d'appeler un serveur -->
				<nav>
					<div class="bouton" id="commande">
						<p>Commander</p>
					</div>
					<div class="bouton" id="appel_serveur">
						<p>Appeler un serveur</p>
					</div>
				</nav>
			</section>

			<!-- Affichage du pied de page avec le fichier pied_de_pahe.php-->
			<?php include("pied_de_page.php"); ?>

		<!-- Fonctions qui permettent de gérer les boutons présents sur la page -->
		<script src="//code.jquery.com/jquery-1.12.0.min.js"></script>
		<script type="text/javascript">
			//Bouton pour pré-valider la commande
			const elt_commande = document.getElementById('commande');
			elt_commande.addEventListener('click', function commande(event){
				//event.preventDefault()
				document.location = "IHM_Commande_Client.php";
			})

			//Appel d'un serveur
			const elt_serveur = document.getElementById('appel_serveur');
			elt_serveur.addEventListener('click', function appel_serveur(event) {
				//event.preventDefault()
				if(confirm("Etes-vous sur de vouloir appeler un serveur ?")){
					alert("Un serveur a été appelé.")
				}
				else{
					
				}
			})

			//Bouton de retour
			const elt_retour = document.getElementById('Retour');
			elt_retour.addEventListener('click', function client(event){
				//event.preventDefault()
				document.location = "index.php";
			})
		</script>
	</body>
</html>