<?php  session_start(); ?>

	
	
	

<?php
include("connectbdd.php");
$userpatient=$_POST["userpatient"];
$age=$_POST["age"];
$adresse=$_POST["adresse"];
$num=$_POST["num"];
$psw=$_POST["psw"];
try{
	$insert1=$rdvsoins->prepare("INSERT INTO patient (userpatient,age,adresse,num,psw) values(?, ?, ?, ?, ?) ");
	$insert1->execute(array($userpatient,$age,$adresse,$num,$psw));
	$insert1->closeCursor();      
$_SESSION["inscr"]=true;
	header("location:index.php");	       }	
	 catch (Exception $e) {
		die("erreur ".$e->getMessage);
		$_SESSION["inscr"]=false;
header("location:creerpatient.php");}

$cle = md5(microtime(TRUE)*100000);		
$stmt = $rdvsoins->prepare("UPDATE patient SET cle=:cle WHERE userpatient like :userpatient");
$stmt->bindParam(':cle', $cle);
$stmt->bindParam(':userpatient', $userpatient);
$stmt->execute();
$destinataire = $adresse;
$sujet = "Activer votre compte" ;
$entete = "From: rdvsoins2020@gmail.com" ;
 
// Le lien d'activation est composé du login(log) et de la clé(cle)
$message = 'Bienvenue sur VotreSite,
 
Pour activer votre compte, veuillez cliquer sur le lien ci-dessous
ou copier/coller dans votre navigateur Internet.
 
http://localhost/pfc/validation.php?log='.urlencode($userpatient).'&cle='.urlencode($cle).'
 
 
---------------
Ceci est un mail automatique, Merci de ne pas y répondre.';
 
 
mail($destinataire, $sujet, $message, $entete) ; // Envoi du mail
 ?>
 	</body>
</html>