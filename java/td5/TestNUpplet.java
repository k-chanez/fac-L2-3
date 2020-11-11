import java.util.TreeSet;

public class TestNUpplet {
  public static void main (String [] args) {
    Doublet d1 = new Doublet (1, 2);
    System.out.println ("d1  : " + d1 + ", somme de ses composantes : " + d1.sommeComposantes ());
    Doublet d2 = new Doublet (2, 3);
    System.out.println ("d2  : " + d2 + ", produit de ses composantes : " + d2.produitComposantes ());
    Doublet d = (Doublet) d1.somme (d2);
    System.out.println (d);
    
    Triplet t1 = new Triplet (1, 1, 1);
    System.out.println ("t1  : " + t1 + ", somme de ses composantes : " + t1.sommeComposantes ());
    Triplet t2 = new Triplet (2, 2, 2);
    System.out.println ("t2  : " + t2 + ", produit de ses composantes : " + t2.produitComposantes ());
    Triplet t  = (Triplet) t1.somme (t2);
    System.out.println (t);
 
    DoubletComparable dc1 = new DoubletComparable (2, 1);
    DoubletComparable dc2 = new DoubletComparable (3, 6);
    System.out.println ("dc1 < dc2 ? " + dc1.compareTo (dc2)); 

    TreeSet <DoubletComparable> s = new TreeSet <DoubletComparable> ();
    s.add (new DoubletComparable (2, 2));
    s.add (new DoubletComparable (1, 2));
    s.add (new DoubletComparable (3, 2));
    s.add (new DoubletComparable (6, 1));
    s.add (new DoubletComparable (1, 1));
    s.add (new DoubletComparable (3, 2));
    s.add (new DoubletComparable (4, 4));
    System.out.println (s);
  }
}
