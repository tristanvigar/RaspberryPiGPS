# Connect to GPS via uart and collect n samples of GPS data
# This is used for testing the GPS class prior to connecting live
# to GPS module.

import time
import serial
import os

# Set number of GPS events to capture
events_to_capture_threshold = 50

current_working_directory = os.getcwd()

sample_data_write_path = current_working_directory + '/' + 'sample-data-files' + '/' + 'gps_test_output.txt'

uart = serial.Serial('/dev/ttyAMA0', baudrate=9600, timeout=10)

if not uart:
    import sys
    print('Could not find /dev/ttyAMA0')
    sys.exit()

with open(sample_data_write_path, 'a') as sample_data_file:
    for i in range(0, events_to_capture_threshold):
        gps_message = uart.readline()
        print(gps_message)
        sample_data_file.write(str(gps_message) + '\n')
        counter += 1
