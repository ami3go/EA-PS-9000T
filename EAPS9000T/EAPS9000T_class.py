import time

import pyvisa # PyVisa info @ http://PyVisa.readthedocs.io/en/stable/
import serial
import serial.tools.list_ports


def get_com_port_by_keyword(keyword):
    """
    Returns the COM port number (e.g., 'COM3') for a device
    whose description contains the given keyword.
    Returns None if no matching device is found.
    """
    ports = serial.tools.list_ports.comports()
    for port in ports:
        # print(port)
        # print(port.description.lower())
        # Check if the keyword is present in the port's description
        if keyword.lower() in port.description.lower(): # Using .lower() for case-insensitive search
            return port.device
    return None

def range_check(val, min, max, val_name):
    if val > max:
        print(f"Wrong {val_name}: {val}. Max value should be less then {max}")
        val = max
    if val < min:
        print(f"Wrong {val_name}: {val}. Should be >= {min}")
        val = min
    return val


class EaPs9000T:
    def __init__(self):
        # Commands Subsystem
        # this is the list of Subsystem commands
        # super(communicator, self).__init__(port="COM10",baudrate=115200, timeout=0.1)
        # print("communicator init")
        self.cmd = storage()
        self.ser = None
        self._retry_cnt = 10
        com_port_list = [comport.device for comport in serial.tools.list_ports.comports()]
        com_port = get_com_port_by_keyword("PS 9000 T")
        if com_port not in com_port_list:
            print("COM port is not found")
            print("Please ensure that USB is connected")
            print(f"Please check COM port Number. Currently it is {com_port} ")
            print(f'Founded COM ports:{com_port_list}')
        else:
            self.ser = serial.Serial(
                port=com_port,
                baudrate=115200,
                timeout=0.1
            )
            if not self.ser.isOpen:
                self.ser.open()
            txt = '*IDN?'

            read_back = self.query(txt)
            print(f"Connected to: {read_back}")
            print("Turn remote mode On")
            self.remote_on()

    @property
    def retry_cnt(self):
        return self._retry_cnt

    @retry_cnt.setter
    def retry_cnt(self, value):
        value = int(value)
        self._retry_cnt = value


    def send(self, txt):
        # will put sending command here
        txt = f'{txt}\r\n'
        # print(f'Sending: {txt}')
        for i in range(self._retry_cnt):
            try:
                self.ser.write(txt.encode())
            except Exception as e:
                print(f"query[{i}]: {txt}, Error: {e}")
                time.sleep(2)

    def query(self, cmd_srt):
        txt = f'{cmd_srt}\r\n'
        for i in range(self._retry_cnt):
            try:
                self.ser.reset_input_buffer()
                self.ser.write(txt.encode())
                # print(f'Query: {txt}')
                return_val = self.ser.readline().decode()
                return return_val
            except Exception as e:
                print(f"query[{i}]: {txt}, Reply: Error: {e}")
                time.sleep(2)

    def close(self):
        self.remote_off()
        self.ser.close()
        self.ser = None
        self.cmd = None

    def set_voltage(self, val):
        self.send(self.cmd.source.voltage.val(val))

    def set_current(self, val):
        self.send(self.cmd.source.current.val(val))

    def output_on(self):
        self.send(self.cmd.output.on())

    def output_off(self):
        self.send(self.cmd.output.off())

    def remote_on(self):
        self.send(self.cmd.system.lock.on())

    def remote_off(self):
        self.send(self.cmd.system.lock.off())

    def get_errors(self):
        return self.query(self.cmd.system.error_all.req())

    def set_ovp(self, val):
        self.send(self.cmd.source.voltage.ovp.val(val))

    def set_ovc(self, val):
        self.send(self.cmd.source.current.ovc.val(val))

# class ESPS9000T:


# service classes

class req3:
    def __init__(self, prefix):
        self.prefix = prefix
        self.cmd = self.prefix

    def req(self):
        return self.cmd + "?"

class str3:
    def __init__(self, prefix):
        self.prefix = prefix
        self.cmd = self.prefix

    def str(self, ):
        return self.cmd

