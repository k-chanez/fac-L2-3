<?php
//reponse contien la réponse de mysql
include("connectbdd.php");
$reponse=$rdvsoins->query('SELECT * FROM patient WHERE userpatient="" ' );
while ($donnees = $reponse->fetch())
{
?>
    <p>
    <strong>Nom</strong> : <?php echo $donnees['userpatient']; ?><br />
	Age : <?php echo $donnees['age']; ?> <br>
	 adresse <?php echo $donnees['adresse']; ?> <br />
	tel: <?php echo $donnees['num']; ?> <br>
	mdp: <?php echo $donnees['psw']; ?> <br>
   </p>
<?php
}

$reponse->closeCursor(); // Termine le traitement de la requête

?>