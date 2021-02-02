<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Connexion</title>
    </head>
    <body>
        <?php
            $username = "FRS";
            $password = "Caroita";
 
            if( isset($_POST['username']) && isset($_POST['password']) ){                   //Test si les identifiants existent
         
                if($_POST['username'] == $username && $_POST['password'] == $password){     //Test si les identifiants correspondent
                     header('Location: IHM_Page_Proprietaire.php');
                }
                else{

        ?>
                    <script type="text/javascript">
                        alert("Identifiant ou mot de passe incorrect");
                        document.location = "IHM_Mot_De_Passe.php";
                    </script>
        
        <?php
                }
            }
        ?>
    </body>
</html>