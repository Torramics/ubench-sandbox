import pyvisa
import atexit

class Agilent34461A:
    def __init__(self, address=None, logger=None):
        self.address = address
        self.logger = logger
        self.rm = pyvisa.ResourceManager()
        self.instrument = None
        self._connected = False

        atexit.register(self.close)

    def connect(self):
        if not self.address:
            raise ValueError("No address provided for the instrument.")
        self.instrument = self.rm.open_resource(self.address)
        self._connected = True
        self._log("Connected to instrument.")
        self.get_id()  # Verify connection

    def disconnect(self):
        if self.instrument:
            self.instrument.close()
            self.instrument = None
            self._connected = False
            self._log("Disconnected from instrument.")

    def is_connected(self):
        return self._connected

    def __enter__(self):
        if self._connected:
            raise ValueError("Cannot use context management on already connected device")
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        atexit.unregister(self.close)
        self.disconnect()

    def get_id(self):
        self._check_connection()
        res = self.instrument.query("*IDN?")
        res = res.split(",")
        if len(res) != 4:
            raise ValueError("IDN string does not follow Agilent's layout")
        if res[0] != "Agilent Technologies":
            raise ValueError(f"IDN returned manufacturer {res[0]}")
        if res[1] != "34461A":
            raise ValueError(f"IDN did not return device type 34410A but {res[1]}")
        return {
            'type': res[1],
            'serial': res[2]
        }

    def get_serial(self):
        return self.get_id()['serial']

    def get_voltage(self):
        self._check_connection()
        self.instrument.write(":CONF:VOLT:DC")
        resp = self.instrument.query(":READ?")
        return float(resp)

    def get_current(self):
        self._check_connection()
        self.instrument.write(":CONF:CURR:DC")
        resp = self.instrument.query(":READ?")
        return float(resp)

    def turn_auto_zero_off(self):
        self._check_connection()
        self.instrument.write(":ZERO:AUTO OFF")
        self._log("Auto-zero turned off.")

    def turn_auto_zero_on(self):
        self._check_connection()
        self.instrument.write(":ZERO:AUTO ON")
        self._log("Auto-zero turned on.")

    def _check_connection(self):
        if not self._connected:
            raise ConnectionError("Instrument is not connected")

    def _log(self, message):
        if self.logger:
            self.logger.info(message)

if __name__ == "__main__":
    with Agilent34410A("USB0::0x0957::0x1A07::MY53206340::INSTR") as multi:
        print("Voltage: ", multi.get_voltage())
        print("Current: ", multi.get_current())

