
import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.Group;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.Pane;
import javafx.scene.control.*;
import javafx.geometry.Insets;
import javafx.stage.Stage;
import javafx.scene.shape.Circle;
import javafx.scene.input.MouseEvent;
import javafx.scene.paint.Color;
import javafx.scene.Group;
import javafx.scene.control.*;
import javafx.scene.canvas.Canvas;
import javafx.scene.canvas.GraphicsContext;
import javafx.scene.shape.ArcType;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import java.net.URL;
import java.io.File ; 
import javax.imageio.ImageIO ;
import javafx.embed.swing.SwingFXUtils;


public class Souris extends Application {


  private ComboBox <String> cbColor = new ComboBox <String> ();
  private ComboBox <String> cbShape = new ComboBox <String> ();
  private ComboBox <String> cbTaille = new ComboBox <String> ();
  private Color pinceau=Color.GREEN;
  public static void main (String[] args){
    launch (args);
  }
  //method qui construit un triangle
  public static void triangle(GraphicsContext gc ,double firstX , double firstY ,int secondX,int secondY) {
    double xp[] = {0,secondY,secondX,0,secondY};
    double yp[] = {0,secondX,secondX,secondY,0};

    for (int i = 0 ; i< 5 ; i++) {
      xp[i] += firstX ;
      yp[i] += firstY ;
    }

  gc.fillPolygon(xp,yp,3);

  }
  //method qui construit une etoile
  public static void fillStar(GraphicsContext g, double ctrX, double ctrY, int radius, int nPoints, double spikiness)
       {
         
           double xPoint[] = new double[2*nPoints]; 
           double yPoint[] = new double[2*nPoints];
          
           nPoints = (int) (nPoints * 2);
          
           for (int i = 0; i < nPoints; i++)
            {
                double iRadius = (i % 2 == 0) ? radius : (radius * spikiness);
                double angle = (270) + (i * 360.0) / (nPoints);

                xPoint[i] = (int) (ctrX + iRadius * Math.cos(Math.toRadians(angle)));
                yPoint[i] = (int) (ctrY + iRadius * Math.sin(Math.toRadians(angle)));
            }
                g.fillPolygon(xPoint, yPoint, nPoints); 
       }
  @Override 
  public void start (Stage primaryStage){ 

    double w1 = cbTaille.getWidth();
    primaryStage.setTitle("Hello World!");
    cbColor.getItems().addAll("vert", "bleu","Jaune","Noir","Rouge","Orange","Gris");
    cbColor.setValue("couleurs");
    cbShape.setValue("formes");
    cbTaille.setValue("taille par defaut");
    cbShape.getItems().addAll("carre","rectangle","rond","etoile","triangle","arc");
    cbTaille.getItems().addAll("40","60","80","100");
    Canvas canvas = new Canvas(810, 480);
    GraphicsContext gc = canvas.getGraphicsContext2D();
    gc.setFill(Color.GREEN);

    canvas.addEventHandler(MouseEvent.MOUSE_PRESSED, 
        new EventHandler<MouseEvent>() {
            @Override
            public void handle(MouseEvent e) {            
              Color c;
              //couleur par defaut "blanc" parcontre si vous dessiner en blanc et vous enregistrer l'image le dessin s'affiche pas parceque le fond de l'image il est blanc 
              switch (cbColor.getValue ()) {
                case "couleurs" : 
                  gc.setFill(Color.WHITE);
                  break;
                case "vert" : 
                  gc.setFill(Color.GREEN);
                  break;
                case "bleu" :
                  gc.setFill(Color.BLUE);
                  break;
                case"Jaune":
                  gc.setFill(Color.YELLOW);
                  break;
                case "Rouge":
                  gc.setFill(Color.RED);
                  break;
                case "Orange":
                  gc.setFill(Color.ORANGE);
                  break;
                case "Noir" :
                  gc.setFill(Color.BLACK);
                  break;
                case "Gris" :
                  gc.setFill(Color.GRAY);
                  break;
                
              }
              
              switch (cbShape.getValue ()){
                // forme par defaut c'est "rond"
                case "formes":
              //taille par defaut on peut dessiner sans sélectionner la taille 
                  if(!(cbTaille.getValue() == "40" || cbTaille.getValue() == "60" || cbTaille.getValue() == "80" || cbTaille.getValue() == "100")){
                    gc.fillOval(e.getX(), e.getY(), 40, 40);
                  }
                  if (cbTaille.getValue() == "40"){
                    gc.fillOval(e.getX(), e.getY(), 30, 30);
                  }
                  if (cbTaille.getValue() == "60"){ 
                    gc.fillOval(e.getX(), e.getY(), 60, 60);
                  }
                  if (cbTaille.getValue() == "80") {
                    gc.fillOval(e.getX(), e.getY(), 80, 80);
                  }
                  if (cbTaille.getValue() == "100"){ 
                    gc.fillOval(e.getX(), e.getY(), 100, 100);
                    }
                  break ;
            
                case "carre":
                //taille par defaut on peut dessiner sans sélectionner la taille 
                  if(!(cbTaille.getValue() == "40" || cbTaille.getValue() == "60" || cbTaille.getValue() == "80" || cbTaille.getValue() == "100")){
                    gc.fillRect(e.getX(), e.getY(), 40, 40);
                  }
                  //avec la selection de taille
                  if(cbTaille.getValue() == "40"){
                    gc.fillRect(e.getX(), e.getY(), 30, 30);
                  }
                  if(cbTaille.getValue() == "60"){
                    gc.fillRect(e.getX(), e.getY(), 60, 60);
                  }
                  if(cbTaille.getValue() == "80"){
                    gc.fillRect(e.getX(), e.getY(), 80, 80);
                  }
                  if(cbTaille.getValue() == "100"){
                    gc.fillRect(e.getX(), e.getY(), 100, 100);
                  }
                  break;

                  case "rond":
              //taille par defaut on peut dessiner sans sélectionner la taille 
                  if(!(cbTaille.getValue() == "40" || cbTaille.getValue() == "60" || cbTaille.getValue() == "80" || cbTaille.getValue() == "100")){
                    gc.fillOval(e.getX(), e.getY(), 40, 40);
                  }
                  if (cbTaille.getValue() == "40"){
                    gc.fillOval(e.getX(), e.getY(), 30, 30);
                  }
                  if (cbTaille.getValue() == "60"){ 
                    gc.fillOval(e.getX(), e.getY(), 60, 60);
                  }
                  if (cbTaille.getValue() == "80") {
                    gc.fillOval(e.getX(), e.getY(), 80, 80);
                  }
                  if (cbTaille.getValue() == "100"){ 
                    gc.fillOval(e.getX(), e.getY(), 100, 100);
                    }
                  break ;

                case "rectangle":
                //taille par defaut on peut dessiner sans sélectionner la taille
                  if(!(cbTaille.getValue() == "40" || cbTaille.getValue() == "60" || cbTaille.getValue() == "80" || cbTaille.getValue() == "100")){
                    gc.fillRect(e.getX(), e.getY(), 50, 30);
                  }
                  //avec la selection de taille 
                  if (cbTaille.getValue() == "40"){
                    gc.fillRect(e.getX(), e.getY(), 40, 20);
                  }
                  if (cbTaille.getValue() == "60"){
                    gc.fillRect(e.getX(), e.getY(), 60, 40);
                  }
                  if (cbTaille.getValue() == "80"){
                    gc.fillRect(e.getX(), e.getY(), 80, 60);
                  }
                  if (cbTaille.getValue() == "100"){
                    gc.fillRect(e.getX(), e.getY(), 100, 80);
                  }
                  break ;

                case "etoile":
                //taille par defaut on peut dessiner sans sélectionner la taille
                  if(!(cbTaille.getValue() == "40" || cbTaille.getValue() == "60" || cbTaille.getValue() == "80" || cbTaille.getValue() == "100")){
                    fillStar(gc,e.getX(),e.getY(), 13, 5,3);
                  }
                  //avec la selection de taille
                  if ((cbTaille.getValue() == "40")){
                    fillStar(gc,e.getX(),e.getY(), 10, 5,3);
                  }
                  if ((cbTaille.getValue() == "60")){
                    fillStar(gc,e.getX(),e.getY(), 15, 5,3);
                  }
                  if ((cbTaille.getValue() == "80")){
                    fillStar(gc,e.getX(),e.getY(), 18, 5,3);
                  }
                  if ((cbTaille.getValue() == "100")){
                    fillStar(gc,e.getX(),e.getY(), 22, 5,3);
                  }
                    break ;  
                case "triangle":
                //taille par defaut on peut dessiner sans sélectionner la taille
                  if(!(cbTaille.getValue() == "40" || cbTaille.getValue() == "60" || cbTaille.getValue() == "80" || cbTaille.getValue() == "100")){
                    triangle(gc,e.getX(),e.getY(), 50,-28);
                  }
                  //avec la selection de taille
                  if ((cbTaille.getValue() == "40")){
                    triangle(gc,e.getX(),e.getY(),  40, -30);
                  }
                  if ((cbTaille.getValue() == "60")){
                    triangle(gc,e.getX(),e.getY(), 60,-40);
                  }
                  if ((cbTaille.getValue() == "80")){
                    triangle(gc,e.getX(),e.getY(), 80,-50);
                  }
                  if ((cbTaille.getValue() == "100")){
                    triangle(gc,e.getX(),e.getY(),100,-60);
                  }
                    break ;

                case "arc":
              //taille par defaut on peut dessiner sans sélectionner la taille 
                  if(!(cbTaille.getValue() == "40" || cbTaille.getValue() == "60" || cbTaille.getValue() == "80" || cbTaille.getValue() == "100")){
                    gc.fillArc(e.getX(),e.getY(),55,55, 180, 180, ArcType.OPEN);
                  }
                  if (cbTaille.getValue() == "40"){
                    gc.fillArc(e.getX(),e.getY(),40, 40, 180, 180, ArcType.OPEN);
                  }
                  if (cbTaille.getValue() == "60"){
                    gc.fillArc(e.getX(),e.getY(),65, 65, 180, 180, ArcType.OPEN);
                  }
                  if (cbTaille.getValue() == "80"){ 
                    gc.fillArc(e.getX(),e.getY(),85, 85, 180, 180, ArcType.OPEN);
                  }
                  if (cbTaille.getValue() == "100"){
                   gc.fillArc(e.getX(),e.getY(),100,100, 180, 180, ArcType.OPEN);
                  }
                  break ;    
              }      
            }
        });
   
    Group root = new Group();
    BorderPane borderPane = new BorderPane();
    
    Button Enregistre = new Button("enregistre");
    
    EventHandler<ActionEvent> enregistre = new EventHandler<ActionEvent>(){
      public void handle(ActionEvent e){
        try{
          Image voir = canvas.snapshot(null,null);
          ImageIO.write(SwingFXUtils.fromFXImage(voir,null),"png",new File("karim.png"));
        }
        catch(Exception d)  {
          System.out.println("Erreur d'enregistrement" + d);
        }
      }
    };

    Enregistre.setOnAction(enregistre);
    borderPane.setLeft(cbColor);
    borderPane.setCenter(cbTaille);
    borderPane.setRight(cbShape);
    borderPane.setBottom(Enregistre);

    final URL imageURL = getClass().getResource("img.jpg"); 
    final Image image = new Image(imageURL.toExternalForm()); 
    final ImageView imageView = new ImageView(image); 
    imageView.setFitHeight(480);
    imageView.setFitWidth(810);
    //root.getChildren().add(imageView);

    Pane pane = new Pane();
    //pane.getChildren().add(canvas);    
    root.getChildren().addAll(imageView,canvas,borderPane);

    
    primaryStage.setScene(new Scene(root, 810, 480));
    primaryStage.show();
  }
}

