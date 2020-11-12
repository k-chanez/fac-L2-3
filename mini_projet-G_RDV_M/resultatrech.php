
<?php session_start();?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="Assets/css/bootstrap.min.css">
    <link rel="stylesheet" type="text/css" href="style.css">
    <title>Résultats de votre recherche</title>
</head>
<body>
<?php
if (isset($_SESSION["inscr"]) and $_SESSION["inscr"]==true) {
    echo "<script>alert('On vous a envoyer un lien de confirmation à votre adresse e-mail.Vérifiez vos mails ')</script>";
    $_SESSION["inscr"]=null;}
?>
    <nav id="menu" class="navbar navbar-default navbar-fixed-top" role="navigation">
        <!-- Brand and toggle get grouped for better mobile display -->
        <div class="navbar-header">
            <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#monmenu">
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="index.php"><span class="glyphicon glyphicon-home"></span> RDV&SOINS</a>
        </div>
        <!-- Collect the nav links, forms, and other content for toggling -->
        <div id="monmenu"class="collapse navbar-collapse ">
            <ul class="nav navbar-nav navbar-right">
            <?php 

if (isset($_SESSION["authmed"])and $_SESSION["authmed"]==true) {
    echo ' <li><a href="comptemedecin.php"><span class="glyphicon glyphicon-user"></span> '.$_SESSION["username"] .'</a></li>';
 } else {
     if(isset($_SESSION["authpat"])and $_SESSION["authpat"]==true)
  echo '<li><a href="gerecompte.php"><span class="glyphicon glyphicon-user"></span> '.$_SESSION["username"] .'</a></li>';
  else{echo'<li><a href="inscription.php"><span class="glyphicon glyphicon-user"></span> Inscription</a></li>';
 } }
            if (isset($_SESSION["authmed"])and $_SESSION["authmed"]==true or (isset($_SESSION["authpat"])and $_SESSION["authpat"]==true)) {
               echo ' <li><a href="logout.php"><span class="glyphicon glyphicon-log-out"></span> Déconnexion</a></li>
                      <li><a href="contact.php"><span class="glyphicon glyphicon-envelope" aria-hidden="true" ></span>Contact </a></li>';
            } else {
             echo ' <li><a href="connexionpr.php"><span class="glyphicon glyphicon-log-in"></span> Connexion</a></li>
                    <li><a href="contact.php"><span class="glyphicon glyphicon-envelope" aria-hidden="true" ></span>Contact </a></li>';
            } 

            ?>
            
            </ul>
        </div>
    </nav><br><br><br><br>
    <nav class="navbar navbar-expand-md" role="navigation">
            <div class="collapse navbar-collapse navbar-ex1-collapse">
                
                <form class="navbar-form navbar-center " role="search" action="resultatrech.php" method="post">
                    <div class="form-group">
                        <input style="width: 500px;" name="rech" type="text" class="form-control" placeholder="Recherchez un médecin, une  Spécialité …">
                    </div>
                    <button type="submit" class="btn btn-default"><span class="glyphicon glyphicon glyphicon-search" aria-hidden="true"></span> Rechercher</button>
                </form>
            </div> 
        </nav>
    
<?php
$resultat="";
//traitement de la requette 
if(isset($_POST['rech']) && !empty($_POST['rech'])){
// si l'utilisateur a entré quelque chose , on traite sa requette 
//pour ne pas avoir des caractères bizzar
$rech= preg_replace("#[^a-zA-Z ?0-9]#i", "",$_POST['rech']) ;
$sql="SELECT usermedecin,specialite,adrcab  FROM medecin WHERE specialite LIKE ? OR usermedecin LIKE ?" ;
//se connecter a la base de données
include("connectbdd.php");
$req = $rdvsoins->prepare($sql);
$req->execute(array('%'.$rech.'%', '%'.$rech.'%')); 
//compter le nombre de rechrche
//mont compteur
$count = $req->rowCount();
if($count >0){
    echo'<h3 class="text-center">  Resultats trouvés pour  " '.$rech.' "</h3> <br> <h4 class="text-center"><span class="glyphicon glyphicon-exclamation-sign"></span>pour prendre un rendez-vous devez vous connectez</h4>' ;  
    while($data = $req -> fetch(PDO::FETCH_OBJ) ){
        ?>
    <div class="row col-md-12" style="background-color: rgba(134, 250, 211,0.2);borde:1"; >
             <br>
                   <div class="col-md-1">
                       <a href="gererhorraires.php"> <img id="personne"src="img/medecin.jpg" alt="compte"></a>
                  </div>
                  <div class="col-md-offset-2 col-md-8" id="dutext">
                  <?php echo '<b> Dr</b>: '.$data ->usermedecin.'<br>'; //$_SESSION["medecin"]=$data ->usermedecin;?>
                  <?php echo '<b> Spécialité: </b>'.$data ->specialite.' <br>'; ?>
                  <?php echo '<b> Adresse du cabinet </b>: '.$data ->adrcab.'<br><br>'; ?>
                  
                </div>
                  <div class="text-center">
                <a id="confirmer" href="prendrerdv.php">Prendre un rendez-vous</a><script> </script>
             <h5 style="color:white";> ____________________________________________________________</h5>  
            </div><br>
             </div>    
     
          <!--  < $_SESSION["inter"]=$_SESSION["medecin"];
    // $_SESSION["medecin"]=null;-->

<?php                
    }
    }
else {
    echo'<h3 class="text-center"> Pas de resultats trouvés pour "'.$rech.'"</h3> <br>' ;
} }


?>
 


</body>
</html>