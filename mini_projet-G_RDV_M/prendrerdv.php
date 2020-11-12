<?php session_start();?>
<!DOCTYPE html>
<!--here starts the html file-->
<html>
<!--  head  -->
<head>
	<meta charset="utf-8">
	<link rel="stylesheet" href="Assets/css/bootstrap.min.css">
	<link rel="stylesheet" type="text/css" href="style.css">
	<link rel="stylesheet" href="prendrerdv.js">
	<title>prendre un rendez-vous</title>
	
</head>
<!--  head  -->

<!--  body  -->
<body>

<?php
if (isset($_SESSION["inscr"]) and $_SESSION["inscr"]==true) {
    echo "<script>alert('On vous a envoyer un lien de confirmation à votre adresse e-mail.Vérifiez vos mails ')</script>";
    $_SESSION["inscr"]=null;}
?>
<?php
if (isset($_SESSION["rdv"]) and $_SESSION["rdv"]==false) {
    echo "<script>alert('Pour prendre un rendez-vous vous devez vous connecter')</script>";
    $_SESSION["rdv"]=null;}
?>
<?php
if ((isset($_SESSION["rdv"]) and $_SESSION["rdv"]==true) and ((isset($_SESSION["authpat"]) and $_SESSION["authpat"]==true))) {
    echo "<script>alert('Votre rendez-vous est enrigesté.Consultez votre liste des rendez-vous')</script>";
    $_SESSION["rdv"]=null;
} ?>
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
	<br><br><br><br>
	

    <!-- nheader  |ends -->
	<!-- menu  |starts -->
	<br><br>
    <div class="container" id="men">
		<!-- forum  |starts -->
		<div class="col-xs-offset-3 col-xs-6">
		<form id="form" class="form-horizontal " method="post" action="insertrdv.php">
		    <div>
				<h1 id="titre" style="color: white;" class="text-center">La prise de rendez-vous en ligne</h1>
				<br>
				<div class="form-group">
				<label for="categorie" class="control-label">Catégorie:</label>
				<br>
				    <select class="form-control" name="categorie" id="categorie" class="col-sm-2">
						<option value="enfant">enfant (de 2 ans à 12 ans)  </option>
						<option value="adolescent">adolescent (de 12ans à 18 ans)</option>
						<option value="adulte">adulte (de 18 ans à 70 ans)</option>
						<option value="agee">personne agée (plus de 70 ans)</option>
					</select>
				</div>
				<div class="form-group">
				<label for="selecmotif" class="control-label">Le Motif du consultation:</label>
					<select class="form-control" name="selecmotif" id="selecmotif" >
						<option value="consultation"> premiere consultation</option>
						<option value="laser">séance de laser</option>
					</select>
				</div>
				<div class="form-group">
					<label for="dat" class="control-label">sélectionner une date qui vous convient:</label>
					<input class=" form-control" id="dat" type="date" name="dat"  required>
				</div>
				<div class="form-group">
					<label for='heure'class="control-label">sélectionner l'heure qui vous convient:</b></label><br>
					<input class=" form-control" type="time" id="heure" name="heure" required>  
				</div>
				</div><br><br>
				<div class="text-center">

          <button type="submit" id="confirmer">Prendre le rendez-vous</button><br><br>
        </div><br>
	
	<!-- forucm  |ends -->
	</form>
</div>
     </div>
	 <!-- menu  |ends -->
</div>
	<!-- wrapper  |ends -->
	<br><br>
	<footer id="footer-page" class="footer text-center">
		<p id="textFooter">
		Tout Droit reservé. rdv & soins 2020.
		</p>
</footer>
<script src="Assets/jquery/jquery.min.js"></script>
        <script src="Assets/js/bootstrap.min.js"></script>
</body>
<!--  body  -->

<!--here ends of html file -->
</html>