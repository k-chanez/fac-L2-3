<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Modifier les informations</title>
    <link rel="stylesheet" href="Assets/css/bootstrap.min.css">
    <link rel="stylesheet" href="style.css">
</head>
<body  >
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
    <br><br><br><br><br><br>
    <div class="container">
    <div id="compte" class="col-md-offset-1 col-md-10">
            <nav class="navbar navbar-default" role="navigation">
                <div class="col-md-1">
             <a href="comptemedecin.php"> <img id="personne"src="img/medecin.jpg" alt="compte"></a>
                </div>
                <div class="col-md-10">
                    <ul class="nav navbar-nav navbar-right">
                        <li  class="active" ><a href="comptemedecin.php">
                        <span class="glyphicon glyphicon-edit" aria-hidden="true"></span><b><u> Modifier mon compte</u></b></a></li>
                        <li><a href="gererhorraires.php"><span class="glyphicon glyphicon glyphicon-time" aria-hidden="true " ></span> Gérer les jours et les horraire de travail</a></li>
                        <li><a href="gererrdv.php"><span class="glyphicon glyphicon glyphicon-list" aria-hidden="true" > </span> La liste rendez-vous</a></li>
                    </ul>
                </div>
            </nav>
      <br><br>
                   <nav class="navbar">
                       <div>
                           <ul class="nav  col-md-6">
                               <li style="font-size:17px;"><a href="modifiercomptemedecin.php"><span class="glyphicon glyphicon glyphicon-pencil" aria-hidden="true " ></span>  <b>Modifier mes informations</b></a></li>
                               <li><a href="supprimermedecin.php"> <span class="glyphicon glyphicon glyphicon-trash" aria-hidden="true " ></span> Supprimer mon compte</a></li>
                           </ul>
                       </div>
                   </nav>
        
      <br><br>
        <div class="col-md-offset-5 col-md-6">
                <form id="formmodifier" class="form-horizontal " method="post" action="taritmodifiermed.php">
                   <div class="form-group">
                    <label for="prenom">Nom et Prénom :</label>
                   <input type="text" name="prenom" id="prenom" >
                   <br>
                   </div>

                   <div class="form-group">
                       <label for="mail"> Address e-mail : </label>
                       <input type="text" id="mail" name="mail" >
                       <br> 
                   </div>

                   <div class="form-group">
                       <label for ="tel">Numéro de téléphone : </label>
                       <input type="text" id="tel" name="tel">  <br>
                   </div>
                   <div class="form-group">
                       <label for ="tel">Années d'expérience: </label>
                       <input type="text" id="tel" name="tel">  <br>
                   </div>

                   <div class="form-group">
                      <label for="mdp"> Mot de passe :</label>
                      <input type="password" id="mdp" name="mdp"><br>
                   </div>

                   <div class="form-group">
                       <label for ="mdpa"> Actuel :</label>
                       <input type="text" id="mdpa" name="mdpa"> <br> 
                   </div>
                   
                   <div class="form-group">
                    <label for ="mdpn"> Nouveau :</label>
                   <input type="text" id="mdpn" name="mdpn" > <br>
                   </div><br>
                   <div>
                    <button type="submit">Confirmer</button>
                    <button type="reset" >Annuler</button>
                    </div>
                    <br>
                </div>
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