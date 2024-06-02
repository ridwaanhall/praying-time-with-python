import math
from datetime import datetime, timedelta

class PrayerTimesCalculator:
    def __init__(self, longitude, latitude, timezone, elevation, temperature, pressure, date, eq_of_time, declination, hisab_range):
        # Convert inputs to appropriate units and formats
        self.longitude = self.deg_to_decimal(longitude)
        self.latitude = self.deg_to_decimal(latitude)
        self.timezone = timezone
        self.elevation = elevation
        self.temperature = temperature
        self.pressure = pressure
        self.date = datetime.strptime(date, "%d %B %Y")
        self.eq_of_time = self.time_to_decimal(eq_of_time)
        self.declination = self.deg_to_decimal(declination)
        self.hisab_range = hisab_range
        print(f"Initialization complete with values:\nLongitude: {self.longitude}, Latitude: {self.latitude}, Timezone: {self.timezone}, Date: {self.date}\nEquation of Time: {self.eq_of_time}, Declination: {self.declination}")

    @staticmethod
    def deg_to_decimal(deg_str):
        # Convert degrees, minutes, seconds to decimal degrees
        d, m, s = map(float, deg_str.split(' '))
        decimal = d + (m / 60) + (s / 3600)
        print(f"Converted degrees {deg_str} to decimal {decimal}")
        return decimal

    @staticmethod
    def time_to_decimal(time_str):
        # Convert minutes and seconds to decimal minutes
        m, s = map(float, time_str.split('m'))
        decimal = m + (s / 60)
        print(f"Converted time {time_str} to decimal minutes {decimal}")
        return decimal

    def calculate_dhuhr(self):
        # Step-by-step Dhuhr calculation
        print("Calculating Dhuhr time...")
        noon = 12 + self.timezone - (self.longitude / 15) - (self.eq_of_time / 60)
        print(f"Solar Noon calculation: 12 + {self.timezone} - ({self.longitude} / 15) - ({self.eq_of_time} / 60) = {noon}")
        return noon

    def calculate_isya(self, angle=18):
        # Step-by-step Isya calculation based on angle
        print(f"Calculating Isya time with angle {angle}...")
        D = (math.sin(math.radians(-angle)) - math.sin(math.radians(self.latitude)) * math.sin(math.radians(self.declination))) / (math.cos(math.radians(self.latitude)) * math.cos(math.radians(self.declination)))
        print(f"Hour angle (D) calculation: D = (sin(radians(-{angle})) - sin(radians({self.latitude})) * sin(radians({self.declination}))) / (cos(radians({self.latitude})) * cos(radians({self.declination}))) = {D}")
        H = math.degrees(math.acos(D)) / 15  # Hour angle in hours
        print(f"Convert hour angle (D) from radians to hours: degrees(acos({D})) / 15 = {H}")
        sunset = 12 + self.timezone - (self.longitude / 15) - (self.eq_of_time / 60)
        print(f"Sunset time calculation: 12 + {self.timezone} - ({self.longitude} / 15) - ({self.eq_of_time} / 60) = {sunset}")
        isya_time = sunset + H
        print(f"Isya time calculation: {sunset} + {H} = {isya_time}")
        return isya_time

    def get_prayer_times(self):
        # Calculate all prayer times
        print("Getting prayer times...")
        dhuhr_time = self.calculate_dhuhr()
        isya_time = self.calculate_isya()
        return dhuhr_time, isya_time

# Input parameters
longitude = "110 49 54.02"
latitude = "07 33 22.00"
timezone = 7
elevation = 100
temperature = 30
pressure = 1010
date = "29 May 1999"
eq_of_time = "2m 33"
declination = "21 41 04.7"
hisab_range = 9

# Initialize the calculator
calculator = PrayerTimesCalculator(longitude, latitude, timezone, elevation, temperature, pressure, date, eq_of_time, declination, hisab_range)
# Get prayer times
dhuhr_time, isya_time = calculator.get_prayer_times()

# Convert decimal time to readable format
def decimal_to_time(decimal_time):
    # Break down the decimal time into hours, minutes, and seconds
    hours = int(decimal_time)
    minutes = int((decimal_time - hours) * 60)
    seconds = (decimal_time - hours - minutes / 60) * 3600
    # Format the time to include hours, minutes, and seconds
    time_str = f"{hours:02d} : {minutes:02d} : {seconds:05.2f}"
    print(f"Converted decimal time {decimal_time} to readable format {time_str}")
    return time_str

# Print prayer times
print(f"Dhuhr time: {decimal_to_time(dhuhr_time)}")
print(f"Isya time: {decimal_to_time(isya_time)}")
