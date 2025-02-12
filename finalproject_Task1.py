#A code for a Device that manages the light's exposure and amount of water required for apartment flowers
import time
import numpy as np
from datetime import datetime

#***
#apm: ahsant 
#ama sensor chizi bename Turn on va turn off nadare
#fagaht yek tabe dare ke read_sensor konid
#oon Device has k turn on turn off dare

class Sensor:
    def __init__(self, topic, pin=100):
        self.topic = topic
        self.topic_list = self.topic.split('/')
        self.group = self.topic_list[1]
        self.device_type = self.topic_list[2]
        self.name = self.topic_list[3]
        self.status= 'OFF'
        self.current_value = 0
        self.current_time = 0
        self.start_time = 0
        self.end_time = 0
        self.pin = pin
        self.report_sensor_status=[]

    def __str__(self):
        return f'Group_Name: {self.group}, Device_Type: {self.device_type} , Device_Name : {self.name}'


    def read_sensor(self):
        if self.device_type == 'lights':
            self.start_time = datetime.strptime("06:00", "%H:%M").time()
            self.end_time = datetime.strptime("18:00", "%H:%M").time()
            self.current_time = datetime.now().time()
            return self.current_time

        elif self.device_type == 'waters':
            self.current_value = np.random.uniform(0, 1)
            return self.current_value

    def turn_on(self):
        self.status = 'ON'
        #self.send_command('TURN_ON')
        if self.device_type == 'Phototransistors':
            #GPIO.output(56, GPIO.HIGH)
            print(f'{self.name} was turned on successfully!')
            self.report_sensor_status.append(f'{self.name} : ON')

        elif self.device_type == 'hygrometer':
            #GPIO.output(39, GPIO.HIGH)
            print(f'{self.name} was turned on successfully!')
            self.report_sensor_status.append(f'{self.name} : ON')



    def turn_off(self):
        self.status = 'OFF'
        #self.send_command('TURN_OFF')
        if self.device_type == 'Phototransistors':
            #GPIO.output(56, GPIO.LOW)
            print(f'{self.name} was turned off successfully!')
            self.report_sensor_status.append(f'{self.name} : OFF')

        elif self.device_type== 'hygrometer':
            #GPIO.output(39, GPIO.LOW)
            print(f'{self.name} was turned off successfully!')
            self.report_sensor_status.append(f'{self.name} : OFF')



class Device(Sensor):
    def __init__(self, topic, mqtt_broker='local_host', port=1883, status = 'OFF', power_rating=0):
        super().__init__(topic)
        self.status= status
        self.power_rating = power_rating
        self.hours_on = 0
        self.start_time = 0
        self.port= port
        self.mqtt_broker= mqtt_broker
        self.lights_status=[]
        self.waters_status =[]
        #self.connect_mqtt()
        #self.setup_gpio()

    def __str__(self):
        parent_str = super().__str__()
        return f'{parent_str}, Status: {self.status}'

    def __repr__(self):
        return self.__str__()

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
            self.start_time = time.time()
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
            total_time = time.time() - self.start_time
            self.hours_on += total_time / 3600
            self.start_time = None
            #GPIO.output(17, GPIO.LOW)
            print(f'{self.name} was turned off successfully!')
            self.lights_status.append(f'{self.name} : OFF')

        elif self.device_type== 'waters':
            #GPIO.output(44, GPIO.LOW)
            print(f'{self.name} was turned off successfully!')
            self.waters_status.append(f'{self.name} : OFF')

    def controlling_light_time(self):
        if self.device_type == 'lights':

            if self.start_time <= self.current_time < self.end_time:
                self.turn_on()
                print(f'turn on the lights for flowers!')

            else:
                self.turn_off()
                print(f'turn off the lights for flowers!')


    def humidity_check(self):
        if self.device_type == 'waters':
            self.read_sensor()

            if  0.4 <= self.current_value < 0.6:
                print(f'The percentage of moisture is: {self.current_value:.2%} ')
                print(f'The moisture of soil is enough now!')

            elif self.current_value < 0.4:
                print(f'The percentage of moisture is: {self.current_value:.2%} ')
                print(f'The moisture of soil is low!')
                self.turn_on()

            elif self.current_value > 0.6:
                print(f'The percentage of moisture is: {self.current_value: .2%}')
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
        elif self.device_type == 'Phototransistors':
            print('The history of Phototransistors status is:')
            for status in self.report_sensor_status:
                print(status)
        elif self.device_type == 'hygrometer':
            print('The history of hygrometers status is:')
            for status in self.report_sensor_status:
                print(status)







if __name__=='__main__':
    a =Device('home/garden/lights/lamp1')
    b=Device('home/garden/waters/spray1')
    #print(a.group)
    #print(b.group)
    #print(a.name)
    #print(b.name)
    c = Sensor('home/garden/Phototransistors/P1')
    d = Sensor('home/garden/hygrometer/H1')
    #print(c.group)
    #print(d.group)
    #print(c.name)
    #print(d.name)
    c.read_sensor()
    d.read_sensor()
    a.turn_on()
    b.turn_off()
    b.humidity_check()
    a.controlling_light_time()
    a.get_status()
    b.get_status()
    c.turn_on()
    d.turn_off()



