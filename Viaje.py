import requests
import urllib.parse

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "nOiEVp32thvBJLoBNYQBYsjx9pQwhcRR"

while True:
    orig = input("Ciudad de origen: ")
    if orig == "s":
        break
    dest = input("Ciudad de destino: ")
    if dest == "s":
        break 
    url = main_api + urllib.parse.urlencode ({"key" :key, "from" :orig, "to" :dest})
    print ("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data ["info"]["statuscode"]
    if json_status == 0:
        print("API Status: " + str(json_status) + " = A succesful route call.\n")
        print("==========================================================================")
        print("Ciudad de origen: " + (orig) + " Ciudad de destino: " + (dest))
        print("Duracion del viaje: "+ (json_data["route"]["formattedTime"]),"horas")
        print("Millas: " + str(json_data["route"]["distance"]),"millas")
        print("Kilometros: " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)),"km")
        Combustible = str("{:.2f}".format((json_data["route"]["distance"]*1.61)/10))
        print("Combustible utilizado (Ltr):",Combustible)
        print("==========================================================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + "(" + str("{:.2f}".format((each["distance"])*1.61)) + "km)")
            print("==========================================================================")
    elif json_status == 402:
            print("**************************************************************************")
            print("Codigo de estado:" + str(json_status) + "; Entradas de usuario no validas para una o ambas direcciones")
            print("**************************************************************************")
    elif json_status == 611:
            print("**************************************************************************")
            print("Codigo de estado:" + str(json_status) + "; Falta una entrada para una o ambas ubicaciones")
            print("**************************************************************************")
    else:
            print("**************************************************************************")
            print("Codigo de estado:" + str(json_status) + "; Consulte")
            print("https://developer.mapquest.com/documentation/directions-api/status-codes")
            print("**************************************************************************\n")