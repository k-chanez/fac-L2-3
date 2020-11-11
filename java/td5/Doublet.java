class Doublet implements NUpplet {
  protected int x;
  protected int y;
  
  public Doublet (int x, int y){
    this.x = x;
    this.y = y;
  }
  public Doublet (Doublet d){
    this.x = d.x;
    this.y = d.y; 
  } 

  @Override
  public int sommeComposantes (){
    return x + y;
  }
  @Override
  public int produitComposantes (){
    return x * y;
  }
  @Override
  public NUpplet somme (NUpplet n){
    Doublet d1 = (Doublet) n;
    Doublet d = new Doublet (x + d1.x, y + d1.y);
    return d;
  }
  @Override
  public String toString (){
    return "(" + x+ ", " + y + ")";
  }
}  
