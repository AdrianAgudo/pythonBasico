Algoritmo aplicacion_de_pedidos
definir datos,pedido como caracter
definir facturación,productos como entero

pais_españa<-falso
datos<-'0'
facturación<-0
productos<-0
salir<-falso
pedido<-'0'

escribir("introduce tus datos personales")
leer datos
escribir("pais de referencia")
leer pais_españa
si(!salir) Entonces
	escribir("introduce pedido")
	leer pedido
FinSi
si pedido hacer
	segun pedido hacer
		Caso1:
			(pedido=20$)
			facturación=facturación+20
			producto=producto+1
		Caso2:
			(pedido=25$)
			facturación=facturación+25
			producto=producto+1
		Caso3:
			(pedido=30$)
			facturación=facturación+30
			producto=producto+1
		Caso4:
			escribir("saliendo de lista de deseos")
			salir=Verdadero
		default:
			facturación=facturación+0
			pedido=pedido+0$
	FinSegun
FinSi
si (pais_españa==Falso) Entonces
	facturación<-facturación*1.16
SiNo
	facturación<-facturación*1.21
	
FinSi
Escribir("enviando pdf con datos y facturación")
Escribir("enviar codigo de cliente al telefono y al correo")
FinAlgoritmo
