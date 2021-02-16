<?php

/*Création des identifiants d'accès à la partie propriétaire*/
    $username = "FRS";
    $password = "Caroita";
 
    /*On regarde si les identifiants rentrés par l'utilisateur existent*/
    if( isset($_POST['username']) && isset($_POST['password']) ){
           
        /*Si ils existent, on regarde si ils correspondent aux identifiants d'accès créés plus haut et on redirige l'utilisateur sur la partie propriétaire*/
        if($_POST['username'] == $username && $_POST['password'] == $password){
            header('Location: IHM_Page_Proprietaire.php');
        }
        else{
        /*Si ils sont incorrects, on garde l'utilisateur sur cette page et on envoit une alerte qui indique qu'au moins un des deux champs est incorrects*/
?>  

            <script type="text/javascript">
                alert("Identifiant ou mot de passe incorrect");
                document.location = "IHM_Mot_De_Passe.php";
            </script>        
<?php
        }
    }
?>


