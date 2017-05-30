
#usuarios_array=usuarios.read()
#for i in usuarios:

import funcion
bandera_usuario=0;
bandera_contrasena=0;
usuario_valido=0;
while(usuario_valido==0):
      archivo_usuario=open("users.txt","r")
      usuarios=archivo_usuario.readlines()
      archivo_usuario.close()
     # print(len(usuarios))
      print('RECUERDE ESCRIBIR SU USUARIO ASÍ: NOMBRE_APELLIDO\n'
            'TODO EN MINÚSCULAS')
      usuario_actual=input("Digite el usuario:")
      for i in range (len (usuarios)):
        if usuarios[i]== usuario_actual+"\n":
           bandera_usuario=1;
           contrasena= input("Digite su contraseña:")
           if usuarios[i+1]==contrasena+"\n":
              print("¡BIENVENIDO USUARIO!\n")
              bandera_contrasena=1
              usuario_valido=1;
              break;
      if bandera_usuario==0:
         print("usuario no encontrado")
      if bandera_contrasena==0:
         print("contraseña incorrecta")
      
                        
opcion_menu=input("Elija una opción del menú\n"
                 "1. Editar usuario/Agregar nuevo usuario\n"
                 "2. Consultar datos\n"
                 "3. Consultar/Agregar nuevos examenes a la base de datos\n"
                 "4. Salir\n")
if opcion_menu=='1':
    opcion_menu1=input("Presione 1 para editar un usuario existente\n"
                           "Presione 2 para agregar un nuevo usuario\n")
    bandera_salida=0
    while  bandera_salida==0:
          if opcion_menu1=='1':
             archivo_usuario=open("users.txt","r")
             usuario_actual=input("Digite el usuario que desea editar:")
             prueba=archivo_usuario.read()
             archivo_usuario.close()
             if usuario_actual in prueba:
                   for i in range (len (usuarios)):
                    if usuarios[i]== usuario_actual+"\n":
                       opcion_menu0=input("3 Editar nombre\n"
                                              "4 Editar contraseña\n")
                       if opcion_menu0=='3':
                        print ("ingrese nuevo nombre\n")
                        usuarios[i]=input()+"\n"
                        archivo_usuario=open("users.txt","w")
                        archivo_usuario.writelines(usuarios)
                        archivo_usuario.close()
                        bandera_salida=1
                          
                       elif opcion_menu0=='4':        
                             
                             posible_contrasena= funcion.validar()
                             print(posible_contraseña)
                             usuarios[i+1]= posible_contrasena
                             print(usuarios[i+1])
                             archivo_usuario=open("users.txt","w")
                             archivo_usuario.writelines(usuarios)
                             archivo_usuario.close()
                             bandera_salida=1
                             
             else:
                   print ("El usuario no se encuentra en la base de datos")
                   continue
          elif opcion_menu1=='2':
                archivo_usuario=open("users.txt","a")
                usuario_nuevo=archivo_usuario.write(input('ingrese nombre_apellido: ')+"\n")
                archivo_usuario.close()
                while True:
                       contrasena_nueva=input("Ingrese nueva contraseña:")+"\n"
                       cont=0;
                       for k in range (len (contrasena_nueva)):
                         if contrasena_nueva[k]=='0':
                             cont=cont+1;
                         elif contrasena_nueva[k]=='1':
                             cont=cont+1; 
                         elif contrasena_nueva[k]=='2':
                             cont=cont+1; 
                         elif contrasena_nueva[k]=='3':
                             cont=cont+1;
                         elif contrasena_nueva[k]=='4':
                             cont=cont+1;
                         elif contrasena_nueva[k]=='5':
                             cont=cont+1; 
                         elif contrasena_nueva[k]=='6':
                             cont=cont+1;
                         elif contrasena_nueva[k]=='7':
                             cont=cont+1;
                         elif contrasena_nueva[k]=='8':
                             cont=cont+1;
                         elif contrasena_nueva[k]=='9':
                             cont=cont+1;
                         elif contrasena_nueva[k]=='\n':
                             cont=cont+1;
                            
                         else:
                              
                              if(k+1==(len (contrasena_nueva))):
                                archivo_usuario=open("users.txt","r")
                                usuario=[]
                                ver=archivo_usuario.readlines()
                                archivo_usuario.close()
                                ver.append(contrasena_nueva)
                                for i in range(len(ver)):
                                    usuario.insert(i,ver[i])
                                        
                                archivo_usuario=open("users.txt","w")
                                archivo_usuario.writelines(usuario)
                                archivo_usuario.close()
                                
                       if (cont== len (contrasena_nueva)):
                         archivo_usuario=open("users.txt","r")
                         usuario=[]
                         ver=archivo_usuario.readlines()
                         archivo_usuario.close()
                         ver.append(contrasena_nueva)
                         for i in range(len(ver)):
                                usuario.insert(i,ver[i])              
                         archivo_usuario=open("users.txt","w")
                         archivo_usuario.writelines(usuario)
                         archivo_usuario.close()
                         
                       else:
                           print("contraseña no valida")
                           continue
                
          else:
              print("opcion incorrecta")
          archivo_usuario=open("users.txt","w")
         # archivo_usuario.writelines(usuarios)
          archivo_usuario.close()
          continue      

if opcion_menu=='2':
      opcion_menu2=input('1: para ver todos los pacientes guardados\n'
                             '2: para consultar un paciente\n'
                             '3: volver al menú anterior\n')
      if opcion_menu2=='1':
            archivo_usuario=open('lis.txt','r')
            archivo_usuario.read()
            archivo_usuario.close()
            
      
      
      
    
                   
           
        
     
        
       
       
       
       
    
    
    
    
    




