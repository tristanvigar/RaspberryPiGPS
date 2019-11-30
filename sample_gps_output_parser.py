import os

current_working_directory = os.getcwd()

raw_output = []

# Output Sequence (Source: https://github.com/adafruit/Adafruit_CircuitPython_GPS - About NMEA Data):
#
# GPGGA
#          1          2         3 4          5 6 7  8    9     10 11   12 13 14
# b'$GPGGA,045357.000,5104.5807,N,11403.5843,W,1,09,1.01,1063.9,M,-17.5,M,,*63\r\n'
#
# 1 - Time (UTC) - (hhmmss.sss)
# 2 - Latitude
# 3 - N or S (North or South)
# 4 - Longitude
# 5 - E or W (East or West)
# 6 - GPS Quality
#     0 - Fix Not Available
#     1 - GPS Fix
#     2 - Differential GPS Fix
# 7 - Number Of Satellites In View
# 8 - Horizontal Dilution of Precision
# 9 - Antenna Altitude Above/Below Mean-Sea-Level (Geoid)
# 10 - Units of Antenna Altitude, Meters
# 11 - Geoidal Separation (Difference between WGS-84 Earth Ellipsoid and Mean-Sea-Level (Geoid), "-" means below Ellipsoid
# 12 - Units of Geoidal Seperation, Meters
# 13 - Age of Differential GPS Data, Time in Seconds since last SC104 Type 1 or 9 Update,
#      Null when DGPS is not used
# 14 - Differential Reference Station ID (0000-1023)
# 15 - Checksum


# GPGSA
# b'$GPGSA,A,3,19,13,11,07,15,28,01,17,30,,,,1.33,1.01,0.87*0B\r\n'
#


# GPRMC
#          1          2 3         4 5          6 7    8     9     10 11 12
# b'$GPRMC,045357.000,A,5104.5807,N,11403.5843,W,0.13,71.67,301119, , ,A*45\r\n'
#
# 1 - Time (UTC) - (hhmmss.ss)
# 2 - Status (V = Navigation Receiver Warning)
# 3 - Latitude
# 4 - N or S (North or South)
# 5 - Longitude
# 6 - E or W (East or West)

# GPVTG
# b'$GPVTG,71.67,T,,M,0.13,N,0.24,K,A*0E\r\n'


with open(current_working_directory + '/' + 'sample_gps_output.txt', 'r') as sample_data_file:
    for line in sample_data_file:
        raw_output.append(line.strip())

for line in raw_output:
    print(line)

