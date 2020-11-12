<?php session_start();?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="Assets/css/bootstrap.min.css">
    <link rel="stylesheet" type="text/css" href="style.css">
    <title>Accédez a votre compte</title>
</head>
<body>
<?php
if (isset($_SESSION["inscr"]) and $_SESSION["inscr"]==true) {
    echo "<script>alert('On vous a envoyer un lien de confirmation à votre adresse e-mail.Vérifiez vos mails ')</script>";
    $_SESSION["inscr"]=null;}
?>
      <?php
if (isset($_SESSION["supression"]) and $_SESSION["supression"]==true) {
    echo "<script>alert('Votre compte a éte supprimé !')</script>"; 
    $_SESSION["supression"]=null;
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
                <li><a href="inscription.php"><span class="glyphicon glyphicon-user"></span> Inscription</a></li>
                <li class="active"><a href="connexionpr.php"><span class="glyphicon glyphicon-log-in"></span> Connexion</a></li>
                <li><a href="contact.php"><span class="glyphicon glyphicon-envelope" aria-hidden="true" ></span>Contact </a></li>';
             </ul>
        </div>
    </nav><br><br><br><br>
    <div class="container" id="men">
        <div class="col-md-offset-3 col-md-6">
                    <H2 id="titre" class="text-center" style="color: white;"> Accéder a votre compte</H2><br><br>
                    <h3 class="text-center"  style="font-family: ecrit;">Choisissez votre profil:</h3> <br><br>       
                    <div class="row">
                        <section class="col-md-offset-1 col-md-5">
                            <div class="text-center">
                                <a id="btn" href="connexionmed.php">je suis médecin</a>
                            </div><br>
                        </section>
                        <section class="col-md-5">
                        <div class="text-center">
                            <a id="btn" href="connexionpat.php">je suis patient</a>
                        </div><br>
                    </section>
                   </div>
                   <br><br><br>
                   <h4 class="text-center">Vous êtes nouveau sur Rdv&Soins !  <a  id="rej" href="inscription.php"> S'inscrire</a>  </h4>




    </div></div>
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