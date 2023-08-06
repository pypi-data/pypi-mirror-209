import os
import sys
import threading
import time
import copy
import serial
import serial.tools.list_ports
from VSautomatic.my_serial import SigmaSerial
from VSautomatic.MyCamera import CameraCapture
from VSautomatic.ReSTTerminal import restterminal
from VSautomatic.RedRatHubS import RedRatHubCmdSetUp
from VSautomatic.MyRedRat import DEV_REDRAT
from .deco import keyword

log_file_path = os.path.realpath(os.path.dirname(os.path.dirname(__file__)) + '//VSautomatic')
Auth_Token = log_file_path + '\Auth_Token.txt'

class MyTools(object):

    def __init__(self):
        self.my_serial = None
        self.my_camera = None
        self.my_rest = None
        self.RedRatS = None
        self.RedRatC = None

    # COM-Serial-Start
    def serial_connect(self, portname):
        '''
        Example:
        | *** Settings *** |
        | Documentation    | COM示例 |
        | Suite Setup      | Open Connection And Log In |
        | Library          | VSautomatic |
        | Library          | Process  |
        | *** Test Cases ***  |
        | SendCommand      |
        |                  | Serial Writer | ifconfig \\n |
        |                  | Sleep         | 3   |
        |                  | ${a}          | Serial Reader |
        |                  | Log           | ${a} |
        |                  | Serial Disconnect |
        | *** Keywords *** |
        | Open Connection And Log In |
        |                  | Serial Connect | COM3 |
        '''
        if self.my_serial is None:
            self.my_serial = SigmaSerial()
        try:
            self.my_serial.open(portname)
            if self.my_serial.isOpen():
                self.alive = True
                # self.thread_read = threading.Thread(target=self.serial_reader)
                # self.thread_read.setDaemon(True)
                # self.thread_read.start()
                return True
            else:
                return False
        except Exception as e:
            return False

    def serial_reader(self):
        '''
        Example:

        '''
        try:
            data = self.my_serial.readlines()
            if len(data) > 1:
                print(data)
                return data
                # logfile = open('.\\Logs\\DUT_log.txt', 'a+')
                # logfile.write(data.decode('utf-8'))
                # logfile.flush()
                # logfile.close()
        except Exception as e:
            print(e)

    def serial_writer(self, command):
        self.my_serial.writes(command)
        
    def serial_disconnect(self):
        if not self.my_serial is None:
            self.alive = False
            if self.my_serial.isOpen():
                self.my_serial.close()
    
    # COM-Serial-End
    # ====================================================================================================================================

    # Rest-Start
    def rest_pair(self,ip):
        '''
        Example:
        | *** Settings *** |
        | Documentation    |  Pair示例 |
        | Suite Setup      |  Open Connection And Log In |
        | Library          |  VSautomatic |
        | *** Test Cases *** |
        | Pair Test |
        |    FOR    |  ${index}     |  IN RANGE                 |  1  |  10 |
        |           |    LOG        |  ${index}                 |
        |           |    Rest Send  |  put current_input HDMI-1 |
        |           |    Rest Send  |  put current_input HDMI-2 |
        |           |    Rest Send  |  put current_input HDMI-3 |
        |    END    |
        | *** Keywords *** |
        | Open Connection And Log In |
        |                            | Rest Pair  |  10.86.79.98 |
        '''
        self.my_rest = restterminal(ip)
        self.auth_token = self.my_rest.sshpair()
        fw = open(Auth_Token, "w")
        fw.write(self.auth_token)
        fw.close()

    def rest_send(self,command):
        fr = open(Auth_Token, "r")
        self.read_auth_token = fr.readline().strip('\n')
        fr.close()
        if self.my_rest is None:
            self.my_rest = restterminal()

        self.my_rest.read_dictionary()
        restValue = self.my_rest.parse_command(command, self.read_auth_token)
        print('restValue:{}'.format(restValue))
        time.sleep(3)
        self.my_rest.parse_command("restlog", self.read_auth_token)

    # Rest-End
    # ====================================================================================================================================

    # Camera-Start
    def camera_open(self):
        '''
        Example:
        | *** Settings *** |
        | Documentation    | Camera示例 |
        | Suite Setup      | Open Connection And Log In |
        | Library          | VSautomatic |
        | Library          | Process |
        | *** Test Cases *** |
        | Camera Test        |
        |                    | Camera ImageCapture |   test1 |    3 |
        |                    | Camera VideoCapture |   testvideo |    10 |
        |                    | Camera Stop |
        | *** Keywords *** |
        | Open Connection And Log In |
        |                  | Camera Open |
        '''
        if self.my_camera is None:
            self.my_camera = CameraCapture()
        try:
            self.my_camera.open()
            if self.my_camera.isOpen():
                self.alive = True
                # self.thread_read = threading.Thread(target=self.serial_reader)
                # self.thread_read.setDaemon(True)
                # self.thread_read.start()
                return True
            else:
                return False
        except Exception as e:
            return False
            
    def camera_imageCapture(self,picName,frameNum):
        self.my_camera.imageCapture(picName,frameNum)

    def camera_videoCapture(self,vidName,duration):
        self.my_camera.videoCapture(vidName,duration)

    def camera_closed(self):
        if not self.my_camera is None:
            self.alive = False
            if self.my_camera.isOpen():
                self.my_camera.close()

    # Camera-End
    # ====================================================================================================================================

    # RedRat_Start
    '''
    Example:
    | *** Settings *** |
    | Documentation    | RedRat示例 |
    | Suite Setup      | Launch ReRat Server and Client |
    | Suite Teardown   | KIll Server and Client |
    | Library          | VSautomatic |
    | *** Test Cases *** |
    | RedRat Test        |
    |                    | RedRat Client Send  |  Menu   | 2 |
    |                    | Camera ImageCapture |   Menuup |   10 |
    |                    | RedRat Client Send  |  Home  |  2 |
    |                    | Camera VideoCapture |    Menuvideo  |  3 |
    | *** Keywords *** |
    | Launch ReRat Server and Client |
    |                    | RedRat Run Server |   Vizio_IR |
    |                    | Sleep             |  10 |
    |                    | RedRat Client     |  10.86.79.145  |  Jason_RedRat  |  Vizio_IR |
    |                    | Camera Open       |
    |                    | Sleep             |  3 |
    | KIll Server and Client |
    |                    | RedRat Kill Server |
    |                    | Camera Stop | 
    '''
    def RedRat_Run_Server(self,RedRatdate):
        self.RedRatS = RedRatHubCmdSetUp(RedRatdate)
        self.RedRatS.run()
        
    def RedRat_Kill_Server(self):
        self.RedRatS.kill()

    def RedRat_Client(self,test_pc_ip,redRat_Name,redRatDataset):
        self.RedRatC = DEV_REDRAT(test_pc_ip,redRat_Name,redRatDataset)

    def RedRat_Client_Send(self,IRMessage,PauseTimer):
        self.RedRatC.IR_GEN(IRMessage,int(PauseTimer))

    # RedRat_End
    # ====================================================================================================================================