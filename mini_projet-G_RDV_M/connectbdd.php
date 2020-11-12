<?php 
try {
	$bd="mysql:host=localhost;dbname=rdvsoins;charset=utf8";
$login="root";
$mdp="";
$rdvsoins= new PDO($bd,$login,$mdp);//le pont :bdd
 	
 } catch (Exception $e) {
 	die("erreur".$e->getMessage());
 	
 } 
?>