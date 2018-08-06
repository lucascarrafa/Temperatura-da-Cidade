# Enviando informações sobre temperatura e umidade da cidade para Twitter

## A biblioteca python-twitter
A primeira coisa a se fazer é instalar a biblioteca do Twitter para fazer a comunicação com a plataforma

```
$ pip install python-twitter
```
## Registrar um App Twitter 
O proximo passo é criar um App no site do Twitter
https://apps.twitter.com/
A partir disso é só gerar os tokens necessários para poder realizar a conexão entre o código Python e o microblog

## Esquemático
Na parte de hardware foi utilizado o sensor DHT11 para coletar os dados e enviar para o Arduino Mini.
![Sensor](/imagens/sensor.png)
Em seguida o Arduino envia as informações por cabo USB para o Raspberry Pi 3 que é responsável pelo tratamento de dados e envio para o Twitter.
![Raspberry](/imagens/rasp.png)