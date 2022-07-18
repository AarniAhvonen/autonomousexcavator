import nidaqmx
from IPython.display import clear_output
from nidaqmx.constants import CurrentShuntResistorLocation
#from scipy import signal
import matplotlib.pyplot as plt

i=0
my_list=[]
DATA_AI0_LIST =[]
avg_list = []

while i<500:
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_current_chan("Dev1/ai39",min_val=-0.01, max_val=0.02, shunt_resistor_loc=CurrentShuntResistorLocation.EXTERNAL,ext_shunt_resistor_val=100.0)
        sensor_data=task.read()
        clear_output(wait=True)
        my_list.append(sensor_data)
        print(sensor_data)
        i=i+1


    #moving_average###########################


    # if len(DATA_AI0_LIST) != len(DATA_AI1_LIST) or len(DATA_AI0_LIST) != len(DATA_AI2_LIST):
    #     print("We got different numbers of data from the sensors, and they are:")
    #     print(f"{DATA_AI0_LIST}, {DATA_AI1_LIST}, {DATA_AI2_LIST}")
    #     print("Clearing all the datas from the lists......")
    #     DATA_AI0_LIST = []
    #     DATA_AI1_LIST = []
    #     DATA_AI2_LIST = []
    #     print("Cleared the lists......")
    last_sensor_data_0 = sensor_data


    if len(DATA_AI0_LIST) == 10:
        DATA_AI0_LIST.pop(0)

    DATA_AI0_LIST.append(last_sensor_data_0)

    sensor_data_average_0 = sum(DATA_AI0_LIST) / len(DATA_AI0_LIST)

    avg_list.append(sensor_data_average_0)














print(len(my_list))
plt.plot(my_list, color='green',mfc='pink' )
plt.plot(avg_list, color='red',mfc='pink' )
#plt.plot(my_list,'g*', avg_list, 'ro')
#plt.plot( sensor_data)
plt.show()



"""
while 1:
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_current_chan("Dev1/ai2", min_val=-0.01, max_val=0.02, shunt_resistor_loc=CurrentShuntResistorLocation.EXTERNAL,ext_shunt_resistor_val=170.0)
        sensor_data=task.read()
        clear_output(wait=True)
        print(sensor_data)


while 1:
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_current_chan("Dev1/ai2", ai_current_shunt_resistance )
        sensor_data=task.read()
        clear_output(wait=True)
        print(sensor_data)
"""