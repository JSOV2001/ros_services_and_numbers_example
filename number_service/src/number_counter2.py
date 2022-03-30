#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int64
from std_srvs.srv import SetBool

#Se declara el programa como ROS Node
rospy.init_node("number_counter2", anonymous= True)
#Se declara el contador
number_counter = Int64()
#Se saca el objeto
publisher_object = None

#Se procesa los ROS Topic Messages
def topic_callback_function(message):
    print(f"Number: {str(message.data)}")
    #Se invoca al contador para modificarlo
    global number_counter
    #Se modifica el contador
    number_counter.data += message.data #Se añade el valor del ROS Topic Message
    #Se publica el contador actual
    publisher_object.publish(number_counter)
    #Se espera un poco mas
    frequency_object.sleep()

#Se procesa los ROS Service Messages
def service_callback_function(request_message):
    if request_message.data:
        #Se invoca al contador para modificarlo
        global number_counter
        #Se modifica el contador
        number_counter.data = 0
        #Se publica el contador reseteado
        publisher_object.publish(number_counter)
        frequency_object.sleep()
        #Se espera un poco mas
        return [True, "Counter resented"]

#Se le da sus caracteristicas al programa (como ROS Node) de ROS Subscriber Node
subscriber_object = rospy.Subscriber("number", Int64, topic_callback_function) #ROS Topic, el datatpe del ROS Message, funcion callback

#Se le da sus caracteristicas al programa (como ROS Node) de ROS Subscriber Node
publisher_object = rospy.Publisher("number_count", Int64, queue_size=10) #ROS Topic, el datatype del ROS Message, el tamaño del buffer

#Se da una frequencia al ROS Publisher Node 
frequency_object = rospy.Rate(1) #Frecuencia de 1 Hz: Un mensaje por segundo

#Se crea el ROS Service para solicitar el reseteo del contador
service = rospy.Service("/reset_number_count", SetBool, service_callback_function)


#Mantiene al programa de salir y lo pone a seguir escuchando al topic
rospy.spin()