public class Segment {
  Point start;
  Point stop;

  //Constructeurs
  public Segment () {}
  public Segment (Point s, Point st) {
    this.start=s;
    this.stop =st;
  }
  public Segment (int x1, int y1, int x2, int y2) {
    this.start=new Point (x1,y1);
    this.stop =new Point (x2,y2);
  }

  //getters
  public Point getStart () {return this.start;}
  public Point getStop  () {return this.stop;}
  
  //setters
  public void setStart (Point s) { this.start=s;}
  public void setStop  (Point s) { this.stop =s;}

  @Override
  public String toString () {
    return "Segment : [ " + start.toString () + ", " +stop.toString () + "]";
  }

  public void translate (double dx, double dy){
    start.translate (dx,dy);
    stop.translate  (dx,dy);
  }
  public boolean extremiteCommune (Segment s){
    return start.equals(s.start) || start.equals (s.stop) || stop.equals(s.start) || stop.equals(s.stop);
  }

  public static boolean extremiteCommune (Segment s1, Segment s2){
    return s1.start.equals(s2.start) || s1.start.equals (s2.stop) || s1.stop.equals(s2.start) || s1.stop.equals(s2.stop);
  }
  public double longueur (){
    return java.lang.Math.sqrt ((stop.abscisse-start.abscisse)*(stop.abscisse-start.abscisse) + (stop.ordonnee-start.ordonnee)*(stop.ordonnee-start.ordonnee));
  }
  public double longueurAuCarre (){
    return (stop.abscisse-start.abscisse)*(stop.abscisse-start.abscisse) + (stop.ordonnee-start.ordonnee)*(stop.ordonnee-start.ordonnee);
  }
  public Point milieu (){
    return new Point ((start.abscisse+stop.abscisse)/2, (start.ordonnee+stop.ordonnee)/2);
  }
}
