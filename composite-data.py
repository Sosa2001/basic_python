#La libreria de CSV nos permite trabajar con archivos separados por ,
import csv

#La libreria copy nos permite tomar datos de un archivo y usarlos dentro de un programa
import copy

#Se crea el diccionario myVehicle
myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

#Se crea un ciclo for para imprimir cada una de las clave:valor que hay dentro del diccionario
for key, value in myVehicle.items():
    #Se imprime la clave:valor
    print("{} : {}".format(key,value))
    
#Se crea la lista myInventoryList
myInventoryList = []

#Se abre el archivo car_fleet.csv y se guarda dentro de la variable csvFile
with open('car_fleet.csv') as csvFile:
    #Se lee el archivo car_fleet.csv donde su delimitador son las comas
    csvReader = csv.reader(csvFile, delimiter=',') 
    #Se crea la variable lineCount y se le asigna el valor de 0
    lineCount = 0  
    #Se lee cada una de las lineas, filas o renglones del archivo csvReader
    for row in csvReader:
        #Si el valor de las lineas es cero
        if lineCount == 0:
            #Se imprime el nombre de la columna
            print(f'Column names are: {", ".join(row)}')  
            #Se aumenta en 1 el valor de la lineCount
            lineCount += 1  
        #Si el valor de las lineas no es cero
        else:  
            #Imprime en cada una de las claves la posición que fue separada por comas anteriormente
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
            #Se copia el valor de las variables dentro del diccionario myVehicle
            currentVehicle = copy.deepcopy(myVehicle)  
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]  
            #Se agrega a la lista un vehiculo
            myInventoryList.append(currentVehicle)  
            #Se aumenta en 1 el valor de la lineCount 
            lineCount += 1  
    #Se imprime el total de filas, renglones o lineas leidas
    print(f'Processed {lineCount} lines.')
    
    #
    currentVehicle = copy.deepcopy(myVehicle)
    
    #Se crea un for para imprimir cada vahiculo de la lista
for myCarProperties in myInventoryList:
    #Se imprimen los datos de cada vehiculo
    for key, value in myCarProperties.items():
        #Se imprime la llave valor
        print("{} : {}".format(key,value))
        #Se imprime un separador
        print("-----")