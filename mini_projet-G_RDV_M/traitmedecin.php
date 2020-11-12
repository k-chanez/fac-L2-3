<?php
session_start();
include("connectbdd.php");
$usermedecin=$_POST["usermedecin"];
$age=$_POST["age"];
$specialite=$_POST["specialite"];
$adresse=$_POST["adresse"];
$num=$_POST["num"];
$mdp=$_POST["mdp"];
$adrcab=$_POST["adrcab"];
try {
	$insert1=$rdvsoins->prepare("INSERT INTO medecin (usermedecin,age,specialite,adresse,num,mdp,adrcab) values(?, ?, ?, ?, ?, ?, ?) ");
	$insert1->execute(array($usermedecin,$age,$specialite,$adresse,$num,$mdp,$adrcab));
	$insert1->closeCursor();      
	$_SESSION["inscr"]=true;     
	header("location:index.php");             
	
	}
	
	 catch (Exception $e) {
		die("erreur ".$e->getMessage);
		$_SESSION["inscr"]=false;
		header("location:creermedcin.php");
}
$cle = md5(microtime(TRUE)*100000);		
$stmt = $rdvsoins->prepare("UPDATE medecin SET cle=:cle WHERE usermedecin like :usermedecin");
$stmt->bindParam(':cle', $cle);
$stmt->bindParam(':usermedecin', $usermedecin);
$stmt->execute();
$destinataire = $adresse;
$sujet = "Activer votre compte" ;
$entete = "From: rdvsoins2020@gmail.com" ;
 
// Le lien d'activation est composé du login(log) et de la clé(cle)
$message = 'Bienvenue sur VotreSite,
 
Pour activer votre compte, veuillez cliquer sur le lien ci-dessous
ou copier/coller dans votre navigateur Internet.
 
http://localhost/pfc/validationmed.php?log='.urlencode($usermedecin).'&cle='.urlencode($cle).'
 
 
---------------
Ceci est un mail automatique, Merci de ne pas y répondre.';
 
 
mail($destinataire, $sujet, $message, $entete) ; // Envoi du mail
		?>  