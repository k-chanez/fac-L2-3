import java.util.Scanner;

public class Entreprise {
  public static void main(String[] args){
    Employe e1 = new Employe("toto",1000);
    System.out.println(e1);
    System.out.println(e1.getSalaire());
    String s;
    int v;
    Scanner clavier = new Scanner(System.in);
    System.out.print("Entrez un nom : "); s = clavier.nextLine();
    System.out.print("Entrez un salaire : "); v = clavier.nextInt();
    Employe e2 = new Employe(s,v);
    System.out.println(e2);
    System.out.println(e2.getSalaire());
    System.out.println("le nombre d'employes crees est : " + Employe.getNbEmployes()); 
    Employe o1 = new Ouvrier("tata",1000, 2); 
    System.out.println(o1); 
    System.out.println(o1.getSalaire()); 
    System.out.println("le nombre d'employés crées est : " + 
                        Employe.getNbEmployes());
    Technicien t1 = new Technicien ("Titi", 1500, "Controle qualite"); 
    System.out.println(t1); 

    Cadre c1 = new Cadre("Bidule", 2000);
    c1.ajouterUnProjet ("Projet machin"); 
    c1.ajouterUnProjet ("Projet truc"); 
    c1.ajouterUnProjet ("Projet bidule"); 
    c1.ajouterUnProjet ("Projet secret");
    System.out.println (c1); 
    c1.afficherLesProjets ();

    Chef chef = new Chef ("Chief", 3000);
    chef.ajouterEmploye (e2);
    chef.ajouterEmploye (t1);
    chef.ajouterEmploye (c1);
    System.out.println (chef); 
    chef.afficherLesEmployes ();
    System.out.println (chef.getPrime ());
 } 
}

