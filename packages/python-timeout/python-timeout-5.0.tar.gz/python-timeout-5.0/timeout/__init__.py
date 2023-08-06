from time import sleep
from random import random, uniform, randrange
from datetime import datetime, timedelta
from dateutil.parser import parse
from printr import printr

class sleep_timer:
    def __init__(self, hour_to_start_at, hour_to_stop_at):
        if type(hour_to_start_at) == int:
            self.hour_to_start_at = hour_to_start_at
            self.hour_to_stop_at = hour_to_stop_at
        else:
            self.hour_to_start_at = parse(hour_to_start_at).hour
            self.hour_to_stop_at = parse(hour_to_stop_at).hour

        self.random_minute_to_start_at = randrange(0, 59)
        self.random_minute_to_end_at = randrange(0, 59) # If started after start_hour generate a random minute to end at

        self.is_active = False
    
    def during_active_time(self):
        now = datetime.now()
        current_hour = now.hour
        current_minute = now.minute

        # Check within active hours
        if self.hour_to_start_at <= current_hour <= self.hour_to_stop_at:
            if not self.is_active and current_hour == self.hour_to_start_at and self.random_minute_to_start_at == 0:
                self.random_minute_to_start_at = randrange(0, 59)
                self.random_minute_to_end_at = randrange(0, 59)

            # Check after start time with randomised minute to start at
            if current_hour == self.hour_to_start_at and current_minute >= self.random_minute_to_start_at:
                self.is_active = True

            elif self.hour_to_start_at < current_hour < self.hour_to_stop_at:
                self.is_active = True
                if self.random_minute_to_start_at != 0:
                    self.random_minute_to_start_at = 0

            # Check before end time including randomised minute to end at
            elif current_hour == self.hour_to_stop_at and current_minute >= self.random_minute_to_end_at:
                self.is_active = False

        return self.is_active

class random_timeout:
    '''Random timeout between from and to values'''
    def __init__(self, from_seconds=None, to_seconds=None, from_minutes=None, to_minutes=None, from_hours=None, to_hours=None, from_days=None, to_days=None, silent=False):
        if from_seconds is not None:
            if from_seconds == 0:
                minimum = random()
            elif from_seconds > 1:
                minimum = from_seconds - random() # Random float between 0 and 1
            else:
                minimum = from_seconds
            if to_seconds:
                maximum = to_seconds
                if to_seconds > 1:
                    maximum += random()
            else:
                maximum = from_seconds
        elif from_minutes is not None:
            if from_minutes == 0:
                minimum = random()
            else:
                minimum = (from_minutes - random()) * 60 # Random float between 0 and 1
            if to_minutes:
                maximum = (to_minutes + random()) * 60
            else:
                maximum = from_minutes + random()
        elif from_hours is not None:
            if from_hours == 0:
                minimum = random()
            else:
                minimum = (from_hours - random()) * 3600 # Random float between 0 and 1
            if to_hours:
                maximum = (to_hours + random()) * 3600
            else:
                maximum = from_hours + random()
        elif from_days is not None:
            if from_days == 0:
                minimum = random()
            else:
                minimum = (from_days - random()) * 86400 # Random float between 0 and 1
            if to_days:
                maximum = (to_days + random()) * 86400
            else:
                maximum = from_days + random()
                
        timeout_in_seconds = uniform(minimum, maximum) # Random float between minimum and maximum
        if not silent:
            if timeout_in_seconds < 60:
                printr('Sleeping', timeout_in_seconds, 'seconds', level='debug')
            elif timeout_in_seconds > 86400:
                timeout_in_days = round(timeout_in_seconds / 86400) # Convert sleep time in seconds to days
                til = datetime.now() + timedelta(seconds=timeout_in_seconds)
                til = til.strftime('%A, %B %e')
                if timeout_in_days == 1:
                    printr('Sleeping 1 day until', til)
                else:
                    printr('Sleeping', timeout_in_days, 'days until', til)
            elif timeout_in_seconds > 3600:
                timeout_in_hours = round(timeout_in_seconds / 3600) # Convert sleep time in seconds to hours
                til = datetime.now() + timedelta(seconds=timeout_in_seconds)
                til = til.strftime('%H:%M')
                if timeout_in_hours == 1:
                    printr('Sleeping 1 hour until', til)
                else:
                    printr('Sleeping', timeout_in_hours, 'hours until', til)
            elif timeout_in_seconds >= 60:
                timeout_in_minutes = round(timeout_in_seconds / 60) # Convert sleep time in seconds to minutes
                til = datetime.now() + timedelta(seconds=timeout_in_seconds)
                til = til.strftime('%H:%M')
                if timeout_in_minutes == 1:
                    printr('Sleeping 1 minute until', til)
                else:
                    printr('Sleeping', timeout_in_minutes, 'minutes until', til)

        sleep(timeout_in_seconds)

class sleep_for:
    '''Sleep amount of time in minutes, hours or days and prints when it will continue'''
    def __init__(self, seconds=None, minutes=None, hours=None, days=None, silent=False):
        if seconds:
            timeout_in_seconds = seconds
        if minutes:
            timeout_in_seconds = minutes * 60
        elif hours:
            timeout_in_seconds = hours * 3600
        elif days:
            timeout_in_seconds = days * 86400

        if not silent:
            if timeout_in_seconds < 60:
                printr('Sleeping', timeout_in_seconds, 'seconds', level='debug')
            elif timeout_in_seconds > 86400:
                timeout_in_days = round(timeout_in_seconds / 86400) # Convert sleep time in seconds to days
                til = datetime.now() + timedelta(seconds=timeout_in_seconds)
                til = til.strftime('%A, %B %e')
                if timeout_in_days == 1:
                    printr('Sleeping 1 day until', til)
                else:
                    printr('Sleeping', timeout_in_days, 'days until', til)
            elif timeout_in_seconds > 3600:
                timeout_in_hours = round(timeout_in_seconds / 3600) # Convert sleep time in seconds to hours
                til = datetime.now() + timedelta(seconds=timeout_in_seconds)
                til = til.strftime('%H:%M')
                if timeout_in_hours == 1:
                    printr('Sleeping 1 hour until', til)
                else:
                    printr('Sleeping', timeout_in_hours, 'hours until', til)
            elif timeout_in_seconds >= 60:
                timeout_in_minutes = round(timeout_in_seconds / 60) # Convert sleep time in seconds to minutes
                til = datetime.now() + timedelta(seconds=timeout_in_seconds)
                til = til.strftime('%H:%M')
                if timeout_in_minutes == 1:
                    printr('Sleeping 1 minute until', til)
                else:
                    printr('Sleeping', timeout_in_minutes, 'minutes until', til)

        sleep(timeout_in_seconds)