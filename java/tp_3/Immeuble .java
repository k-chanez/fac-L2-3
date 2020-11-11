public class Immeuble {
  private String adresse;
  private Lot [] lots;
  private double totalTantiemes;

  public Immeuble (String a) {
    adresse = a;
    lots = new Lot [0];
  }

  public double getTotalTantiemes () {return totalTantiemes;}
  public Lot [] getLots () {return lots;}
  
  public void ajouterLot (Lot l) {
    int nbLots = lots.length;
    Lot [] tmp = new Lot [nbLots + 1];
    for (int i = 0; i < nbLots; i++)
        tmp [i] = lots [i]; 
    tmp [nbLots] = l;
    lots = tmp;
  }

  public int existeLot (int num){
     for (int i=0; i<lots.length; i++){
       if (lots[i].getNumero() == num) 
	 return i;
     }
     return -1;
  }
 
   public boolean supprimerLot (int num) {
    int nbLots = lots.length;
    int index = existeLot(num);
    if (index !=-1){
      Lot [] tmp = new Lot [nbLots-1];
      for (int i=0; i < index; i++)
        tmp[i]=lots[i];
      for (int i=index+1, j=index ; i<nbLots; i++, j++)
        tmp[j]=lots[i];
      lots=tmp;
      return true;
    }
    return false;
  }

  public void calculerTantieme () {
    for (Lot l : lots) {
      l.calculerTantiemes ();
    }
  }

  public void calculerTotalTantiemes () {
    calculerTantieme ();
    double total = 0;
    for (Lot l : lots) {
      total += l.getTantiemes();
    } 
    totalTantiemes = total;
  }
  public Lettre [] genererLettres (double charges) {
    calculerTotalTantiemes ();
    Lettre [] lettres = new Lettre [lots.length];
    int i =0;
    for (Lot l : lots) {
      lettres [i] = new Lettre (l.getProprio(), l.getTantiemes()/totalTantiemes * charges);
      i++;
    }
    return lettres; 
  }


}
