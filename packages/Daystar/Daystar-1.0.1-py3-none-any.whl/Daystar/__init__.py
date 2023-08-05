from Solarflare.solarflare import *
import datetime


def to_islamic(year):
  return (year - 622) * 1.03


def to_islamic_solar(year):
  return (to_islamic(year) / 34) - 1429


def gregorian_to_hindu_true_solar(lat, long, date=datetime.datetime.now()):
  # Get the current Gregorian date
  sun_longitude = ecliptical_longitude(sunrise(lat, long, date))
  gregorian_date = datetime.date.today()
  # Get the Sun's longitude at sunrise on January 1st
  sun_longitude_jan_1 = 280.4588  # This is an approximate value
  # Calculate the Hindu true solar date
  hindu_true_solar_date = gregorian_date + datetime.timedelta(
    days=(sun_longitude / 360) - (sun_longitude_jan_1 / 360))
  # Return the Hindu true solar date
  return hindu_true_solar_date


class Daystar:

  def __init__(self, lat, long):
    self.lat = lat
    self.long = long

  def risetime(self, date=datetime.datetime.now()):
    return sunrise(self.lat, self.long, date)

  def settime(self, date=datetime.datetime.now()):
    return sunset(self.lat, self.long, date)

  def solarnoon(self, date=datetime.datetime.now()):
    return fromJulian(solar_transit(self.long, date))

  def hrangle(self, date=datetime.datetime.now()):
    return hour_angle(self.long, date)

  def coordinates(self, date=datetime.datetime.now()):
    return {"dec": declination(date), "ra": right_ascension(date)}

  def mean(self, date=datetime.datetime.now()):
    return mean_anomaly(date)

  def true(self, date=datetime.datetime.now()):
    return true_anomaly(date)

  def ceq(self, date=datetime.datetime.now()):
    return equation(date)

  def solar_julian(self, date=datetime.datetime.now()):
    return {
      "rise": julian_date(sunrise(self.lat, self.long, date)),
      "set": julian_date(sunset(self.lat, self.long, date))
    }

  def alt(self, date=datetime.datetime.now()):
    return altitude(self.lat, self.long, date)

  def azi(self, date=datetime.datetime.now()):
    return azimuth(self.lat, self.long, date)

  def nadir(self, date=datetime.datetime.now()):
    return fromJulian(solar_transit(self.long, date) - 0.5)

  def long(self, date=datetime.datetime.now()):
    return ecliptical_longitude(date)

  def solar_seasons(self, date=datetime.datetime.now()):
    return {
      "spring": spring(),
      "summer": summer(),
      "fall": autumn(),
      "winter": winter(),
    }
