<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<link rel="stylesheet" href="IHM.css" />
		<title>Supprimer un article</title>
		<script type="text/javascript">
			function aff_bouteille(action){
    			document.getElementById('block_bouteille').style.display = (action == "oui")? "inline" : "none";
			}
			function aff_boisson(action){
    			document.getElementById('block_boisson').style.display= (action == "oui")? "inline" : "none";
			}
		</script>
	</head>

	<body>
		<div id="bloc_page">
			
			<?php include("entete.php"); ?>
		
			<section>
				<div id="Choix_ajout">
					<h3>Que voulez vous supprimer ?</h3>
					<input type="radio" name="Choix_ajout" value="Bouteille" onchange="aff_bouteille('oui'); aff_boisson('non')" /><label class="label-radio">Une bouteille</label><br/>
		        	<input type="radio" name="Choix_ajout" value="Boisson" onchange="aff_bouteille('non'); aff_boisson('oui')" /><label class="label-radio">Une boisson</label><br/><br/>
				</div>
				<h3>Sélectionner l'article à supprimer</h3>

				<div id="block_bouteille" hidden="hidden">
					<select name="modif_bouteille" id="modif_bouteille">
						<option>Ice-Tea</option>
						<option>Eau</option>
	        			<option>Sirop de Fraise</option>
	        			<option>Sirop de Menthe</option>
	        			<option>Coca-Cola</option>
	        			<option>Limonade</option>
					</select>
				</div>

				<div id="block_boisson" hidden="hidden">
					<select name="modif_boisson" id="modif_boisson">
						<option>Ice Tea</option>
						<option>Eau</option>
						<option>Sirop de Menthe 12%</option>
						<option>Sirop de Menthe 25%</option>
						<option>Sirop de Fraise 12%</option>
						<option>Sirop de Fraise 25%</option>
						<option>Coca-Cola</option>
						<option>Limonade	</option>
					</select>
				</div>
				<br />
				<br />
				<nav>
					<input type="button" name="Supprimer" value="Supprimer" id="supprimer" />
				</nav>
			</section>

			<?php include("pied_de_page.php"); ?>

		</div>
		<script src="//code.jquery.com/jquery-1.12.0.min.js"></script>
		<script type="text/javascript">
			const elt = document.getElementById('supprimer');
			elt.addEventListener('click', function supprimer(event) {
				event.preventDefault()
				if(confirm("Etes-vous sur de vouloir supprimer cet article ?")){
					alert("L'article a été supprimé");
					document.location = "IHM_Liste_Articles.php";
				}
				else{
					
				}
			})

			//Bouton de retour
			const elt_retour = document.getElementById('Retour');
			elt_retour.addEventListener('click', function retour(event){
				event.preventDefault()
				document.location = "IHM_Liste_Articles.php";
			})
		</script>
	</body>
</html>