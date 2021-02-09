void setup()
{
  Serial.begin(9600);
  pinMode(10,OUTPUT);
  pinMode(9,OUTPUT);
  pinMode(8,OUTPUT);
  Serial.println("a - auto\nr - red\ny - yellow\ng - green\n\nselect mode:");
}

char t = ' ';

void loop()
{
  if(Serial.available()){
       t = Serial.read();
       Serial.println(t);
     }

  if(t == 'a') // auto
     {
       digitalWrite(10, HIGH);
       digitalWrite(9, LOW);
       digitalWrite(8, LOW);
       delay(1000);
       digitalWrite(10, LOW);
       digitalWrite(9, HIGH);
       digitalWrite(8, LOW);
       delay(1000);
       digitalWrite(10, LOW);
       digitalWrite(9, LOW);
       digitalWrite(8, HIGH);
       delay(1000);
     }

  if(t == 'r') // red
     {
       digitalWrite(10, HIGH);
       digitalWrite(9, LOW);
       digitalWrite(8, LOW);
     }

  if(t == 'y') // yellow
     {
       digitalWrite(10, LOW);
       digitalWrite(9, HIGH);
       digitalWrite(8, LOW);
     }

  if(t == 'g') // green
     {
       digitalWrite(10, LOW);
       digitalWrite(9, LOW);
       digitalWrite(8, HIGH);
     }
  }
