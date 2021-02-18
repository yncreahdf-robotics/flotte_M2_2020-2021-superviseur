<?php
/*Page affichant le contenu du panier du client avant l'envoie de la commande. Si le client ne veut plus modifier son panier, il peut envoyer la commande avec le bouton de validation qui va appeler envoie_commande.php*/

	/*On démarre une session pour utiliser un panier associé au client*/
	session_start();	

	/*On récupère les fonctions de gestion du panier depuis le fichier fonctions_panier.php*/
	include_once("fonctions_panier.php");

	/*On vérifie que le panier est bien créer*/
	creationPanier();

?>

<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<link rel="stylesheet" href="IHM.css" />
		<title>Commande client en cours</title>
	</head>

	<body>
		<div id="bloc_page">
			
			<!-- Affichage de l'entete de la page avec le fichier entete.php -->
			<?php include("entete.php"); ?>
		
			<!-- Affichage du panier -->
			<section>
				<h2>Commande en cours</h2>
				<h2><br />Liste des articles sélectionnés :</h2>
				<?php
					for($i = 0; $i < count($_SESSION['panier']['nom_produit']); $i++){
						echo $_SESSION['panier']['nom_produit'][$i] . " - Quantité : " . $_SESSION['panier']['quantite_produit'][$i] . " - Prix unitaire : " . $_SESSION['panier']['prix_produit'][$i] . "€<br />";
					}

					/*On calcule le montant total du panier*/
					$_SESSION['panier']['montant_panier'] = montantTotal();
				?>
				<p>
					Table : <?php echo $_SESSION['panier']['table'] ?><br />
					Prix total : <?php echo $_SESSION['panier']['montant_panier'] ?>€
				</p>
				<nav>
					<div class="bouton" id="valider">
						<p>Valider la commande</p>
					</div>
					<div class="bouton" id="appel_serveur">
						<h3>Appeler un serveur</h3>
					</div>
				</nav>
			</section>

			<!-- Affichage du pied de page avec le fichier pied_de_page.php -->
			<?php include("pied_de_page.php"); ?>
			
		</div>

		<!-- Fonctions qui permettent de gérer les boutons présents sur la page -->
		<script src="//code.jquery.com/jquery-1.12.0.min.js"></script>
		<script type="text/javascript">
			//Validation de la commande
			const elt_valider = document.getElementById('valider');
			elt_valider.addEventListener('click', function valider_commande(event) {
				if(confirm("Valider la commande ?")){
					alert("Commande envoyée.")
					document.location = "envoie_commande.php";
				}
				else{
					
				}
			})

			//Appel d'un serveur
			const elt = document.getElementById('appel_serveur');
			elt.addEventListener('click', function appel_serveur(event) {
				if(confirm("Etes-vous sur de vouloir appeler un serveur ?")){
					alert("Un serveur a été appelé.")
				}
				else{
					
				}
			})

			//Bouton de retour
			const elt_retour = document.getElementById('Retour');
			elt_retour.addEventListener('click', function client(event){
				document.location = "IHM_Page_Client.php";
			})
		</script>
	</body>
</html>