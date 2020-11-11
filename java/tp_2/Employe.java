class Employe {
  private static int nbEmployesCrees = 0;
  private String nomEmploye;
  private int salaireDeBase;
  public Employe (String n, int s) {
    nbEmployesCrees ++;
    this.nomEmploye = n;
    this.salaireDeBase = s;
  }
  public int getSalaire () {
    return this.salaireDeBase;
  }
  public static int getNbEmployes () {
    return nbEmployesCrees;
  }
  @Override
  public String toString () {
    return "Nom : " + this.nomEmploye;
  }
}
