public class Appartement extends Lot {
  private int etage;
  private int surfBalcon;

  public Appartement (int n, int s, String p, int e, int b) {
    this.setNumero (n);
    this.setSurface (s);
    this.setProprio (p);
    this.etage      = e;
    this.surfBalcon = b;
   
  } 
  
  @Override
  public void calculerTantiemes () {
     this.setTantiemes ((this.getSurface() * 3 + surfBalcon) * (10 + 4 * etage));
  }

  @Override
  public String toString () {
    return super.toString () + ", etage : " + etage + ", surface du balcon : " + surfBalcon + ".";
  }
 
}
