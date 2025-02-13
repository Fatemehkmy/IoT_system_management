from finalproject_Task1 import *


class AdminPanel:

    def __init__(self):
        self.groups = {}
        self.devices={}
        self.username=[]
        self.password= None
        self.status_in_group={}
        self.status_in_device_type=[]
        self.sensor_groups={}
        self.energy_threshold = 400



    #ahsant ahsant kheyli awlii 
    #hamchenin mitonid Password ro too hamin ja bezarid k fght afradi k dastresi drn btonan das bznan beehsh
    #ya yek code khas ghable set_password bezarid k fgth afradi k ramzr ro daran betoonan set_password konan 
    #ama dar kol ahsant 
    
    def set_password(self):
        Syms =['$', '@', '#', '%']
        username= input('Please Enter your username :')
        if username not in self.username:
            self.username.append(username)
        while True:
            new_password = input('Please set a password :')
            if len(new_password.strip()) < 8 :
                print('Your password is weak! Please try again.')
            elif  not any(char.isdigit() for char in new_password):
                print('Password should have at least one numeral')
            elif not any(char.isupper() for char in new_password):
                print('Password should have at least one uppercase letter')
            elif not any(char.islower() for char in new_password):
                print('Password should have at least one lowercase letter')
            elif not any(char in Syms for char in new_password):
                print('Password should have at least one of the symbols $@#')
            else:
                confirm_pass = input('Please confirm your password :')
                if confirm_pass == new_password:
                    self.password = new_password
                    print('You have successfully set your username and password!!')
                    return

                else:
                    print('Entered passwords do not match. Please try again.')



    def create_group(self, group_name):
        if not self.check_info():
            print("Access denied. Can not create group.")
            return

        if group_name not in self.groups:
            self.groups[group_name] = []
            print(f'Group {group_name} is created')

        else:
            print('Your group name has already existed !')


    def add_device_to_group(self, group_name, device):
        if group_name in self.groups:
            self.groups[group_name].append(device)

        else:
            print(f'Group {group_name} does not exist')




    def create_device(self, group_name, device_type, name):
        if not self.check_info():
            print("Access denied. Can not create device.")
            return
        if group_name in self.groups:
            topic = f'home/{group_name}/{device_type}/{name}'
            new_device = Device(topic)
            self.add_device_to_group(group_name, new_device)
            print(f'The new device : {new_device} created !')
        else:
            print(f'Group {group_name} does not exist')





    def create_multiple_devices(self, group_name, device_type, number_of_devices):

        if group_name in self.groups:
            for i in range(1, number_of_devices + 1):
                device_name = f"{device_type}{i}"
                topic = f'home/{group_name}/{device_type}/{device_name.lower()}'
                new_device = Device(topic)
                self.add_device_to_group(group_name, new_device)
            print(f'{number_of_devices} devices were created !')
        else:
            print(f'Group {group_name} does not exist')

    def get_devices_in_groups(self, group_name):
        
        if group_name in self.groups:
            return self.groups[group_name]

        else:
            print(f'Group {group_name} does not exist')
            return []







        #besiar awli ahsant babate check_info 
        #ama check_info ro aval bezarid ta afradi k bare aval code ro mikhonan befahman chie
        #bad estefadasho bebinand
        #ahsant
    def turn_on_all_in_group(self, group_name):

        if not self.check_info():
            print("Access denied.")
            return
        devices = self.groups[group_name]
        for device in devices:
            device.turn_on()
        print(f'All Devices in {group_name} is turned on !')




    def turn_off_all_in_group(self, group_name):
        if not self.check_info():
            print("Access denied.")
            return
        devices = self.groups[group_name]
        for device in devices:
            device.turn_off()
        print(f'All Devices in {group_name} is turned on !')





    def turn_on_all(self):
        if not self.check_info():
            print("Access denied. Can not turn on.")
            return
        for device in self.groups.values():
            device.turn_on()
        print('All Devices are turned on successfully !')




    def turn_off_all(self):
        if not self.check_info():
            print("Access denied. Can not turn off.")
            return
        for device in self.groups.values():
            device.turn_off()
        print('All Devices turned on successfully !')



    def get_status_in_group(self, group_name):
        if not self.check_info():
            print("Access denied. Can not retrieve group status.")
            return
        status_report = []
        devices= self.groups[group_name]
        if group_name in self.groups:
            for device in devices:
                device_status = {
                    'Device_Name': device.name,
                    'Status': device.status
                }
                status_report.append(device_status)




            print(f'The report of devices defined in {group_name}  is as follows:')
            print(f"Group: {group_name}")
            for device_status in status_report:
                print(f" Device Name: {device_status['Device_Name']}, Status: {device_status['Status']}")

        else:
            print(f'Group "{group_name}" does not exist!')



    def get_status_in_device_type(self, device_type):
        if not self.check_info():
            print("Access denied. Can not retrieve device status.")
            return
        print('The report of selected device_type in different groups defined in the house is as follows:')
        for devices in self.groups.values():
            for device in devices:
                if device.device_type == device_type:
                    print(f"Device Name: {device.name}, Status: {device.status}")





    def create_sensor(self, group_name, device_type, name):
        if not self.check_info():
            print("Access denied. Can not create sensor.")
            return
        if group_name in self.groups:
            topic = f'home/{group_name}/{device_type}/{name}'
            new_sensor = Sensor(topic)
            self.add_sensor_to_group(group_name, new_sensor)
            print(f'The new sensor : {new_sensor} created !')
        else:
            print(f'Group {group_name} does not exist')



    def add_sensor_to_group(self, group_name, sensor):
        if group_name in self.groups:
            self.groups[group_name].append(sensor)

        else:
            print(f'Group {group_name} does not exist !')


    #ahsant babate in function
    def create_multiple_sensor(self, group_name, device_type, number_of_sensor):
        if group_name in self.groups:
            for i in range(1, number_of_sensor + 1):
                sensor_name = f" {device_type}{i}"
                topic = f'home/{group_name}/{device_type}/{sensor_name.lower()}'
                new_sensor = Sensor(topic)
                self.add_sensor_to_group(group_name, new_sensor)
            print(f'{number_of_sensor} sensors were created !')
        else:
            print(f'Group {group_name} does not exist !')

    #alan motvaje shdoam ama dar asl sensor ha az hamoon aval active hastan
    #ama inke b in ghazxie fek kardid neshon mide darke kameli az masale peyda krdid
    def active_sensor(self, group_name, device_type):
        if not self.check_info():
            print("Access denied. Can not Add sensor to group.")
            return
        if group_name in self.groups:
            for sensor in self.groups[group_name]:
                if device_type == ' Phototransistors':
                    sensor.turn_on()

                elif device_type == 'hygrometer':
                    sensor.turn_on()
            print(f'The all sensors of type: {device_type} were turned on !')
        else:
            print(f'Group {group_name} does not exist !')

    def deactivate_sensor(self, group_name, device_type):
        if not self.check_info():
            print("Access denied. Can not Add sensor to group.")
            return
        if group_name in self.groups:
            for sensor in self.groups[group_name]:
                if device_type == 'Phototransistors':
                    sensor.turn_off()

                elif device_type == 'hygrometer':
                    sensor.turn_off()
            print(f'The all sensors of type: {device_type} were turned off!')
        else:
            print(f'Group {group_name} does not exist !')




    def check_info(self):
        for i in range(3):
            username= input('Please Enter your username :')
            if username in self.username:
                logging_password = input('Please Enter your password :')
                if logging_password != self.password:
                    print('Your entered password is not correct!')
                else:
                    print('Login successful!')
                    return True

            else:
                print("Username does not exist!")

        print('Your AdminPanel is locked due to too many failed attempts!')
        return False

    #AHSANT AHSANT
    #Badan mitonid ba estefade az matplotlib rasm ham konin energy ro bar asase zaman
    def energy_control(self):
        total_energy=0
        for devices in self.groups.values():
            for device in devices:
                if device.device_type == 'lights' and device.status == 'ON':
                    energy_consumption= device.power_rating * device.hours_on
                    total_energy += energy_consumption
        return total_energy
    #inja mitonid yek bot too telegram besazid va API Token ro bardarid
    #ba estefade az ketabkhoeneye telegram-python-bot ba command bot.send_message b shomareye fard message ersal kone jaye print
    def send_alarm(self):
        total_energy= self.energy_control()
        if total_energy > self.energy_threshold:
            print(f'ALARM! Energy consumption exceeded threshold! Total: {total_energy} watt-hours')
        else:
            print('*** Energy consumption is optimal ! ***')









if __name__=='__main__':
    a=AdminPanel()
    a.set_password()
    a.create_group('garden')
    a.create_group('kitchen')
    a.create_device('garden','lights', 'lamp0')
    a.create_device('kitchen', 'lights', 'lamp0')
    a.create_device('garden', 'waters', 'spray0')
    a.create_multiple_devices('garden', 'lights', 10)
    a.turn_on_all_in_group('garden')
   #a.energy_control()
   #a.send_alarm()
    a.create_sensor('garden', 'hygrometer', 'H1')
    a.create_multiple_sensor('garden','hygrometer',5)
    a.active_sensor('garden', 'hygrometer')
    a.get_status_in_group('garden')
    a.get_status_in_group('kitchen')
   #a.get_status_in_device_type('lights')
   #a.get_status_in_device_type('waters')
   #a.get_status_in_device_type('hygrometer')
