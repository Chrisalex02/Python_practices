from datetime import datetime #Del paquete datetime trae la clase datetime

#Pedir la meta y la fecha, separados por dos puntos y dejando un salto de linea
user_input = input("Indique su meta  y la fecha en que desea cumplirla separado por\':\' \n")
input_list = user_input.split(":") #separando el imput cada vez que aparezcan ":"

#split covierte el str en list, se extraen las posciciones
meta = input_list[0]
deadline = input_list[1]

fecha_deadline = datetime.strptime(deadline, "%d.%m.%Y")
#print(fecha_deadline)
#print(type(fecha_deadline))

fecha_hoy = datetime.today()#definir la fecha de hoy
tiempo_restante = fecha_deadline - fecha_hoy

#convertir en entero la fecha y darle formato
# Tiempo restante en segundos dividido para obtener lo minutos y luego las horas
horas_restantes = int(tiempo_restante.total_seconds() /60/60)
mensaje = "El tiempo restante para cumplir su meta de {} es de {} horas"
print(mensaje.format(meta,horas_restantes))