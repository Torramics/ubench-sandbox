# import pyvisa as visa
import time
import numpy as np  # Import numpy for calculations

from agilent34461a_dmm import Agilent34461A

with Agilent34461A("USB0::0x0957::0x1A07::MY53206340::INSTR") as multi:
    # print("Voltage: ", multi.get_voltage())
    # print("Current: ", multi.get_current())
    multi.turn_auto_zero_off()

    # Initialize an empty list to store the voltage measurements
    voltage_values = []
    timestamps = []  # Add a new list for timestamps

    # Desired sleep duration between measurements (in seconds)
    sleep_duration = 1

    # Calculate the expected sampling rate in Hz before starting the measurement loop
    expected_sampling_rate = 1 / sleep_duration

    try:
        while True:
            # Get the current time before taking a measurement
            timestamp = time.time()
            timestamps.append(timestamp)

            # Read and print the voltage measurement
            # voltage = inst.query_ascii_values(":READ?")
            # voltage = inst.query(":READ?")
            voltage = multi.get_voltage()
            voltage_values.append(voltage)
            # print(f"Voltage: {voltage_values[-1]} V")

            # Wait for the desired sleep duration before taking the next measurement
            # time.sleep(sleep_duration)
    except KeyboardInterrupt:
        # Close the session when done (this will also release the instrument)
        multi.close()

    # Calculate the actual sampling rate in Hz after interrupting the measurement
    time_differences = np.diff(timestamps)  # Calculate time differences between consecutive measurements
    actual_sampling_rate = 1 / np.mean(time_differences)  # Calculate the average sampling rate
    print(f"Expected Sampling Rate: {expected_sampling_rate} Hz")
    print(f"Actual Sampling Rate: {actual_sampling_rate} Hz")