<?php session_start(); ?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="Assets/css/bootstrap.min.css">
    <link rel="stylesheet" href="style.css">
    <title>Rendez-vous accéptés</title>
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
    </nav>
  
    <div class="container">
        <br><br> <br><br><br><br>
        <div id="compte" class="col-md-offset-2 col-md-8">
            <nav class="navbar navbar-default" role="navigation">
                <div class="col-xs-6">
             <a href="gerecompte.php"> <img id="personne"src="img/images.png" alt="compte"></a>
                </div>
                <div class="col-xs-6">
                    <ul class="nav navbar-nav navbar-right">
                        <li ><a href="gerecompte.php"> Gerer mon compte</a></li>
                        <li class="active"><a href="mesrdv.php"><span class="glyphicon glyphicon glyphicon-time" aria-hidden="true " ></span> <b><u> Mes rendez-vous</u></b></a></li>
                    </ul>
                </div>
            </nav>
      <br><br>
                             <h4 class="text-center"><span class="glyphicon glyphicon glyphicon-calendar" aria-hidden="true" > </span> Listes des rendez-vous</h4><br><br>
<div class="col-md-12">
    <div  class=" col-md-4">
        <ul  class="nav">
            <li id="vert" ><a href="rdvacceptes.php"> Rendez-vous accéptés</a></li>
            <li id="orange"><a href="rdvenattente.php"> Rendez-vous en attentes </a></li>
            <li class="active" id="rouge" style=background-color:rgb(201,7,7) ;><a href="rdvrefuses.php"><b> Rendez-vous refusés</b> </a></li>
        </ul>
        <br><br>
    </div>
    <div  class="cadrerouge col-md-offset-2 col-md-6">
        hkjcwhjkh
        wslckjwkljc
        wclkjckwj <br>
        ijqzuhfdsqhujh <br>
        sfljsklj
        sflskhjfh$ <br>
        shcjksqh <br>
        hkjcwhjkh
        wslckjwkljc
        wclkjckwj <br>
        
        
    </div>
    <br><br>
</div><br><br><br>

    <div><br>
        <h5 class="text-center">Prendre un autre rendez-vous par<a id="rej" href="prendrerdv.php"> ici!</a></h5>
    </div><br><br>
</div>

    </div>
    <br><br>
  <footer  id="footer-page" class="footer text-center">
        <p id="textFooter">
        Tout Droit reservé. rdv & soins 2020.
        </p>
</footer>
    <script src="Assets/jquery/jquery.min.js"></script>
  <script src="Assets/js/bootstrap.min.js"></script>
</body>
</html>