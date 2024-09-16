print("Bienvenido")
print("Encontrara una serie de protocolos de seguridad para ingresar al edifcio")
print()
print("1. El usuario tiene un nivel de acceso numérico (0 a 5), donde 0 es acceso denegado y 5 es el nivel de acceso más alto.")
print("2. El usuario debe tener una tarjeta activa (True/False) para acceder al edificio.")
print("3. El usuario debe haber cambiado su contraseña en los últimos 30 días.")
print("4. Si cumple todas estas condiciones, se le permitirá acceder, de lo contrario, se denegará el acceso.")

validezT = 0
validezC = 0

ingreso = input("Desea ingresar al edificio?\nSi/No: ")

#Cuenta activa y contraseña
if ingreso =="Si":
    
    print("1. Verificacion de cuenta activa")
    cuentaAct = int(input("Por favor digite el numero de su tarjeta (7 numeros): "))

    if cuentaAct == 3284841:
        validez = 2
        print("Verificacion aceptada")
        contraseña = input("Por favor digite su contraseña: ")
        if contraseña == "01JasTa":
            print("Contraseña correcta")
            validezC = 3
        else:
            print ("Contraseña incorrecta")
            validez = 0

    elif cuentaAct == 1051561:
        print("Verificacion aceptada")
        validez = 2
        contraseña = input("Por favor digite su contraseña: ")
        if contraseña == "02Jsnia":
            print("Contraseña correcta")
            print("¡CONTRASEÑA DESACTUALIZADA! Por favor actualice su contraseña lo mas antes posible")
            validezC = 0
        else:
            print ("Contraseña incorrecta")
            validez = 0

    elif cuentaAct == 1564848:
        print("Verificacion aceptada")
        validez = 2
        contraseña = input("Por favor digite su contraseña: ")
        if contraseña == "01La24d":
            print("Contraseña correcta")
            validezC = 3
        else:
            print ("Contraseña incorrecta")
            validez = 0

    elif cuentaAct == 8478448:
        print("Verificacion aceptada")
        validez = 2
        contraseña = input("Por favor digite su contraseña: ")
        if contraseña == "ec1510d":
            print("Contraseña correcta")
            validezC = 3
        else:
            print ("Contraseña incorrecta")
            validez = 0

    elif cuentaAct == 2120055:
        print("Verificacion aceptada")
        validez = 2
        contraseña = input("Por favor digite su contraseña: ")
        if contraseña == "wkd9n2w":
            print("Contraseña correcta")
            print("¡CONTRASEÑA DESACTUALIZADA! Por favor actualice su contraseña lo mas antes posible")
            validezC = 0
        else:
            print ("Contraseña incorrecta")
            validez = 0

    elif cuentaAct == 9484048:
        print("Verificacion aceptada")
        validez = 2
        contraseña = input("Por favor digite su contraseña: ")
        if contraseña == "AStro23":
            print("Contraseña correcta")
            validezC = 3
        else:
            print ("Contraseña incorrecta")
            validez = 0

    elif cuentaAct != 0:
        print("Cuenta no encontrada")
        validez = 0

    else:
        print("Verificacion rechazada")
        validez = 0

#Validez total acorde a la contraseña y cuenta activa
    validezT = validez + validezC
    print()
    if validezT == 5:
        print("Acceso total al edificio permitido sin restricciones, validacion = 5")
    elif validezT == 2:
        print("Acceso al edificio con areas restringidas, validacion = 2")
    elif validezT == 0:
        print("Acceso denegado al eficio por favor verifique su numero de registro o contraseña si son correctas")

elif ingreso == "No":
    print("Que tenga un buen dia")
else:
    print("Error, seleccionar Si/No")