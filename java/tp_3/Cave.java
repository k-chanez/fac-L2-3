Cave.java{
  public Cave (int n, int s, String p) {
    this.setNumero (n);
    this.setSurface (s);
    this.setProprio (p);
  } 
  
  @Override
  public void calculerTantiemes () {
     this.setTantiemes (this.getSurface() * 14);
  }

  @Override
  public String toString () {
    return super.toString () + ", cave."; 
  }
 
}