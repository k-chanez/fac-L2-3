<?php
session_start();
    include("connectbdd.php");
    try {
$sql ="DELETE FROM patient WHERE userpatient = :name";
$stmt = $rdvsoins->prepare($sql);
$name =$_SESSION["username"];
$stmt->bindValue(':name', $name);
$res = $stmt->execute();
$stmt->closeCursor(); 
$_SESSION["supression"]=true;
$_SESSION["authpat"]=false;
  header("location:connexionpr.php");	}
  catch (Exception $e) {
		die("erreur ".$e->getMessage);
		$_SESSION["supression "]=false;
    header("location:#");}
?>