#This project is from McMaster University, ENGINEER 1P13
ip_address = '172.17.42.73' # Enter your IP Address here
project_identifier = 'P3A' # Enter the project identifier i.e. P3A or P3B
#--------------------------------------------------------------------------------
import sys
sys.path.append('../')
from Common.hardware_project_library import *

hardware = True
QLabs = configure_environment(project_identifier, ip_address, hardware).QLabs
if project_identifier == 'P3A':
    arm = qarm(project_identifier,ip_address,QLabs,hardware)
    table = servo_table(ip_address,QLabs,None,hardware)
else:
    speed = 0.1 # in m/s
    bot = qbot(speed,ip_address,QLabs,project_identifier,hardware)
#--------------------------------------------------------------------------------
# STUDENT CODE BEGINS
#---------------------------------------------------------------------------------

bot.activate_linear_actuator()
bot.linear_actuator_out(3.3)
            
def transfer_container():
    global p_bin_colour
    bot.activate_line_following_sensor()          #activates the line and colour sensors
    bot.activate_color_sensor()
    while True:                        #infinite loop so that the bot keeps going
        try:
            sensor = bot.read_color_sensor()
            if bot.line_following_sensors() == [1, 1]:  #if both sensors on the line, go straight
                bot.set_wheel_speed([0.05,0.05])
            elif bot.line_following_sensors() == [0, 1]:  #if left sensor doesnt detect, turn left until it detects
                bot.set_wheel_speed([0.05, 0])
            else:
                bot.set_wheel_speed([0, 0.05])    #if right sensor doesnt detect, turn right until it detects
            if sensor[0][0] > 0.5:                 #if it reads the desired colour, stop and break the loop
                    bot.stop()
                    break
        except:
            time.sleep(0.1)
            continue
    bot.forward_time(0.5)

def deposit_container():
    bot.activate_linear_actuator()        #activates the actuator to dispense
    bot.linear_actuator_in(3.3)          #does procedure to dispense
    time.sleep(1)  
    bot.linear_actuator_out(3.3)

def home():
    bot.activate_line_following_sensor()
    while True:
        if bot.line_following_sensors() == [1, 1]:  #if both sensors on the line, go straight
            bot.set_wheel_speed([0.05,0.05])
        elif bot.line_following_sensors() == [0, 1]:  #if left sensor doesnt detect, turn left until it detects
            bot.set_wheel_speed([0.05, 0])
        else:
            bot.set_wheel_speed([0, 0.05])    #if right sensor doesnt detect, turn right until it detects
    
def main():
    transfer_container()
    deposit_container()
    home()



#---------------------------------------------------------------------------------
# STUDENT CODE ENDS
#---------------------------------------------------------------------------------
    

    

