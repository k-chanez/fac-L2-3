<<?php 
session_start();
include("connectbdd.php");
$reponse=$rdvsoins->query("SELECT * FROM medecin");
$true=false;
while ($donnees=$reponse->fetch()) {
	if (isset($_POST["usermedecin"]) and $_POST["usermedecin"]==$donnees["usermedecin"] and 
        isset($_POST["mdp"]) and $_POST["mdp"]==$donnees["mdp"]) {

$actif = $donnees['actif'];
$_SESSION["username"]=$donnees["usermedecin"];
header("location:index.php");
$true=true;
	} }
//actiiiiiiive			
if($actif == '1') {$_SESSION["authmed"]=true;$true=true;header("location:index.php");}
else {
	$_SESSION["authmed"]=false;
header("location:connexionmed.php");
}
 ?>