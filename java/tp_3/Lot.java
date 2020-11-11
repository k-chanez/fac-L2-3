public abstract class Lot {
  private int numero;
  private int surface;
  private String proprio;
  private int tantiemes;
  
  public abstract void calculerTantiemes ();

  @Override
  public String toString () {
    return "Lot numero : " + numero + ", proprietaire : " + proprio + ", surface : " + surface;
  }
 
  public int    getNumero  () { return numero; }
  public int    getSurface () { return surface; }
  public String getProprio  () { return proprio; }
  public int    getTantiemes () { return tantiemes; }

  public void setNumero    (int n)    { numero  = n; }
  public void setSurface   (int s)    { surface = s; }
  public void setProprio   (String p) { proprio = p; }
  public void setTantiemes (int t)    { tantiemes = t; }
}
