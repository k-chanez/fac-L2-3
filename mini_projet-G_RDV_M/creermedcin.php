<?php session_start();?>
<!DOCTYPE HTML>
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <link rel="stylesheet" href="Assets/css/bootstrap.min.css">
  <link rel="stylesheet" type="text/css" href="style.css">
  <title>Créer votre compte médecin </title>
  
</head>
<body>
<?php
if (isset($_SESSION["inscr"]) and $_SESSION["inscr"]==true) {
    echo "<script>alert('inscription réussie Connectez-vous avec vos nouveaux parametres')</script>";
    $_SESSION["inscr"]=null;
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
            <li class="active"><a href="inscription.php"><span class="glyphicon glyphicon-user" aria-hidden="true"></span>Inscription</a></li>
            <li><a href="connexionpr.php"><span class="glyphicon glyphicon-log-in" aria-hidden="true"></span> Connexion</a></li>
            <li><a href="contact.php">
            <span class="glyphicon glyphicon-envelope" aria-hidden="true" ></span>Contact </a></li>

        </ul>
    </div>
</nav>
<br><br>
  <div class="container" id="men">
    <div class="col-md-offset-2 col-md-8">
      <form id="formmedecin" class="form-horizontal " method="post" action="traitmedecin.php">
        <div>
        <H2 id="titre" class="text-center" style="color: white";> Je suis un médecin</H2>
        <H4 class="text-center" style="color: white";> Si vous êtes un médecin,un expert va vous contacter !</H4>
        
        <br>
        <div id="form-group">
          <label for="usermedecin">Nom et Prénom<span id="etoile">*</span>:</label>
          <input class=" form-control" type="text" name="usermedecin" id="usermedecin" placeholder="saisissez votre nom et prénom" required>
        </div>
        <div id="form-group">
          <label for="age">Age:</label>
          <input class=" form-control" type="text" name="age" id="age" placeholder="saisissez votre age">
        </div> 
        <div id="form-group">
        <label for="spacialite">Spécialité</label>
          <select name="specialite" id="specialite" class=" form-control">
          <option value="ALLEGOLOGIE">ALLEGOLOGIE</option>
          <option value="cardiologie ">Cardiologie </option>
          <optgroup label="Chirurgie">
          <option value="chirurgien">Chirurgien</option>
          <option value="chirurgien-rhino-larygologiste ">Chirurgien-rhino-larygologiste </option>
          <option value="chirurgien-ortho-pediatrie">Chirurgien-ortho-pediatrie</option>
          </optgroup>
          <option value="dentiste">Dentiste</option>
          <option value="dermatologie ">Dermatologie </option>
          <option value="diabetologie">Diabetologie</option>
          <option value="endcronolgie-diabetologie">Endcronolgie-diabetologie</option>
          <option value="gastroenterologie">Gastroenterologie</option>
          <option value="generaliste ">Generaliste </option>
          <option value="genegologie ">Genegologie </option>
          <option value="medecine interne">Medecine interne</option>
          <option value="neurologie">Neurologie</option>
          <option value="oto-rhino-larygologiste">Oto-rhino-laryngologiste</option>
          <option value="ophetalmologie ">Ophetalmologie </option>
          <option value="ortopedie ">Ortopedie </option>
          <option value="pediatrie ">Pediatrie </option>
          <option value="pneumologie">Pneumologie</option>
          <option value="psychologie">Psychologie</option> 
          <option value="psyciatrie">psyciatrie</option>
          <option value="rhumatologie">Rhumatologie</option>
          <option value="radiologie">radiologie</option>
          <option value="stomatologie">Stomatologie</option>
          <option value="urologie">Urologie</option>
          </select> 
        </div>    
        <div id="form-group">
            <label for="adresse">Adresse e-mail<span id="etoile">*</span>:</label>
            <input class=" form-control" type="text" name="adresse" id="adresse" placeholder="Ex : xxxx@gmail.com" required><span  id="aideadresse"></span> 
            <h5>Vous allez recevoir un code de confirmation à votre adresse mail.</h5><br>
        </div>
        <div id="form-group">
            <label for="num"><b>Numéro du téléphone<span id="etoile">*</span>:</label>
            <input class=" form-control" type="num" name="num" id="num"value="+231"required>
        </div><br>
        <div id="form-group">
             <label for="mdp"><b>Mot de passe<span id="etoile">*</span>:</label>
             <input class=" form-control" type="password" name="mdp" id="mdp" placeholder="8 caractères au minimum" required><span id="aideMdp"></span>
        </div>
        <div class="text-center">
        <h3></h3>
        </div>
        <div id="form-group">
              <label for="adrcab">L'adresse du cabinet<span id="etoile">*</span>:</label>
              <input class=" form-control" type="text" name="adrcab" id="adrcab" required>
        </div>
               <h5><span id="etoile">*</span> Indiquer les champs obligatoires que vous devez remplir</h5>
        <div class="checkbox">
                <label>
                    <input type="checkbox" value="">
                    J’accepte les conditions d’utilisation. 
                </label>
        </div>
        <div class="text-center">
          <button id="insc" type="submit">S'inscrire</button><br><br>
        </div><br>  
      </div>         
     </form>
    </div>
  </div> <br><br>
  <footer  id="footer-page" class="footer text-center">
    <p id="textFooter">
    Tout Droit reservé. rdv & soins 2020.
    </p>
</footer>
   <!--la partie javascipt-->
   <script>       
    document.getElementById("mdp").addEventListener("input", (e) => {
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
})</script>
  <script src="Assets/jquery/jquery.min.js"></script>
  <script src="Assets/js/bootstrap.min.js"></script>
</body>
</html>