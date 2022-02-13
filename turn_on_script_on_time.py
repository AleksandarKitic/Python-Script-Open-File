import time
from datetime import datetime
import pytz


class TurnOnScript:

    def __init__(self, time_zone, date_time, start_time, end_time):
        self.time_zone = time_zone
        self.date_time = date_time
        self.start_time = start_time
        self.end_time = end_time

    def start_project(self):
        # SETTING TIME VARIABLES
        self.time_zone = pytz.timezone('US/Central')
        self.date_time = datetime.now(self.time_zone).time()
        self.date_time.strftime('%H:%M:%S')
        self.start_time = '09:40:00'
        self.end_time = '09:41:00'
        starting_time = datetime.strptime(self.start_time, '%H:%M:%S').time()
        ending_time = datetime.strptime(self.end_time, '%H:%M:%S').time()
        print(f'Time now: {self.date_time}')
        print('-' * 30)
        print(f'Time starting app: {starting_time}')
        print(f'Time ending app: {ending_time}')
        print('-' * 30)

        # SETTING TIME COUNT FOR STARTING APP
        # while self.date_time != self.start_time:
        while True:
            counting_time = datetime.now(self.time_zone).time()
            current_counting_time = counting_time.strftime('%H:%M:%S')
            print(f'{current_counting_time}')
            time.sleep(1)

            # STARTING APP

            if current_counting_time == self.start_time:
                print('Turning on app..')
                print('Working hours..')
                while True:
                    working_hours = datetime.now(self.time_zone).time()
                    current_working_hours = working_hours.strftime('%H:%M:%S')
                    print(f'{current_working_hours}')
                    time.sleep(1)

                    if current_working_hours == self.end_time:
                        print('Turning off app..')
                        time.sleep(1)
                        exit()


start = TurnOnScript('', '', '', '',)
start.start_project()
