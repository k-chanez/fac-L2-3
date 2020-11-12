
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="Assets/css/bootstrap.min.css">
    <link rel="stylesheet" type="text/css" href="style.css">
    <title>Validation</title>
</head>
<body>
<?php
if (isset($_SESSION["inscr"]) and $_SESSION["inscr"]==true) {
    echo "<script>alert('On vous a envoyer un lien de confirmation à votre adresse e-mail.Vérifiez vos mails ')</script>";
    $_SESSION["inscr"]=null;}
?>

<?php
if ((isset($_SESSION["rdv"]) and $_SESSION["rdv"]==true) and ((isset($_SESSION["authpat"]) and $_SESSION["authpat"]==true))) {
    echo "<script>alert('Votre rendez-vous est enrigesté.Consultez votre liste des rendez-vous')</script>";
    $_SESSION["rdv"]=null;
} ?>

<?php
if ((isset($_SESSION["rdv"]) and $_SESSION["rdv"]==true) and ((isset($_SESSION["authpat"]) and $_SESSION["authpat"]==false))) {
    echo "<script>alert('nooooooooooooooon')</script>";
    $_SESSION["rdv"]=null;
} 
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
    </nav> <br><br><br>
  




<?php
session_start();
include("connectbdd.php");

$userpatient = $_GET['log'];
$cle = $_GET['cle'];
 
// Récupération de la clé correspondant au $login dans la base de données
$stmt = $rdvsoins->prepare("SELECT cle,actif FROM patient WHERE userpatient like :userpatient ");
if($stmt->execute(array(':userpatient' => $userpatient)) && $row = $stmt->fetch())
  {
    $clebdd = $row['cle'];    // Récupération de la clé
    $actif = $row['actif']; // $actif contiendra alors 0 ou 1
  }
 
 
// On teste la valeur de la variable $actif récupérée dans la BDD
if($actif == '1') // Si le compte est déjà actif on prévient
  {
     echo '<div class="container col-md-offset-3 col-md-6 text-center"style="background-color:white;>
     <div class="col-md-12" style="background-color:white;"><br>
     <span class="glyphicon glyphicon-info-sign text-center" style="color:rgb(190, 100, 7); font-size:50px";></span> <br>
     <h4> Votre compte est déjà actif !</h4>
     <a href="connexionpat.php">Se Connecter</a><br>
     </div>';
  }
else // Si ce n'est pas le cas on passe aux comparaisons
  {
     if($cle == $clebdd) // On compare nos deux clés    
       {
          // Si elles correspondent on active le compte !    
          echo '<div class="container col-md-offset-3 col-md-6 text-center">
          <p class="col-md-12">
            <a href="#"><img src="img/merci.PNG"
              alt="logo" title="logo"></a>
          </p>
            <div class="col-md-12" style="background-color:white;">
            <span class="glyphicon glyphicon-ok-circle text-center" style="color:green; font-size:50px";></span> <br>
            <h4> Votre compte vient d\'etre activé.Connectez-vous avec vos nouveaux paramètres</h4><br>
            <a href="connexionpat.php">Se Connecter</a>
          </div>
       </div>';
 
          // La requête qui va passer notre champ actif de 0 à 1
          $stmt = $rdvsoins->prepare("UPDATE patient SET actif = 1 WHERE userpatient like :userpatient ");
          $stmt->bindParam(':userpatient', $userpatient);
          $stmt->execute();
          $_SESSION["actif"]=1;
       }
     else // Si les deux clés sont différentes on provoque une erreur...
       {
          echo '<div class="container col-md-offset-3 col-md-6 text-center"style="background-color:white; >
          <div class="col-md-12" style="background-color:white;"><br>
          <span class="glyphicon glyphicon-remove-circle text-center" style="color:red; font-size:50px";></span> <br>
          <h4> Votre compte est déjà actif !</h4>
          <a href="connexionpat.php">Se Connecter</a><br>
          </div>';
       }
  }?>
    
    <script src="Assets/jquery/jquery.min.js"></script>
  <script src="Assets/js/bootstrap.min.js"></script>
  </body>
</html>
