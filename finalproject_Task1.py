#A code for a Device that manages the light exposure and amount of water required for apartment flowers
'''
APM:

Very good ! 


'''
import time
import numpy as np
from datetime import datetime

class Device:
    def __init__(self, topic, mqtt_broker='local_host', port=1883):
        self.topic= topic
        self.topic_list=self.topic.split('/')
        self.group=self.topic_list[1]
        self.device_type=self.topic_list[2]
        self.name=self.topic_list[3]
        self.status= 'off'
        self.port= port
        self.mqtt_broker= mqtt_broker
        self.lights_status=[]
        self.waters_status =[]
        #self.connect_mqtt()
        #self.setup_gpio()

    def setup_gpio(self):
        if self.device_type == 'lights':
            pass
            GPIO.setup(17, GPIO.OUT)

        elif self.device_type == 'waters':
            pass
            GPIO.setup(44, GPIO.OUT)

    def turn_on(self):
        self.status = 'on'
        #self.send_command('TURN_ON')
        if self.device_type == 'lights':
            #GPIO.output(17, GPIO.HIGH)
            print(f'{self.name} was turned on successfully!')
            self.lights_status.append(f'{self.name} : ON')

        elif self.device_type == 'waters':
            #GPIO.output(44, GPIO.HIGH)
            print(f'{self.name} was turned on successfully!')
            self.waters_status.append(f'{self.name} : ON')


    def turn_off(self):
        self.status = 'off'
        #self.send_command('TURN_OFF')
        if self.device_type == 'lights':
            #GPIO.output(17, GPIO.LOW)
            print(f'{self.name} was turned off successfully!')
            self.lights_status.append(f'{self.name} : OFF')

        elif self.device_type == 'waters':
            #GPIO.output(44, GPIO.LOW)
            print(f'{self.name} was turned off successfully!')
            self.waters_status.append(f'{self.name} : OFF')

    def controlling_light_time(self):
        if self.device_type == 'lights':
            self.start_time= datetime.strptime("06:00", "%H:%M").time()
            self.end_time= datetime.strptime("18:00", "%H:%M").time()

            current_time = datetime.now().time()
            if self.start_time <= current_time < self.end_time:
                self.turn_on()
                print(f'turn on the lights for flowers!')

            else:
                self.turn_off()
                print(f'turn off the lights for flowers!')


    def humidity_check(self):
        if self.device_type == 'waters':
            humidity_value= np.random.uniform(0,1)
            if  0.4 <= humidity_value < 0.6:
                print(f'The percentage of moisture is: {humidity_value:.2%} ')
                print(f'The moisture of soil is enough now!')

            elif humidity_value < 0.4:
                print(f'The percentage of moisture is: {humidity_value:.2%} ')
                print(f'The moisture of soil is low!')
                self.turn_on()

            elif humidity_value > 0.6:
                print(f'The percentage of moisture is: {humidity_value}')
                print(f'The moisture of soil is high!')
                self.turn_off()

    def get_status(self):
        if self.device_type == 'lights':
            print('The history of lights status is:')
            for status in self.lights_status:
                print(status)
        elif self.device_type == 'waters':
            print('The history of waters status is:')
            for status in self.waters_status:
                print(status)






if __name__=='__main__':
    a =Device('home/garden/lights/lamp1')
    b=Device('home/garden/waters/spray1')
    print(a.group)
    print(b.group)
    print(a.name)
    print(b.name)
    a.turn_on()
    b.turn_off()
    b.humidity_check()
    a.controlling_light_time()
    a.get_status()
    b.get_status()
