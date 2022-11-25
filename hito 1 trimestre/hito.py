
def gestiondepedidos():
    while True:
            inicio=input('Bienvenido a su compra, desea registrarse o iniciar sesión: ')
            if inicio=='registrarse':
                    break 
            if inicio=='iniciar sesión':
                    break

    if inicio=='registrarse':
        nombre=input('Dime tu nombre y apellidos: ')
        correo=input('Dime tu correo electrocino: ')
        contraseña=input('Digame una contraseña')
        numero=input('Dime tu número de telefono: ')
        print('Se ha registrado correctamente')

    elif inicio=='iniciar sesión':
        correo=input('Dime tu correo electrocino: ')
        contraseña=input('Digame su contraseña ')
        numero=0000000
        nombre='X'
        print('Ha iniciado sesión correctamente')

    print('Tenemos 3 productos a la venta' )
    print('producto1=20€(sin contar el iva)')
    print('producto2=25€(sin contar el iva)')
    print('producto3=30€(sin contar el iva)')
    print('Para comprar eliga el producto que quiera entre producto1, producto2 y producto3')
    print('Cuando ya quiera terminar la compra ponga terminar ')
    pedido=0
    facturación=0
    while True:
        pedidos=input('Diga los productos que quiere comprar:')
        if pedidos=='producto1':
            facturación=facturación+20
            pedido=pedido+1
            print('ha añadido el producto 1')
        elif pedidos=='producto2':
            facturación=facturación+25
            pedido=pedido+1
            print('ha añadido el producto 2')
        elif pedidos=='producto3':
            facturación=facturación+30
            pedido=pedido+1
            print('ha añadido el producto 3')
        elif pedidos=='terminar':
            break
        else:
            print('No ha pedido ningún producto')
    print(f'Ha realizado un total de {pedido} pedidos')
    pais=(input('Usted compra desde España: '))
    if pais== 'si':
        factura=facturación*1.21
        print(f'Su factura total es de {factura}')
    else:
        factura=facturación*1.16
        print(f'Su factura total es de {factura}')
    print(f'Se le ha enviado la factura en pdf a {correo}')
    print(f'Se le ha enviado el el código de seguimiento a {correo} y a su telefono {numero}. ')
    print(f'Gracias por su compra {nombre}')


gestiondepedidos()