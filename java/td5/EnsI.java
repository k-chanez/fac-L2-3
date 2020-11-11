import java.util.*;

public class EnsI {
  private ArrayList<Integer> liste;
  public EnsI () {
    liste = new ArrayList<Integer>();
  }
  public EnsI (int a) {
    liste = new ArrayList<Integer>();
    liste.add(new Integer(a));
  }
  public EnsI (EnsI e) {
    liste = new ArrayList<Integer>();
    //Version iterateur
    ListIterator <Integer> it = e.liste.listIterator();
    while (it.hasNext())
      liste.add (it.next());
    //Version sans iterateur
    /*for(int i=0; i<e.cardinal(); i++)
        liste.add(e.liste.get(i));*/
  }
  public boolean isEmpty () {
    return liste.isEmpty();
  }
  public int cardinal () {
    return liste.size();
  }
  public boolean singleton () {
    return cardinal()==1;
  }
  @Override
  public String toString () {
    return liste.toString();
  }
  public boolean appartient (int a) {
    return liste.indexOf(a) != -1;
  }
  public void add (int a) {
    if(!appartient(a))
        liste.add(new Integer(a));
  }
  private void remove (int a) {
    if(!isEmpty())
        liste.remove(new Integer(a));
  }
  private int getE (int i) {
    return (liste.get(i));
  }
  public EnsI union (EnsI e) {
    EnsI res= new EnsI(e);
    for(int i=0; i< cardinal(); i++)
      res.add(getE(i));
    return res;
  }
  public EnsI inter (EnsI e) {
    EnsI res= new EnsI();
    int a;

    //Version avec iterateur
    ListIterator <Integer> it = liste.listIterator();
    while (it.hasNext()){
      a=it.next();
      if (e.appartient(a))
      res.add(a);
    }

    //Sans iterateur
    /*for(int i=0; i< cardinal(); i++){
        a = liste.get(i);
        if (e.appartient(a))
          res.add(a);
    }*/

    return res;
  }
  public EnsI diff (EnsI e) {
    EnsI res= new EnsI(this);
    int a;
     
    //Version avec iterateur
    ListIterator <Integer> it = liste.listIterator();
    while (it.hasNext()){
      a=it.next();
      if (e.appartient(a))
        res.remove (a);
    }

    //Sans iterateur
    /*for(int i=0; i< e.cardinal(); i++){
        a=(e.liste.get(i));
        if (res.appartient(a))
          res.remove(a);
    }*/
    return res;
  }
  public boolean inclus (EnsI e) {
    int a;
  
    //Version avec iterateur
    ListIterator <Integer> it = liste.listIterator();
    while (it.hasNext()){
      a=it.next();
      if (!e.appartient(a))
        return false;
    }

    //Sans iterateur
    /*for(int i=0; i< cardinal(); i++){
      a=(liste.get(i));
      if (!e.appartient(a))
        return false;
    }*/

    return true;
  }
  @Override
  public boolean equals (Object o) {
    if (o instanceof EnsI){
      EnsI aux = (EnsI)o;
      return inclus(aux) && aux.inclus(this);
    }
    return false;
  }
}

