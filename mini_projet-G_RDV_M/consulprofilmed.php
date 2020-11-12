<?php session_start();?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="Assets/css/bootstrap.min.css">
    <link rel="stylesheet" type="text/css" href="style.css">
    <title>RDV&SOINS</title>
</head>
<body>
<?php
if (isset($_SESSION["inscr"]) and $_SESSION["inscr"]==true) {
    echo "<script>alert('inscription réussie Connectez-vous avec vos nouveaux parametres')</script>";
    $_SESSION["inscr"]=null;}
?>

<?php
if (isset($_SESSION["rdv"]) and $_SESSION["rdv"]==true and (isset($_SESSION["authpat"]) and $_SESSION["authpat"]==true)) {
    echo "<script>alert('Votre rendez-vous est enrigesté.Consultez votre liste des rendez-vous')</script>";
    $_SESSION["rdv"]=null;
} 
if (isset($_SESSION["rdv"]) and $_SESSION["rdv"]==true and (isset($_SESSION["authpat"]) and $_SESSION["authpat"]==false)) {
    echo "<script>alert('Votre rendez-vous est n''enrigesté')</script>";
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
    </nav> <br><br><br><br>
    <div class="container">
    <div class="col-md-offset-2 col-md-8" style="background-color:white";>
    <?php if (isset($_SESSION["medecin"])) {
    
    
     echo'medecin'.$_SESSION["medecin"];}?>
    </div>
    </div>
</body>
</html>