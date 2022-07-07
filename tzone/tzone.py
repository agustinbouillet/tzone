from datetime import datetime
import pytz
import locale

class TZone:
    DATETIME_FORMAT_ISO_TSEP = '%Y-%m-%dT%H:%M:%S'
    DATETIME_FORMAT_ISO = '%Y-%m-%d %H:%M:%S'
  
    def __init__(self, timezone: str='America/Buenos_Aires', lc: str='es_es.UTF-8'):
        locale.setlocale(locale.LC_ALL, lc)
        self.tz = pytz.timezone(timezone)
        self.date = datetime.now(self.tz)
        self.date_time = self.date.strftime(self.DATETIME_FORMAT_ISO_TSEP)

    def __str__(self) -> str:
        return self.date_time

    def datetime_now(self):
        return self.date
      
    def get_datetime(self) -> dict:
      """Define la fecha y hora en que se crea la respuesta
      """
      return {
          'date': self.date_time,
          'day': self.date.day,
          'month': self.date.month,
          'year': self.date.year,
          'hour': self.date.hour,
          'minutes': self.date.minute,
          'seconds': self.date.second,
          'month_name': self.date.strftime('%B'),      
          'day_name': self.date.strftime('%A')     
      }


if __name__ == '__main__':
  dt = TZone() 
  breakpoint()