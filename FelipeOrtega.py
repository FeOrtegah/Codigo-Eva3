
titulo=f""" {"LISTADO VEHICULOS"}
{"-"*80}
{"marca":<15}{"año":<10}{"kilometraje":<15}{"costo reparacion":<20}{"impuesto":<15}{"total reparacion":<20}
{"-"*80}
"""
menu="""
1.Registrar vehiculo
2.Lista de vehiculos
3.Imprimir lista 
4.salir
"""
pedidos=[]
marcas=["toyota","ford","chevrolet"]

def RegistrarVehiculo():
    while True:
        try:
            marca=input(f"Marca del vahiculo {marcas}: ").split().lower()
            año=int(input("año del vehiculo: "))
            kilometraje=int(input("kilometraje del vehiculo: "))
            reparacion=float(input("costo de reparacion estimado: "))
            impuesto=reparacion *0.08
            total=reparacion + impuesto
            if len(marca)>0 and marca in marcas and año>0 and kilometraje>0 and impuesto>0 and total>0 :
                pedidos.append([marca,año,kilometraje,reparacion,impuesto,total])
                input("pedido añadido con exito")
                break
            else:
                 input("algo se ingreso mal, reingrese...")
        except:
            input("error en el registro")

def ListarTvehiculos():
     salida = titulo
     for t in pedidos:
         salida+=f"{t[0]:<15}" #marca
         salida+=f"{t[1]:<10}" #año
         salida+=f"{t[2]:<15}" #kilometraje
         salida+=f"{t[3]:<20}" #precio estimado
         salida+=f"{t[4]:<15}" #impuesto
         salida+=f"{t[5]:<20}" #total + 8%impuesto
         salida+="\n" 
         return salida    
def ImprimirOrden():
     res=input(f"imprimir [si]: ").split().lower() 
     if res == "si":
         with open (pedidos+".txt","w")as archivo:
             archivo.write(ListarTvehiculos)
while True:
    try:  
        opc=print("")
        if opc == "4":
            break
        elif opc== "1":
            RegistrarVehiculo()
        elif opc=="2":
            ListarTvehiculos()
        elif opc=="3":
            ImprimirOrden()
    except Exception as e:
        input(f"excepcion menu: (str{e})")
