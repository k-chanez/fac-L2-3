<?php 
session_start();
include("connectbdd.php");
$reponse=$rdvsoins->query("SELECT * FROM patient");
$true=false;
while ($donnees=$reponse->fetch()) {
	if (isset($_POST["userpatient"]) and $_POST["userpatient"]==$donnees["userpatient"] and 
        isset($_POST["psw"]) and $_POST["psw"]==$donnees["psw"]) {

$actif = $donnees['actif'];
$_SESSION["username"]=$donnees["userpatient"];
header("location:index.php");
$true=true;
	} }
//actiiiiiiive			
if($actif == '1') {$_SESSION["authpat"]=true;$true=true;header("location:index.php");}
else {
	$_SESSION["authpat"]=false;
header("location:connexionpat.php");
}
 ?>
 <!--$userpatient = $_POST['userpatient']; 
$stmt = $rdvsoins->prepare("SELECT actif FROM patient WHERE userpatient like :userpatient ");
if($stmt->execute(array(':userpatient' => $userpatient))  && $row = $stmt->fetch())
  {
	   
	 // $actif contiendra alors 0 ou 1
  }
 
if($actif == '1') // Si $actif est égal à 1, on autorise la connexion
  {
   //...
   // On autorise la connexion...
   //...
  }
else // Sinon la connexion est refusé...
  {
   //...
   // On refuse la connexion et/ou on prévient que ce compte n'est pas activé
   //...
  }-->