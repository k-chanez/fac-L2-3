class DoubletComparable extends Doublet implements Comparable<DoubletComparable> {
  public DoubletComparable (int x, int y) {super (x, y);}
  public DoubletComparable (DoubletComparable d) {super (d);}
  
  @Override
  public int compareTo (DoubletComparable d) {
    if (produitComposantes () == d.produitComposantes ())
      return 0;
    if (produitComposantes () < d.produitComposantes ())
      return -1;
    else 
      return 1;
  }
}
