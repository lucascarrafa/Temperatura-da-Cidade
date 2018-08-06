import twitter
import time
import serial

arduino = serial.Serial('/dev/ttyUSB0',9600) #recebe os dados do arduino

#inserir os tokens gerados pelo Twitter em https://apps.twitter.com/
api = twitter.Api(consumer_key='',
                      consumer_secret='',
                      access_token_key='',
                      access_token_secret='')

#funcao que posta os dados no usuario logado
def resposta(temp, umid):
	status = api.PostUpdate('São Mateus está com a temperatura de '+temp+' ºC e umidade de '+umid+'%')
	print(status.text) #imprime no terminal o conteudo que foi postado



##____________________MAIN____________________##

while True:
	
	valor = arduino.readline().decode("utf-8")
	umidade, temperatura = valor.split(' ')
	resposta(temperatura[:5],umidade) #os dados recebidos pelo arduino contem um \n no fim de cada linha, para eliminar, foi usado [:5] que pega apenas os cinco primeiros caracteres
	#print(temperatura[:5])
	time.sleep(60)  #espera 60 segundos para enviar a proxima postagem
