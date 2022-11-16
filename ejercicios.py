def ejercicio2():
#nota indiviual:30%, hito grupal 20%,nota examen =50%
#nota se mide en puntos
#sacar nota media =(NHI*0,3)+(NHG*0,2)+(NE*0,5)

#entrada
    print("Ingrese su nota del hito individual, grupal y del examen")
    nhi=float(input('Hito individual: '))
    nhg=float(input('Hito grupal: '))
    ne=float(input('Examen: '))
#proceso
    nm=(nhi*0.3)+(nhg*0.2)+(ne*0.5)
#salida
    print(f'su nota media es {nm}')

#ejercicio2()

def ejercicio3():
#nota de examen 
#20 preguntas
#las preguntas correctas +0,5 , las pregunts incorrectas -0,5 y las preguuntas sin contestar no suman ni restan
#nota examen=(PC*0,5)+(PI*-0,5)

#entrada
    print('De las 20 preguntas dime el número de preguntas que son correctas ,incorrectas y las que has dejado en blanco')
    pc=int(input('Preguntas correctas: '))
    pi=int(input('Preguntas incorrectas: '))
    pb=int(input('Preguntas en blanco: '))
#proceso
    ne=(pc*0.5)+(-pi*0.5)
#salida
    print(f'su nota de examen es {ne}')

#ejercicio3()

