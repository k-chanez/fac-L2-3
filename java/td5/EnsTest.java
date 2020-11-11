public class EnsTest {
  public static void main(String[] arg){
   EnsI e1= new EnsI(2);
   e1.add (5);
   e1.add (6);
   e1.add (8);
   System.out.println("e1 : " + e1);
   System.out.println("4 appartient a e1 ? " + e1.appartient(4));
   EnsI e2= new EnsI(8);
   System.out.println("Cardinal de e1 : " + e1.cardinal());
   System.out.println("e1 est un singleton ? " + e1.singleton());
   System.out.println("e2 : " + e2);
   EnsI e12 = e2.union(e1);
   System.out.println ("e12, e1 union e2 : " + e12);
   System.out.println("e1 inclus dans e2 ? " + e1.inclus(e12));
   EnsI e1Moins5 = e1.diff (new EnsI (5));
   System.out.println("e1 diff 5 : " + e1Moins5);
   
   EnsI e3= new EnsI(1);
   e3.add (34);
   e3.add (8);
   e3.add (9);
   e3.add (13);
   System.out.println("e3 : " + e3);
   EnsI e1ou3 = e3.union (e1);
   System.out.println ("e1 union e3 : " + e1ou3);
   EnsI e1et3 = e3.inter (e1);
   System.out.println ("e1 inter e3 : " + e1et3);
   //e1.remove (8);
   System.out.println("e1 : " + e1);
   e1=e1.diff(new EnsI(8));
   System.out.println("e1 : " + e1);
  }
}
