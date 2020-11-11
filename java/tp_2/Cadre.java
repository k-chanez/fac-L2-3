class Cadre extends Employe {
  protected String [] projets;
  protected static int primeA = 3000;
  public Cadre (String n, int s) {
    super (n, s);
    this.projets = new String [0];
  }
 
  @Override
  public String toString () {
    return super.toString ();
  }


  public boolean ajouterUnProjet (String p) {
    int nbProj = projets.length;
    if (nbProj < 10) {
      String [] tmp = new String [nbProj + 1];
      for (int i = 0; i < nbProj; i++)
        tmp [i] = projets [i]; 
      tmp [nbProj] = p;
      projets = tmp;
      return true;
    }
    else {
      System.out.println ("Impossible d'ajouter un projet, ce cadre en a deja trop en charge");
      return false;
    }
  }

  public void afficherLesProjets () {
    for (int i =0; i < projets.length ; i++)
      System.out.println (projets [i]);
  }
}
