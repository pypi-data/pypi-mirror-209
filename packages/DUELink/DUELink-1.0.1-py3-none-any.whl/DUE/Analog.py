from DUE.SerialInterface import SerialInterface

class AnalogController:
    def __init__(self, serialPort:SerialInterface):
        self.serialPort = serialPort
        self.Fixed_Frequency = 50

    def Read(self, pin):

        if pin < 0 or pin >= self.serialPort.DeviceConfig.MaxPinAnalog:
            raise ValueError("Invalid pin")

        cmd = "print(aread({0}))".format(str(pin))

        self.serialPort.WriteCommand(cmd)

        res = self.serialPort.ReadRespone()

        if res.success:
            try:
                return int(res.respone)
            except:
                pass

        return -1
    
    def Write(self, pin, duty_cycle):
        if pin < 0 or (pin >= self.serialPort.DeviceConfig.MaxPinIO): # Led
            raise ValueError('Invalid pin')

        if duty_cycle < 0 or duty_cycle > 1000:
            raise ValueError('Duty cycle must be in the range 0..1000')

        cmd = f'awrite({pin}, {duty_cycle})'
        self.serialPort.WriteCommand(cmd)

        res = self.serialPort.ReadRespone()
        if res.success:
            return True

        return False
