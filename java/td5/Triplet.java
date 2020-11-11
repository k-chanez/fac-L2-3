class Triplet implements NUpplet {
  protected int x;
  protected int y;
  protected int z;
  
  public Triplet (int x, int y, int z){
    this.x = x;
    this.y = y;
    this.z = z;
  }
  public Triplet (Triplet t){
    this.x = t.x;
    this.y = t.y; 
    this.z = t.z; 
  } 

  @Override
  public int sommeComposantes (){
    return x + y + z;
  }
  @Override
  public int produitComposantes (){
    return x * y * z;
  }
  @Override
  public NUpplet somme (NUpplet n){
    Triplet t1 = (Triplet) n;
    Triplet t = new Triplet (x + t1.x, y + t1.y, z + t1.z);
    return t;
  }
  @Override
  public String toString (){
    return "(" + x + ", " + y + ", " + z + ")";
  }
}  
