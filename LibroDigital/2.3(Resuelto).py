
"""Realizar un programa que pida al usuario la velocidad de un atleta en m/s y el radio de la
circunferencia de la pista, y resultada el programa devuelve el tiempo que tarda el atleta en dar
2 vueltas a la pista, sabiendo que el atleta descansa 1 minuto cada 1000 metros."""

#solicitamos los datos del corredor y de la pista al usuario
velocidad = float(input("Ingrese la velocidad del atleta teniendo en cuenta que se toma en metros sobre segundos: "))
radio = float(input("Ingrese el radio de la circunferencia de la pista expresada en metros: "))

#calculamos la longutud de la pista por 2 ya que necesita recorrer 2 vueltas
longitud = (2*3.14*radio)*2
#calculo que determina cuantas veces tomará un descanso
descanso = longitud//1000
#tiempo total que tardará en realizar el recorrido, con los descansos incluidos
tiempo = (longitud/velocidad)+(descanso*60)
#imprimimos los resultados
print(f"El tiempo que tardará el atleta va a ser de: {tiempo} segundos")
print(f"O lo mismo que {(tiempo/60)/60} horas") #no solicitado