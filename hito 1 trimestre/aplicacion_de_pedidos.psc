Algoritmo aplicacion_de_pedidos
definir datos,pedido como caracter
definir facturaci�n,productos como entero

pais_espa�a<-falso
datos<-'0'
facturaci�n<-0
productos<-0
salir<-falso
pedido<-'0'

escribir("introduce tus datos personales")
leer datos
escribir("pais de referencia")
leer pais_espa�a
si(!salir) Entonces
	escribir("introduce pedido")
	leer pedido
FinSi
si pedido hacer
	segun pedido hacer
		Caso1:
			(pedido=20$)
			facturaci�n=facturaci�n+20
			producto=producto+1
		Caso2:
			(pedido=25$)
			facturaci�n=facturaci�n+25
			producto=producto+1
		Caso3:
			(pedido=30$)
			facturaci�n=facturaci�n+30
			producto=producto+1
		Caso4:
			escribir("saliendo de lista de deseos")
			salir=Verdadero
		default:
			facturaci�n=facturaci�n+0
			pedido=pedido+0$
	FinSegun
FinSi
si (pais_espa�a==Falso) Entonces
	facturaci�n<-facturaci�n*1.16
SiNo
	facturaci�n<-facturaci�n*1.21
	
FinSi
Escribir("enviando pdf con datos y facturaci�n")
Escribir("enviar codigo de cliente al telefono y al correo")
FinAlgoritmo
