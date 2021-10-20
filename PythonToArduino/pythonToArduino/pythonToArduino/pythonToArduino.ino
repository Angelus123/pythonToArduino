const int led = 13;
const int led1 = 12;
int receivedData = 0;

void setup()
{
  pinMode(led, OUTPUT);
  pinMode(led1, OUTPUT);
  digitalWrite (led, LOW);
  digitalWrite (led1, LOW);
  Serial.begin(9600);
  Serial.println("Connected Successfully");
}

void loop(){
  
  while(Serial.available())
  {
    receivedData = Serial.read();
  }
  
  if (receivedData == '1')
  {
    digitalWrite (led, HIGH);
    digitalWrite (led1, HIGH);
  }
  else if (receivedData == '0')
  {
    digitalWrite (led, LOW);
    digitalWrite (led1, LOW);
  }
}
