import os
import time

# Runtime Variables
current_working_directory = os.getcwd()
sample_data_path = current_working_directory + '/' + 'sample-data-files' + '/' + 'gps_data.txt'

# GPS Initialization Details
gps_file = '/dev/ttyAMA0'

class GPS:
    def __init__(self, gps_file, gps_baud_rate=9600, gps_timeout=10):
        self.gps_file = gps_file
        self.gps_baud_rate = gps_baud_rate
        self.gps_timeout = gps_timeout
        self.uart_handler = None
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

    def initialize_uart(self):
        import serial
        try:
            uart = serial.Serial(self.gps_file, baudrate=self.gps_baud_rate, timeout=self.gps_timeout)
        except serial.SerialException as e:
            import sys
            print(f'Connection has failed. Exception: {e}')
            sys.exit()
        self.uart_handler = uart

    def retrieve_sample_gps_data():
        for i in range(0, lines_of_gps_data_limit):
            temp = uart.readline()
            temp = temp.decode('utf-8')
            sample_data_from_gps.append(temp)
        return sample_data_from_gps

    def print_dashboard(self):
        print('=============================')
        print(f'GPS File: {self.gps_file}')
        print('')
        print(f'UTC Time: {self.utc_time[0:2]}:{self.utc_time[2:4]}:{self.utc_time[4:6]}')
        print(f'Latitude: {self.latitude} {self.latitude_direction}')
        print(f'Longitude: {self.longitude} {self.longitude_direction}')
        print(f'GPS Quality: {self.gps_quality}')
        print(f'Satellites In View: {self.satellites_in_view}')
        print(f'Satellite IDs: {self.satellites_ids}')
        print(f'PDOP (Meters): {self.pdop_in_meters}')
        print(f'HDOP (Meters): {self.hdop_in_meters}')
        print(f'VDOP (Meters): {self.vdop_in_meters}')
        print(f'Speed (KM/H): {self.speed_in_kilometers}')
        print('=============================')

    def parse_gps_line(self):
        while True:
            try:
                get_event = self.uart_handler.readline().decode()
            except UnicodeDecodeError:
                continue
            gps_data = get_event.split(',')

    # GPGGA Data
    # 1 - Time UTC, 2 - Latitude, 3 - N or S, 4 - Longitude, 5 - E or W
    # 6 - GPS Quality, 7 - Number, satellites in view, 8 - Horizontal Dilution
    # of precision, 9 - Antenna Altitude above/below sea level (geoid)
    # 10 - Units of Antenna Altitude, Meters, 11 - Geoidal Separation,
    # 12 - Unites of Geoidal Separation, Meters, 13 - Age of Differential Data
    # 14 - Differential Reference Station ID, 15 - Checksum
            if gps_data[0] == '$GPGGA':
                if gps_data[1]:
                    self.update_utc_time(gps_data[1])
                if gps_data[2]:
                    self.update_latitude(gps_data[2])
                if gps_data[3]:
                    self.update_latitude_direction(gps_data[3])
                if gps_data[4]:
                    self.update_longitude(gps_data[4])
                if gps_data[5]:
                    self.update_longitude_direction(gps_data[5])
                if gps_data[6]:
                    if gps_data[6] == '0':
                        self.update_gps_quality = 'Fix Not Available'
                    if gps_data[6] == '1':
                        self.update_gps_quality = 'GPS Fix'
                    if gps_data[6] == '2':
                        self.update_gps_quality = 'Differential GPS Fix'
                if gps_data[7]:
                    self.update_satellites_in_view = gps_data[7]
                os.system('clear')
                self.print_dashboard()

    # GPGSA Data
    # 1 - Total number of messages, 2 - Mode, 3 - ID of 1st satellite used
    # for fix, ..., 14 - ID of 14th satellite used for fix, 15 - PDOP, Meters,
    # 16 - HDOP, Meters, 17 - VDOP, Meters, 18 - Checksum
            if gps_data[0] == '$GPGSA':
                satellites_in_view_list = []
                self.satellites_ids = []
                for i in range(3, 14 + 1):
                    if gps_data[i]:
                        self.satellites_ids.append(gps_data[i])
                self.satellites_in_view = self.satellites_ids.sort()

    # RPRMC Data
    # 1 - Time UTC, 2 - Status, 3 - Latitude, 4 - N or S, 5 - Longitude,
    # 6 - E or W, 7 - Speed over ground, Knots, 8 - Track made good, Degrees
    # true, 9 - Date, ddmmyy, 10 - Magnetic Variation, degrees, 11 - E or W,
    # 12 - Checksum
            if gps_data[0] == '$GPRMC':
                pass

    # GPVTG Data
    # 1 - Track degrees, 2 - T = True, 3 - Track degrees, 4 - M = Magnetic,
    # 5 - Speed, Knots, 6 - N = Knots, 7 - Speed, Kilometers per Hour,
    # 8 - K = Kilometers Per Hour, 9 - Checksum
            if gps_data[0] == '$GPVTG':
                self.update_speed(gps_data[7])

    def update_utc_time(self, utc_time):
        self.utc_time = utc_time

    def update_latitude(self, latitude):
        self.latitude = latitude

    def update_latitude_direction(self, latitude_direction):
        self.latitude_direction = latitude_direction

    def update_longitude(self, longitude):
        self.longitude = longitude

    def update_longitude_direction(self, longitude_direction):
        self.longitude_direction = longitude_direction

    def update_gps_quality(self, gps_quality):
        self.gps_quality = gps_quality

    def update_satellites_in_view(self, satellites_in_view):
        self.satellites_in_view

    def update_satellite_ids(self, satellite_ids):
        pass

    def update_pdop(self, pdop):
        self.pdop_in_meters = pdop

    def update_hdop(self, hdop):
        self.hdop_in_meters = hdop

    def update_vdop(self, vdop):
        self.vdop_in_meters = vdop

    def update_speed(self, speed):
        self.speed_in_kilometers = speed

# gps.py starting point
if __name__ == '__main__':
    import os
    gps = GPS(gps_file)
    gps.initialize_uart()

    gps.parse_gps_line()
