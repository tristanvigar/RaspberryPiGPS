import os
import serial
import time

current_working_directory = os.getcwd()
sample_data_file_path = current_working_directory + '/' + 'sample_gps_output.txt'

try:
    uart = serial.Serial('/dev/ttyAMA0', baudrate=9600, timeout=10)
except serial.SerialException as e:
    import sys
    print('{}'.format(e))
    sys.exit()

with open(current_working_directory + '/' + 'sample_gps_output.txt', 'r') as sample_data_file:
    for line in sample_data_file:
        temp = line.strip()
        raw_output.append(temp[2:-1])

for entry in raw_output:
    current_entry = entry.split(',')
    print(current_entry)

    # $GPGGA
    # $GPGSA
    # $GPRMC
    # $GPVTG

class GPS:
    pass
#    def __init__(self, uart):
#        self.utc_time = None
#        self.latitude = None
#        self.latitude_direction = None
#        self.longitude = None
#        self.longitude_direction = None
#        self.gps_quality
#        self.satellites_in_view
#        self.satellites_ids = []
#        self.pdop_in_meters
#        self.hdop_in_meters
#        self.vdop_in_meters
#        self.speed_in_kilometers

# Time (UTC)
# Latitude (Either GGA or RMC)
# N or S
# Longitude (Either GGA or RMC)
# E or W
# Number of satellites in view
# GPS Quality (0, 1, 2)
# Satellites in view
# Satellite IDs (14 possible)
# PDOP, Meters
# HDOP, Meters
# VDOP, Meters
# Speed, Kilometers Per Hour
