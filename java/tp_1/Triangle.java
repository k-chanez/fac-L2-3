public class Triangle{
  Point sommets [] = new Point [3];
  public Triangle (){}
  public Triangle (Point p1, Point p2, Point p3){
    sommets = new Point []{p1, p2, p3};
  }
  public Triangle (Point [] s){
    sommets=s;
  }
  @Override
  public String toString (){
    return "Triangle : " + sommets[0].toString () + ",  " + sommets[1].toString () + ", " + sommets[2].toString (); 
  }
  
  public int nbCoteMemelongueur (){
    Segment [] cotes = {new Segment (sommets[0], sommets[1]), new Segment (sommets[0], sommets[2]), new Segment (sommets[1], sommets[2])};
    int i =0;
    double eps = 0.0001;
    double l =cotes[0].longueur ();
    for (Segment s : cotes){
      if (l - s.longueur() < eps) i++;
    }
    return i; 
  }

  public static int max(double []t){
    int index=0;
    double max=t[0];
    for (int i=0; i<t.length; i++){
      if (t[i]>max){
        max=t[i];
	index=i;
      }
    }
    return index;
  }

  public boolean equilateral (){
    return nbCoteMemelongueur() == 3 ;
  }
  public boolean isocele (){
    return nbCoteMemelongueur() == 2 ;
  }
  public boolean rectangle (){
    Segment [] cotes = {new Segment (sommets[0], sommets[1]), new Segment (sommets[0], sommets[2]), new Segment (sommets[1], sommets[2])};
    double [] longueurs = {cotes[0].longueurAuCarre(), cotes[1].longueurAuCarre(), cotes[2].longueurAuCarre()};
    switch (max (longueurs)){
      case 0 : return longueurs[0]==longueurs[1]+longueurs[2];
      case 1 : return longueurs[1]==longueurs[0]+longueurs[2];
      case 2 : return longueurs[2]==longueurs[0]+longueurs[1];
      default:return false;
    } 
  }
}
