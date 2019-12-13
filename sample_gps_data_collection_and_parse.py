import os
import time

# Runtime variables
current_working_directory = os.getcwd()
sample_data_file_path = current_working_directory + '/' + 'sample_gps_output.txt'
lines_of_gps_data_limit = 1000
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

def retrieve_sample_gps_data(uart, lines_of_gps_data_limit):
    sample_data_from_gps = []
    for i in range(0, lines_of_gps_data_limit):
        temp = uart.readline()
        temp = temp.decode('utf-8')
        sample_data_from_gps.append(temp)
    return sample_data_from_gps

def write_sample_gps_data(gps_sample_output):
    with open(current_working_directory + '/' + 'sample_gps_output.txt', 'w') as sample_data_file:
        for entry in gps_sample_output:
            sample_data_file.write(entry)

uart = initialize_uart(gps_file, gps_baud_rate, gps_timeout)

gps_sample_output = retrieve_sample_gps_data(uart, lines_of_gps_data_threshold)

write_sample_gps_data(gps_sample_output)

# Class variables are modified by GPGGA, GPGSA, RPRMC and GPVTG
# TODO: Refactor class variable assignments so they are updated
#       when they make the most sense
# TODO: Ensure gps_line_data is decoded prior to being passed to
#       parse_gps_line()
class GPS:
    def __init__(self, uart):
        self.utc_time = None
        self.latitude = None
        self.latitude_direction = None
        self.longitude = None
        self.longitude_direction = None
        self.gps_quality = None
        self.satellites_in_view = None
        self.satellites_ids = []
        self.pdop_in_meters = None
        self.hdop_in_meters = None
        self.vdop_in_meters = None
        self.speed_in_kilometers = None

    def parse_gps_line(gps_data_line):
        gps_data = gps_data_line.split(',')

    # GPGGA Data
    # 1 - Time UTC, 2 - Latitude, 3 - N or S, 4 - Longitude, 5 - E or W
    # 6 - GPS Quality, 7 - Number, satellites in view, 8 - Horizontal Dilution
    # of precision, 9 - Antenna Altitude above/below sea level (geoid)
    # 10 - Units of Antenna Altitude, Meters, 11 - Geoidal Separation,
    # 12 - Unites of Geoidal Separation, Meters, 13 - Age of Differential Data
    # 14 - Differential Reference Station ID, 15 - Checksum
        if gps_data[0] = '$GPGGA':
            pass

    # GPGSA Data
    # 1 - Total number of messages, 2 - Mode, 3 - ID of 1st satellite used
    # for fix, ..., 14 - ID of 14th satellite used for fix, 15 - PDOP, Meters,
    # 16 - HDOP, Meters, 17 - VDOP, Meters, 18 - Checksum
        if gps_data[0] = '$GPGSA':
            pass

    # RPRMC Data
    # 1 - Time UTC, 2 - Status, 3 - Latitude, 4 - N or S, 5 - Longitude,
    # 6 - E or W, 7 - Speed over ground, Knots, 8 - Track made good, Degrees
    # true, 9 - Date, ddmmyy, 10 - Magnetic Variation, degrees, 11 - E or W,
    # 12 - Checksum
        if gps_data[0] = '$GPRMC':
            pass

    # GPVTG Data
    # 1 - Track degrees, 2 - T = True, 3 - Track degrees, 4 - M = Magnetic,
    # 5 - Speed, Knots, 6 - N = Knots, 7 - Speed, Kilometers per Hour,
    # 8 - K = Kilometers Per Hour, 9 - Checksum
        if gps_data[0] = '$GPVTG':
            pass
