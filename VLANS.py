vlan = int(input("Ingrese numero de la vlan: "))
if vlan >= 1 and vlan <= 1005:
    print("El numero de la vlan corresponde a una vlan normal")

elif vlan >= 1006 and vlan <=4094:
    print("El numero de la vlan corresponde a una vlan extendida")

else: 
    print("El numero de vlan no corresponde a una categoria.")





