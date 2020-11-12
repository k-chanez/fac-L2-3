<?php
session_start();
include("connectbdd.php");
$categorie=$_POST["categorie"];
$selecmotif=$_POST["selecmotif"];
$dat=$_POST["dat"];
$heure=$_POST["heure"];
if(isset($_SESSION["username"])){$userpatient=$_SESSION["username"];}
$usermedecin=$_SESSION["medecin"];
try {
if(isset($_SESSION["authpat"]) and $_SESSION["authpat"]==true){
	$insert2=$rdvsoins->prepare("INSERT INTO rdv (categorie,selecmotif,dat,heure,userpatient,usermedecin) values (?, ?, ?, ?, ?, ?) ");
	$insert2->execute(array($categorie,$selecmotif,$dat,$heure,$userpatient,$usermedecin));
	$insert2->closeCursor();      
	$_SESSION["rdv"]=true;
	header("location:index.php");	   
}     else{
	$_SESSION["rdv"]=false;
}
}


	
	 catch (Exception $e) {
		die("erreur ".$e->getMessage);
		$_SESSION["rdv"]=false;
		}
		

	header("location:prendrerdv.php");
?>
 	