class dig_param3:
    def __init__(self, prefix, min, max):
        self.prefix = prefix
        self.cmd = self.prefix
        self.max = max
        self.min = min
        self.ending = ""

    def val(self, count=0):
        count = range_check(count, self.min, self.max, "MAX count")
        txt = f'{self.cmd} {count}{self.ending}'
        return txt

# add ending ON and OFF to the ed of string
class str_on_off:
    def __init__(self, prefix):
        self.prefix = prefix
        self.cmd = self.prefix

    def on(self):
        return self.cmd + " ON"

    def off(self):
        return self.cmd + " OFF"

class speed:
    def __init__(self, prefix):
        self.prefix = prefix
        self.cmd = self.prefix

    def fast(self):
        return self.cmd + " FAST"

    def slow(self):
        return self.cmd + " SLOW"


class range_resolution:
    def __init__(self, prefix, min, max):
        self.prefix = prefix
        self.cmd = self.prefix
        self.max = max
        self.min = min

    def val(self, count=0):
        count = range_check(count, self.min, self.max, "MAX count")
        txt = f'{self.cmd} {count}'
        return txt


# command storage class.
# this is constructor to make VISA command in easy style

class storage:
        def __init__(self):
            self.cmd = None
            self.prefix = None
            # super(communicator, self).__init__()
            # super(storage,self).__init__()
            # communicator.init(self, "COM10")
            # this is the list of Subsystem commands
            # self.calculate = calculate()

            # self.configure = configure()
            # self.data = data()
            # self.display = display()
            self.measure = measure()
            # self.sense = sense()
            # self.input = input_cmd()
            # self.sample = sample()
            self.system = system()
            self.output = str_on_off("OUTP")
            self.source = source()
            self.idn = req3("*IDN") # Returns	the	device	identification	string,	which	contains	following	information,	separated	by	commas:
            self.cls = str3("CLS") # Clears the error queue, the status byte (STB) and all bits in the Event Status Register (ESR), except for bit 0.
            self.reset = str3("*RST")
            self.read_status = req3("*STB") # Reads the STatus Byte register


class configure(req3):
    # availanle commands for CONFigure
    # * CONFigure?
    # * CONFigure:CURRent:AC
    # * CONFigure:CURRent:DC
    # * CONFigure:DIGital:BYTE
    # * CONFigure:FREQuency
    # * CONFigure:FRESistance
    # * CONFigure:PERiod
    # * CONFigure:RESistance
    # * CONFigure:TEMPerature
    # * CONFigure:TOTalize
    # * CONFigure:VOLTage:AC
    # * CONFigure:VOLTage:DC
    def __init__(self):
        print("INIT CONFIGURE")
        # super(configure, self).__init__()
        self.prefix = "CONFigure"
        self.cmd = "CONFigure"
        self.current = current(self.prefix)
        self.voltage = voltage(self.prefix)
        # self.frequency = frequency(self.prefix)
        # self.period = period(self.prefix)
        # self.temperature = temperature(self.prefix)
        # self.resistance = resistance(self.prefix)
        # self.fresistance = fresistance(self.prefix)
        # self.totalize = totalize(self.prefix)



class voltage(dig_param3, req3):
    def __init__(self, prefix):
        self.min = 0
        self.max = 500
        self.prefix = prefix + ":" + "VOLTage"
        self.cmd = self.prefix
        self.ending = "V"
        self.ovp = Protection(self.prefix, 0, 500)


class current(dig_param3, req3):
    def __init__(self, prefix):
        self.min = 0
        self.max = 5
        self.prefix = prefix + ":" + "CURrent"
        self.cmd = self.prefix
        self.ending = "A"
        self.ovc = Protection(self.prefix, 0, 5)


# class ac(str3,req3):
#     def __init__(self, prefix):
#         self.prefix = prefix
#         self.cmd = self.prefix + ":" + "AC"
#         self.prefix = self.cmd



# class dc(str3,req3):
#     def __init__(self, prefix):
#         self.prefix = prefix
#         self.cmd = self.prefix + ":" + "DC"
#         self.prefix = self.cmd


class source:
    # command list :
    # SOURce < n >: VOLTage
    # SOUR1: VOLT?
    # SOURce < n >: OUTCURRent
    # SOUR1: OUTCURR?
    # SOURce < n >: RANGe < NR1 >

    def __init__(self):
        # print("INIT Measure")
        self.cmd = "SOUR"
        self.prefix = "SOUR"
        self.current = current(self.prefix)
        self.voltage = voltage(self.prefix)
        self.power = spwr(self.prefix)

