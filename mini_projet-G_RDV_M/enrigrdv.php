<?php 
session_start();
$categorie=$_POST["categorie"];
$selectmotif=$_POST["selectmotif"];
$selectdate=$_POST["selectdate"];
$heur=$_POST["heur"];
include("connectbdd.php");
try {

	$insert=$bdd->prepare("INSERT INTO rendezvous (categorie,selectmotif,selectdate,heur) values(?, ?, ?, ?) ");
$insert->execute(array($categorie,selectmotif,$selectdate,$heur));
$_SESSION["prendrerdv"]=true;
} catch (Exception $e) {
	die("erreur ".$e->getMessage());
$_SESSION["prendrerdv"]=false;
}
header("location:prendrerdv.php");
 ?>