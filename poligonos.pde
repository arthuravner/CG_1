//float g_a = 0; 
float g_a = HALF_PI;

void setup()
{
  size(500, 500);
  rectMode(CENTER);
}
void draw()
{
  background(200);
  translate(width/2, height/2);
  
  int w = 80; // largura
  int h = 100; // atura
  
  //ellipse
  int raio = 200; //raio
  //int n = 3; // numero de lados poligono
  
  int n = (int)map(mouseX, 0, width, 1, 20);
  
  float angulo = TWO_PI/n;
  
  //rect((width - w)/2, (height - h)/2, w, h);
  //rect(width/2, height/2, w, h);
  //rect(0, 0, w, h);
  //rect(mouseX, mouseY, w, h);
  //ellipse(mouseX, mouseY, w, h);
  //ellipse(0, 0, raio * 2, raio * 2);
  beginShape();
  for(int i = 0; i < n; i++)
  {
    //float x = raio * cos(angulo * i - HALF_PI);
    //float y = raio * sin(angulo * i - HALF_PI);
    float x = raio * cos(angulo * i - g_a);
    float y = raio * sin(angulo * i - g_a);
    //ellipse(x, y, 10, 10);
    vertex(x,y);
  }
  endShape(CLOSE);
  g_a += 0.01;
}

/*

posição hora:
((2pi / 12) * (hora + (minuto/60))) - HALF_PI

pesquisa google sugerida:
processing reference

*/
