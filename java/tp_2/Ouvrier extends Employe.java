class Ouvrier extends Employe {
  protected int numAtelier;
  public Ouvrier (String n, int s, int num) {
    super (n, s);
    this.numAtelier = num;
  }
  @Override
  public String toString () {
    return super.toString () + ", atelier : " + numAtelier;
  }
}
