from enum import Enum
import time

class SystemController:
    class ResetOption(Enum):
        SystemReset = 0
        Bootloader = 1

    def __init__(self, serialPort):
        self.serialPort = serialPort

    def Reset(self, option : Enum):
        cmd = "reset({0})".format(1 if option.value == 1 else 0)
        self.serialPort.WriteCommand(cmd)
        # The device will reset in bootloader or system reset
        self.serialPort.Disconnect()

    def GetTickMicroseconds(self):
        cmd = "print(tickus())"
        self.serialPort.WriteCommand(cmd)
        res = self.serialPort.ReadRespone()
        if res.success:
            try:
                return int(res.respone)
            except:
                pass
        return -1
    
    def GetTickMilliseconds(self):
        cmd = "print(tickms())"
        self.serialPort.WriteCommand(cmd)
        res = self.serialPort.ReadRespone()
        if res.success:
            try:
                return int(res.respone)
            except:
                pass
        return -1
    
    def Beep(self, pin:int, frequency:int, duration:int)->bool:
        if frequency < 0 or frequency > 10000:
            raise ValueError("Frequency is within range[0,10000] Hz")
        if duration < 0 or duration > 1000:
            raise ValueError("duration is within range[0,1000] millisecond")
        
        cmd = "beep({0}, {1}, {2})".format(pin, frequency, duration)
        self.serialPort.WriteCommand(cmd)
        res = self.serialPort.ReadRespone()
        return res.success
    
    def Print(self, text: str)->bool:
        cmd = f"print(\"{text}\")"
        self.serialPort.WriteCommand(cmd)
        res = self.serialPort.ReadRespone()
        return res.success
    
    def Println(self, text: str)->bool:
        cmd = f"println(\"{text}\")"
        self.serialPort.WriteCommand(cmd)
        res = self.serialPort.ReadRespone()
        return res.success
    
    def Wait(self, millisecond: int)->bool:
        cmd = f"wait({millisecond})"       
        self.serialPort.WriteCommand(cmd)
        time.sleep(millisecond / 1000)
        res = self.serialPort.ReadRespone()
        return res.success

    






