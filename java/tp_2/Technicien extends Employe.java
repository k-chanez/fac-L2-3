class Technicien extends Employe {
  protected String service;
  protected static int primeA = 1000;
  public Technicien (String n, int s, String serv) {
    super (n, s);
    this.service = serv;
  }
  @Override
  public String toString () {
    return super.toString () + ", service : " + service;
  }
}
