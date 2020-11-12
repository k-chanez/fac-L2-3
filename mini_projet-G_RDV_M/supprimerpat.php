<?php session_start(); ?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Supprimer mon compte</title>
    <link rel="stylesheet" href="Assets/css/bootstrap.min.css">
    <link rel="stylesheet" href="style.css">
</head>
<body  >
<?php
if (isset($_SESSION["inscr"]) and $_SESSION["inscr"]==true) {
    echo "<script>alert('On vous a envoyer un lien de confirmation à votre adresse e-mail.Vérifiez vos mails ')</script>";
    $_SESSION["inscr"]=null;}
?>
    <nav id="menu"class="navbar navbar-default navbar-fixed-top " role="navigation">
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
        <div id="monmenu"class="collapse navbar-collapse">
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
        </div><!-- /.navbar-collapse -->
    </nav>
    <br><br><br><br><br><br>
    <div class="container">
        <div id="compte" class="col-md-offset-2 col-md-8">
            <div>
            <nav class="navbar navbar-default" role="navigation">
                <div class="col-xs-6">
                    <a href="gerecompte.php"> <img id="personne"src="img/images.png" alt="compte"></a>
                       </div>
                       <div class="col-xs-6">
                           <ul class="nav navbar-nav navbar-right">
                               <li class="active" ><a href="gerecompte.php"><b><u> Gerer mon compte</u></b></a></li>
                               <li><a href="mesrdv.php"> <span class="glyphicon glyphicon glyphicon-time" aria-hidden="true " ></span>Mes rendez-vous</a></li>
                           </ul>
                       </div>
                   </nav>
             <br><br>
                   <nav class="navbar">
                       <div>
                           <ul class="nav  col-md-6">
                               <li ><a href="Modifiercomptepat.php"><span class="glyphicon glyphicon glyphicon-pencil" aria-hidden="true " ></span> Modifier mes informations</a></li>
                               <li style="font-size:17px;"><a href="supprimerpat.php"><span class="glyphicon glyphicon glyphicon-trash" aria-hidden="true " ></span><b> Supprimer mon compte</b></a></li>
                           </ul>
                       </div>
                   </nav>
        </div>
<br>

<form action="traitsuppressionpat.php" method="POST" role="form">
         <div class=" alert">
<h4 style="color: red;"><strong> <span class="glyphicon glyphicon-alert"></span>  A lire avant de supprimer votre compte</h4></strong> <br>

    Lorsque vous supprimer votre compte sur Rdv &soins vous ne pouvez plus le récupérer, ni prendre un rendez-vous en ligne dans cette application.
    Si vous avez des questions, vous pouvez  <a id="rej"href="contact.php">nous contacter</a>. 
</div>
<div class="text-center">
    <br>
    <button type="submit" >Supprimer</button></div></form>
    
<br>
        </div>
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