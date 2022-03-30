#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int64

#Se declara el programa como ROS Node
rospy.init_node("number_publisher2", anonymous= True)

#Se da al programa (como ROS Node) sus caracteristicas como ROS Publisher Node
publisher_object = rospy.Publisher("/number", Int64, queue_size=10) #SE declara el ROS Topic, el datatype del ROS Message, y el tamaño del buffer
#El tamaño del buffer puede recibir 10 veces el tamaño del message

#Se da una frequencia al ROS Publisher Node 
frequency_object = rospy.Rate(1) #Frecuencia de 1 Hz: Un mensaje por segundo

number_message = Int64()
while not rospy.is_shutdown():
    #Se declara el contenido del message
    number_message.data = 2
    #Se publica el message en el ROS Topic
    publisher_object.publish(number_message)
    #Se espera un poco mas
    frequency_object.sleep() 
    
rospy.loginfo("Se ha cerrado este nodo")
