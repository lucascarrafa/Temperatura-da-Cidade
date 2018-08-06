#include <dht.h>

#define PIN A1

dht DHT; //Inicializa o sensor

void setup()
{
  Serial.begin(9600);
  delay(1000);
}

void loop()
{
  DHT.read11(PIN); //Lê as informações do sensor
  Serial.print(DHT.humidity);
  Serial.print(" ");
  Serial.println(DHT.temperature); 

  //Não diminuir o valor abaixo. O ideal é a leitura a cada 2 segundos
  delay(2000);  
}
