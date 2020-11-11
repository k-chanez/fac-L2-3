public class Garage extends Lot {
  private boolean ferme;

  public Garage (int n, int s, String p, boolean f) {
    this.setNumero (n);
    this.setSurface (s);
    this.setProprio (p);
    this.ferme      = f;
  } 
  
  @Override
  public void calculerTantiemes () {
     this.setTantiemes ((this.getSurface () * (ferme ? 2 : 1)) * 14);
  }
  
  @Override
  public String toString () {
    return super.toString () + ferme?", box.":"place de parking."; 
  }
 
}