# class svoltage(voltage, dig_param3):
#     def __init__(self, prefix):
#         self.min = 0
#         self.max = 500
#         self.ending = "V"
#         self.prefix = prefix + ":" + "VOLT"
#         self.cmd = self.prefix
#
# class scurrent(current, dig_param3):
#     def __init__(self, prefix):
#         self.min = 0
#         self.max = 5
#         self.ending = "A"
#         self.prefix = prefix + ":" + "CURRENT"
#         self.cmd = self.prefix


class Protection(req3, dig_param3):
    def __init__(self, prefix, min_val, max_val):
        self.min = min_val
        self.max = max_val
        self.ending = ""
        self.prefix = prefix + ":" + "PROTection"
        self.cmd = self.prefix


class spwr(current, dig_param3):
    def __init__(self, prefix):
        self.min = 0
        self.max = 3000
        self.prefix = prefix + ":" + "POWER"
        self.cmd = self.prefix

class sres(current, dig_param3):
    def __init__(self, prefix):
        self.min = 0
        self.max = 10000
        self.prefix = prefix + ":" + "RESISTANCE"
        self.cmd = self.prefix

class system:
    def __init__(self):
        self.cmd = "SYST"
        self.prefix = "SYST"
        self.lock = str_on_off(self.prefix + ":LOCK")
        self.error = req3(self.prefix + ":ERR")
        self.error_all = req3(self.prefix + ":ERR:ALL")
        # self.config = syst_conf(self.prefix)

class syst_conf:
    def __init__(self):
        # print("INIT Measure")
        self.cmd = "CONF"
        self.prefix = "CONF"
        self.controller = controller(self.prefix)

class controller:
    def __init__(self):
        # print("INIT Measure")
        self.cmd = "CONT"
        self.prefix = self.prefix + ":"+"CONT"
        self.speed = speed(self.prefix)

class measure:
    # command list :
    # SOURce < n >: VOLTage
    # SOUR1: VOLT?
    # SOURce < n >: OUTCURRent
    # SOUR1: OUTCURR?
    # SOURce < n >: RANGe < NR1 >

    def __init__(self):
        # print("INIT Measure")
        self.cmd = "MEASURE"
        self.prefix = "MEASURE"
        self.current = current(self.prefix)
        self.voltage = voltage(self.prefix)
        self.power = spwr(self.prefix)


if __name__ == '__main__':
   ps = EaPs9000T()
   ps.remote_on()
   ps.set_voltage(10)
   ps.output_on()

   time.sleep(3)
   ps.output_off()
   ps.close()
   #  cmd = storage()
   #  # print(cmd.configure.current.dc.str())
   #  # print(cmd.measure.current.dc.req())
   #  dev = com_interface()
   #  dev.init("COM8")
   #  dev.send(cmd.system.lock.on())
   #  # print(dev.query("*IDN?"))
   #  # dev.send(cmd.reset.str())
   #
   # # Preset
   #  interval = 0.02
   #  pulse_width = 0.001
   #  dc_time = 5
   #  v_dc = 30
   #  v_peak = 200
   #  i_lim = 2
   #
   #  dev.send(cmd.source.current.val(i_lim))
   #  time.sleep(0.1)
   #  dev.send("SOUR:VOLT:CONT:SPE FAST")
   #  time.sleep(0.1)
   #  dev.send(cmd.output.on())
   #  # DC bias
   #  dev.send(cmd.source.voltage.val(v_dc))
   #  time.sleep(dc_time)
   #
   #  # High Voltage pulse
   #  dev.send(cmd.source.voltage.val(v_peak))
   #  time.sleep(pulse_width)
   #  dev.send(cmd.source.voltage.val(v_dc))
   #
   #  time.sleep(dc_time)
   #  dev.send(cmd.output.off())
   #
   #  dev.send(cmd.system.lock.off())
   cmd = storage()
   print(cmd.source.voltage.req())
   print(cmd.source.voltage.val(10))
   print(cmd.source.current.ovc.val(5))
   print(cmd.source.voltage.ovp.val(500))

