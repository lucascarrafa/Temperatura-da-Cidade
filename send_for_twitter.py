import twitter
import time
import serial

arduino = serial.Serial('/dev/ttyUSB0',9600)

api = twitter.Api(consumer_key='',
                      consumer_secret='',
                      access_token_key='',
                      access_token_secret='')

def resposta(temp, umid):
	status = api.PostUpdate('São Mateus está com a temperatura de '+temp+' ºC e umidade de '+umid+'%')
	print(status.text)



##____________________MAIN____________________##

while True:
	
	valor = arduino.readline().decode("utf-8")
	umidade, temperatura = valor.split(' ')
	resposta(temperatura[:5],umidade)
	#print(temperatura[:5])
	time.sleep(60)  
