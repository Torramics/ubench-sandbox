import nidaqmx
from nidaqmx.constants import AcquisitionType
import logging
from time import sleep, time

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

device_id = "cDAQ1Mod1"
pin_output = "AO0"

# Function to set voltage
def set_voltage(channel, voltage):
    try:
        with nidaqmx.Task() as task:
            task.ao_channels.add_ao_voltage_chan(channel, min_val=-10.0, max_val=10.0)
            task.write(voltage)
            logging.info(f"Voltage set to {voltage} V on channel {channel}")
    except nidaqmx.DaqError as e:
        logging.error(f"Failed to set voltage on {channel}: {e}")
        raise

# Function to cycle through a voltage pattern
def cycle_voltages(channel, pattern, duration=10, interval=1):
    start_time = time()
    while time() - start_time < duration:
        for voltage in pattern:
            set_voltage(channel, voltage)
            sleep(interval)

# Example usage
if __name__ == "__main__":
    voltage_pattern = [0, 2.5, 5, 7.5, 10, 7.5, 5, 2.5]  # Example voltage pattern
    try:
        logging.info("Starting voltage cycling...")
        cycle_voltages(f'{device_id}/{pin_output}', voltage_pattern, duration=60, interval=2)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
