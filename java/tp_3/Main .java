public class Main {
  public static void main (String [] args) {
   Appartement a = new Appartement (8, 100, "Dupond", 2, 10);
   Cave c = new Cave (34, 10, "Dupont");
   Immeuble i = new Immeuble ("Rue de la Soif, Paris");
   i.ajouterLot (a);
   i.ajouterLot (c);
   Lettre [] l = i.genererLettres (30000);
   for (Lettre li : l)
    System.out.println (li);
  }
}
