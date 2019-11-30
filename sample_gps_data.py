import time
import serial
import os

current_working_directory = os.getcwd()

sample_data_write_path = current_working_directory + '/' + 'sample_gps_output.txt'

uart = serial.Serial('/dev/ttyAMA0', baudrate=9600, timeout=10)

if not uart:
    import sys
    print('Could not find /dev/ttyAMA0')
    sys.exit()

counter = 0

# Write 50 lines of sample data
with open(sample_data_write_path, 'a') as sample_data_file:
    while counter <= 50:
        gps_message = uart.readline()
        print(gps_message)
        sample_data_file.write(str(gps_message) + '\n')
        counter += 1
