import os
import time

# Runtime variables
current_working_directory = os.getcwd()
sample_data_file_path = current_working_directory + '/' + 'sample_gps_output.txt'
lines_of_gps_data_threshold = 1000
gps_file = '/dev/ttyAMA0'
gps_baud_rate = 9600
gps_timeout = 10
gps_sample_output = []

def initialize_uart(gps_file, gps_baud_rate, gps_timeout):
    import serial
    try:
        uart = serial.Serial(gps_file, baudrate=gps_baud_rate, timeout=gps_timeout)
    except serial.SerialException as e:
        import sys
        print('{}'.format(e))
        sys.exit()
    return uart

def retrieve_sample_gps_data(uart, lines_of_gps_data_threshold):
    sample_data_from_gps = []
    for i in range(0, lines_of_gps_data_threshold):
        temp = uart.readline()
        temp = temp.decode('utf-8')
        sample_data_from_gps.append(temp)
    return sample_data_from_gps

def write_sample_gps_data(gps_sample_output):
    with open(current_working_directory + '/' + 'sample_gps_output.txt', 'w') as sample_data_file:
        for entry in gps_sample_output:
            sample_data_file.write(entry)

def parse_gps_line(gps_data_line):
    pass
    # $GPGGA
    # $GPGSA
    # $GPRMC
    # $GPVTG

uart = initialize_uart(gps_file, gps_baud_rate, gps_timeout)

gps_sample_output = retrieve_sample_gps_data(uart, lines_of_gps_data_threshold)

write_sample_gps_data(gps_sample_output)

#class GPS:
#    pass
#    def __init__(self, uart):
#        self.utc_time = None
#        self.latitude = None
#        self.latitude_direction = None
#        self.longitude = None
#        self.longitude_direction = None
#        self.gps_quality = None
#        self.satellites_in_view = None
#        self.satellites_ids = []
#        self.pdop_in_meters = None
#        self.hdop_in_meters = None
#        self.vdop_in_meters = None
#        self.speed_in_kilometers = None
