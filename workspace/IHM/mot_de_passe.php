<<<<<<< HEAD
=======
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Connexion</title>
    </head>
    <body>
>>>>>>> 6d06d4ece447e73cdf7ebeb950d34a24066ce44b
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
<<<<<<< HEAD

?>
=======
?>  
>>>>>>> 6d06d4ece447e73cdf7ebeb950d34a24066ce44b
                    <script type="text/javascript">
                        alert("Identifiant ou mot de passe incorrect");
                        document.location = "IHM_Mot_De_Passe.php";
                    </script>
<<<<<<< HEAD
        
<?php
                }
            }
?>
=======
<?php
                }
            }
 ?>
    </body>
</html>
>>>>>>> 6d06d4ece447e73cdf7ebeb950d34a24066ce44b
