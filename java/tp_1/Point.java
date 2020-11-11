class Point {
  protected double abscisse;
  protected double ordonnee;

  public Point () {};
  public Point (double x, double y){
    this.abscisse=x;
    this.ordonnee=y;
  }
  
  public double getAbscisse () {return abscisse;}
  public double getOrdonnee () {return ordonnee;}

  public void setAbscisse (double x) {this.abscisse=x;}
  public void setOrdonnee (double y) {this.ordonnee=y;}

  @Override 
  public String toString () {
    return "(" + abscisse + ", " + ordonnee + ")";
  }
  
  @Override 
  public boolean equals (Object o) {
    if(!(o instanceof Point))
      return false;
    Point p = (Point) o;
    return (abscisse == p.abscisse) && (ordonnee == p.ordonnee); 
  }

  @Override
  public int hashCode() {
    return new Double(abscisse).hashCode() + new Double(ordonnee).hashCode();
  }

  void translate (double dx, double dy) {
    this.abscisse += dx;
    this.ordonnee += dy;
  }
}
