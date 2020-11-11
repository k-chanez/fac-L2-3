public class SegmentTest {
  public static void main (String [] args) {
    Point a = new Point (2, 3);
    Point b = new Point (3, 4);
    Point c = new Point (4, 5);
    System.out.println ("Point a : " + a);
    System.out.println ("Point b : " + b);
    Segment ab = new Segment (a, b);
    System.out.println ("Segment ab :\n" + ab);
    b.setAbscisse (5);
    b.setOrdonnee (5);
    System.out.println ("Segment ab :\n" + ab);
    Segment quatreEntiers = new Segment (0, 1, 4, 5);
    System.out.println ("Segment quatreEntiers :\n" + quatreEntiers);
    System.out.println ("Extremite commune ? " + ab.extremiteCommune (quatreEntiers));
    System.out.println ("Extremite commune ?(version statique)"+ Segment.extremiteCommune (ab, quatreEntiers));
    Point m = ab.milieu();
    System.out.println ("Coordonnees du milieu de ab : " + m);
    System.out.println ("Longueur du segment ab : " + ab.longueur());
    Triangle t = new Triangle (a, b, c);
    System.out.println (t);
    System.out.println ("Equilateral ? " + t.equilateral ());
    System.out.println ("Isocele ? " + t.isocele());
    System.out.println ("Rectangle ? " + t.rectangle ());
    
  }
}
