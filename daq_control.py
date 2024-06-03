import nidaqmx
from nidaqmx.constants import AcquisitionType
from time import sleep

device_id = "cDAQ1Mod1"
pin1 = "AO15"
# Function to set voltage
def set_voltage(channel, voltage):
    with nidaqmx.Task() as task:
        task.ao_channels.add_ao_voltage_chan(channel, min_val=-10.0, max_val=10.0)
        task.write(voltage)

# Function to get voltage (only for AI channels)
def get_voltage(channel):
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan(channel, min_val=-10.0, max_val=10.0)
        task.timing.cfg_samp_clk_timing(1000, sample_mode=AcquisitionType.CONTINUOUS)
        data = task.read(number_of_samples_per_channel=1)
        return data

# Example usage
if __name__ == "__main__":
    # Replace 'cDAQ1Mod1/ao0' and 'cDAQ1Mod1/ai0' with your actual channel names
    set_voltage(f'{device_id}/{pin1}', 5.0)
    # voltage = get_voltage(f'{device_id}/{pin1}')
    # print(f"Measured Voltage: {voltage} V")
	
    counter = 0
    while 1:
	    counter = counter + 1
	    set_voltage('cDAQ1Mod1/ao15', counter % 5)
	    sleep(0.001)
