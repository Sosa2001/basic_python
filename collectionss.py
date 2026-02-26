#Para crear una lista se usan []
#Creamos la lista myFruitList y dentro de ella guardamos las siguientes frutas "apple", "banana", "cherry"
myFruitList = ["apple", "banana", "cherry"]


#Imprimimos la lsita de frutas completa
print(myFruitList)

#Imprimimos el tipo de dato que es myFruitList
print(type(myFruitList))

#Imprimimos el valor que está en la primera posición de la lista myFruitList (este valor es "apple")
print(myFruitList[0])

#Imprimimos el valor que está en la segunda posición de la lista myFruitList (este valor es "banana")
print(myFruitList[1])

#Imprimimos el valor que está en la tercera posición de la lista myFruitList (este valor es "cherry")
print(myFruitList[2])

#Vamos a cambiar el valor de la lista en su posición 2 que antes era "cherry" y ahora va a ser "orange"
myFruitList[2] = "orange"

#Imprimimos la lista completa con el cambio
print(myFruitList)

#Para crear una tupla se usan ()
#Creamos la tupla llamada myFinalAnswerTuple y dentro de ella guardamos las siguientes frutas "apple", "banana", "pineapple"
myFinalAnswerTuple = ("apple", "banana", "pineapple")

#Imprimimos la lista completa
print(myFinalAnswerTuple)

#Imprimimos el tipo de dato de myFinalAnswerTuple
print(type(myFinalAnswerTuple))

#Imprimimos el primer valor de la tupla que es "apple"
print(myFinalAnswerTuple[0])

#Imprimimos el segundo valor de la tupla que es "banana"
print(myFinalAnswerTuple[1])

#Imprimimos el tercer valor de la tupla que es "pineapple"
print(myFinalAnswerTuple[2])

#Para crear un diccionario se utilizan llaves y dentro de ellas se van a crear una clave y un valor. La clave y el valor van separados por dos puntos y luego de cada clave valor se separa del siguiente usando una coma
#Creamos el diccionario myFavoriteFruitDictionary con las siguientes claves: "Akua", "Saavi", "Paulo", y sus correspondientes valores "apple", "banana", "pineapple"
myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}

#Imprimimos el diccionario completo
print(myFavoriteFruitDictionary)

#Imprimimos el tipo de variable de myFavoriteFruitDictionary
print(type(myFavoriteFruitDictionary))

#Imprimimos el valor de la clave "Akua"
print(myFavoriteFruitDictionary["Akua"])

#Imprimimos el valor de la clave "Saanvi"
print(myFavoriteFruitDictionary["Saanvi"])

#Imprimimos el valor de la clave "Paulo"
print(myFavoriteFruitDictionary["Paulo"])