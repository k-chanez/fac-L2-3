public class Lettre {
  protected String nom;
  protected double montant;

  public Lettre (String n, double m) {
    nom = n;
    montant = m;
  }

  @Override
  public String toString () {
    return "Monsieur, Madame " + nom + ", vous devez " + montant + "Euros.";
  }
}
