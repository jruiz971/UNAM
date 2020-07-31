"""
Synchronize time with server - no ntp

Juan Luis Ruiz Vanegas
juanluisruiz971@gmail.com

Last revision 31072020

"""

#------ PC ------#
import datetime
from datetime import datetime

currentDT = datetime.now()
yearPC, monthPC, dayPC,hoursPC, minutesPC,secondsPC,milisecondsPC = (currentDT.year,currentDT.month,currentDT.day,currentDT.hour,currentDT.minute,currentDT.second,currentDT.microsecond)

#------ SERVER ------#

import os 

serverHour = os.popen('ssh user@SERVERIP "date +"%T.%6N""').read()
time_object = datetime(yearPC,monthPC,dayPC,hoursPC,minutesPC,secondsPC,milisecondsPC).isoformat()
os.system(f'ssh user@IP sudo date -s{time_object}')


hoursServer = serverHour[0:2]
minutesServer = serverHour[3:5]
secondsServer = float(serverHour[6:-1])

#------ Diference PC - SERVER (s) ------#
import math

serverSeconds = []
localSeconds = []
tries = 0
if(hoursPC== int(hoursServer) and  minutesPC == int(minutesServer)):
        while (int(secondsServer) != secondsPC) and tries <20:
            seconds = math.ceil( (secondsPC + secondsServer) /2)
            
            ###Have to be these seconds
            print("Change to Second: ",seconds)
            
            
            #----- CHANGE LOCAL TIME  -----#
            time_object_local = datetime(yearPC,monthPC,dayPC,hoursPC,minutesPC,seconds).isoformat()
            os.system(f"sudo date -s{time_object_local}")
            
            #----- CHANGE SERVER TIME  -----#
            time_object_server = datetime(yearPC,monthPC,dayPC,hoursPC,minutesPC,seconds+1).isoformat() #Add one second for delay
            os.system(f'ssh user@SERVERIP sudo date -s{time_object_server}')
            
            #----- GET NEW LOCAL DATE VALUES -----#
            currentDT = datetime.now()
            secondsPC= currentDT.second
            
            #----- GET NEW SERVER DATE VALUES -----#
            serverHour = os.popen('ssh user@SERVERIP "date +"%T.%6N""').read()
            secondsServer = float(serverHour[6:-1])
            #print("s",secondsPC,secondsServer)
            
            #----- SET LIMIT -----#
            tries += 1
            
            #---- APPEND DATA TO PLOT ----#
            serverSeconds.append(int(secondsServer))
            localSeconds.append(secondsPC)
            
        #----- PLOT -----#


        import matplotlib
        import matplotlib.pyplot as plt
        import numpy as np

        Diference = []
        Iterations = []
        for i in range (len(localSeconds)):
            Diference.append(serverSeconds[i]-localSeconds[i] )
            Iterations.append(i+1)
        fig, ax = plt.subplots()
        ax.plot( Iterations,Diference )


        ax.set(ylabel="Seconds delay", xlabel="Numbers of Iterations", title='TIME DIFFERENCE: \n Server Seconds - Local Seconds')
        ax.grid()
        plt.grid(True)
        plt.savefig('TIME DIFFERENCE'+'.png')
        plt.show()
        
else: 
    #----- IF DIFFERENCE IS BIG, UPDATE SERVER TIME (BECOUSE OF ERRORS FROM OTHER USERS SETTING TIME) -----#
    print("Server",hoursServer,minutesServer,secondsServer)
    print("PC",hoursPC,minutesPC,secondsPC)

    time_object = datetime(yearPC,monthPC,dayPC,hoursPC,minutesPC,secondsPC,milisecondsPC).isoformat()
    os.system(f'ssh user@SERVERIP sudo date -s{time_object}')

    


