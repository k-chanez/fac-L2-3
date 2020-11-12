<!--<div class="row col-md-12">
            <div  class="table-responsive " style="background-color:rgb(23, 130, 138);" > 
<table class="table text-body">
       <tr> <td class="col-md-1">ID</td>
        <td class="col-md-2">Userpatient</td>
        <td class="col-md-2">Age</td>
        <td class="col-md-2">E-mail</td>
        <td class="col-md-2">Num</td>
        <td class="col-md-1">mdp</td>
        <td class="col-md-1">modifier</td></tr>
          <
include("connectbdd.php");
$reponse=$rdvsoins->query('SELECT * FROM patient' );
while ($donnees = $reponse->fetch())
{
?>
<table class="">
  <td class="col-md-1">  echo $donnees['id']; ?></td>
  <td class="col-md-2"> echo $donnees['userpatient']; ?></td>
  <td class="col-md-2">  echo $donnees['age']; ?></td>
  <td class="col-md-3"> < echo $donnees['adresse']; ?></td>
  <td class="col-md-3"> < echo $donnees['num']; ?></td>    
  <td class="col-md-1"> < echo $donnees['psw']; ?></td>      
   <td class="col-md-1"> 
   <button type="submit" >modifier</button>
    </td>     
     </table></table>
   </p>
<
}

$reponse->closeCursor(); // Termine le traitement de la requête

?></div>-->
