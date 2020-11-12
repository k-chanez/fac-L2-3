<?php session_start();?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="Assets/css/bootstrap.min.css">
    <link rel="stylesheet" type="text/css" href="style.css">
    <title>Créer votre compte patient</title>
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
                <li class="active"><a href="inscription.php"><span class="glyphicon glyphicon-user" aria-hidden="true"></span>Inscription</a></li>
                <li><a href="connexionpr.php"><span class="glyphicon glyphicon-log-in" aria-hidden="true"></span> Connexion</a></li>
                <li><a href="contact.php">
                <span class="glyphicon glyphicon-envelope" aria-hidden="true" ></span>Contact </a></li>
    
            </ul>
        </div>
    </nav><br><br>
    <div class="container" id="men">
        <!-- forum  |starts -->
        <div class="col-md-offset-2 col-md-8">
        <form id="formpat" class="form-horizontal " method="post" action="traitpatient.php">
            <div>
                <H2 id="titre" class="text-center"  style="color: white";> Je suis un patient</H2><br>
                <div class="form-group">
                 <Label for="userpatient" >Nom et Prénom<span id="etoile">*</span>:</Label>
                 <input class=" form-control" id="userpatient" name="userpatient" type="text" placeholder="saisissez votre nom complet" required>
                
                </div>
                <div class="form-group">
                    <Label for="age" >Age:</Label>
                    <input class=" form-control" id="age" name="age" type="text" placeholder="saisissez votre age">
                </div>
                <div class="form-group">
                    <Label for="adresse" ><span id="etoile">*</span>Adresse e-mail<span id="etoile">*</span>:</Label>
                    <input class=" form-control" id="adresse" name="adresse" type="text" placeholder="Ex : xxxx@gmail.com">
                    <span  id="aideadresse" ></span> 
                    <h5> Vous allez recevoir un code de confirmation à votre adresse mail.</h5>
                </div>
                <div class="form-group">
                    <Label for="num" >Numéro du téléphone<span id="etoile">*</span>:</Label>
                    <input class=" form-control" id="num" name="num" type="text" value="+231" required>
                </div>
                <div class="form-group">
                    <Label for="psw" >Mot de passe<span id="etoile">*</span>:</Label>
                    <input class="form-control" id="psw" name="psw" type="password" placeholder="8 carractère minimum" required>
                    <span id="aideMdp"></span>
                </div>
                <div class="checkbox">
                    <label>
                        <input type="checkbox" value="">
                        J’accepte les conditions d’utilisation. <br>
                    </label><br>
                </div>
                <div class="text-center">
          <button id="insc" type="submit">S'inscrire</button><br><br>
        </div><br>
            </div>    
        </form>
         </div>
    </div>
  <br><br>
 <footer  id="footer-page" class="footer text-center">
        <p id="textFooter">
        Tout Droit reservé. rdv & soins 2020.
        </p>
</footer>

                            <!--la partie javascipt-->
                <script>       
                 document.getElementById("psw").addEventListener("input", (e) => {
                    var valeur = e.target.value;
                    var qualite = "court"
                    var couleur = "red"
                    if (valeur.length >= 8) {
                        qualite = "Excellent"
                        couleur = "green"
                    } else if (valeur.length >= 4) {
                        qualite = 'moyen'
                        couleur = "orange"
                    }
                    var aideMdp = document.getElementById("aideMdp")
                    aideMdp.textContent = qualite;
                    aideMdp.style.color = couleur;
                })
                document.getElementById("adresse").addEventListener("blur", (e) => {
if (e.target.value.indexOf("@") === -1) {
    document.getElementById("aideadresse").textContent = "format invalide"
} else {
    document.getElementById("aideadresse").textContent = ""
}
})



        </script>
                <script src="Assets/jquery/jquery.min.js"></script>
        <script src="Assets/js/bootstrap.min.js"></script>
</body>
</html>