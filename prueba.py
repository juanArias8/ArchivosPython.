usuariosTxt = open("users.txt","r")
usuarios = usuariosTxt.readlines()
usuariosTxt.close()
print(usuarios)
isuser = False;
login = '1'
while login == '1':
    nameL = input("Ingrese nombre de usuario ==>  ")
    for i in range(len(usuarios)):
        if(usuarios[i] == nameL + "\n"):
            passL = input("Ingrese password de usuario ==>  ")
            if(usuarios[i+1] == passL + "\n"):
                print("Bienvenido " + nameL + "   Será nuestro gusto ayudarte <3")
                isuser = True
                login = '0'
                break;
            else:
                print("Contraseña incorrecta ....")
        else:
            if i == len(usuarios)-1:
                print("Usuario no encontrado")
                login = input("¿Desea volver a intentarlo? \n0 para rechazar\n1 para confirmar")
        


if(isuser == True):
    print("\n\n")
    print("-------------------------------------------------------------------")
    print("-------------------------------------------------------------------")
    opcion = input("Ingrese 1 para modificar o agregar usuario ==>  ")
    bol = True;
    while bol:
        opc1 = input("Ingrese\n 0 para modificar\n1 para agregar ==>  ")
        if opc1 == '0':
            userup = input("ingrese el nombre del usuario a modificar ==>  ")
            for i in range(len(usuarios)):
                if(usuarios[i] == userup+"\n"):
                    opc = input("Ingrese 1 para cambiar nombre\n2 para cambiar contraseña ==>  ")
                    if opc == '1':
                        newname = input("Ingrese el nuevo nombre ==>  ")
                        usuarios[i] = newname
                        break;
                    elif opc == '2':
                        newpass = input("Ingrese la nueva contraseña para ==> " + usuarios[i])
                        isd = newpass.isdigit()
                        if  isd == True:
                            usuarios[i+1] = newpass
                            break;
                        else:
                            print("El valor a ingresar debe ser tipo numérico")
                            break;
                    else:
                        print("Opcion no valida")
                        continue;
                else:
                    if i == len(usuarios) and userup != usuarios[i]:
                        print ("Usuario no encontrado")
                    continue;
        elif opc1 == '1':
            newname = input("Ingrese el nombre para el nuevo usuario ==>  ") 
            newpass = input("Ingrese el password para el nuevo usuario ==>  ") 
            isd = newpass.isdigit()
            if  isd == True:
                usuarios.append(newname + "\n")
                usuarios.append(newpass + "\n")
            else:
                print("El valor a ingresar debe ser tipo numérico")
        else:
            print("Opción no válida")
        print(usuarios)
        usuariosTxt = open("users.txt","w")
        usuariosTxt.writelines(usuarios)
        usuariosTxt.close()
        print("Desea realizar otra acción (?) \n 1 para confirmar \n 0 para cancelar ==>  ")
        con = input()
        if con == '0':
            bol = False
    print("Ha sido un placer servirle <3")


