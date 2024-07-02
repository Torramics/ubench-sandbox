import pyvisa as visa
import time
import matplotlib.pyplot as plt
from collections import deque

# Initialize PyVISA resource manager
rm = visa.ResourceManager()

# Specify the VISA address of your instrument
visa_address = 'USB0::0x0957::0x1A07::MY53206340::INSTR'

# Initialize plot
plt.ion()  # Turn on interactive mode
fig, ax = plt.subplots()
line, = ax.plot([], [], 'b-', label='Voltage (V)')
ax.set_xlabel('Time')
ax.set_ylabel('Voltage (V)')
ax.set_title('Live Voltage Measurement')
ax.grid(True)
ax.legend()

# Initialize deque for storing data
max_points = 100  # Adjust based on how many points you want to display
times = deque(maxlen=max_points)
voltages = deque(maxlen=max_points)

try:
    # Open a connection to the instrument
    dmm = rm.open_resource(visa_address)
    
    # Set a longer timeout (in milliseconds) to handle slower measurements
    dmm.timeout = 10000  # 10 seconds timeout
    
    # Clear any previous data in the input buffer
    dmm.clear()

    # Main loop for continuous data acquisition
    while True:
        # Query the instrument for DC voltage measurement
        derp = dmm.query('MEAS:VOLT:DC?')
        
        # Convert the measurement to float and append to the deque
        volt = float(derp)
        voltages.append(volt)
        
        # Append current time to deque
        times.append(time.time())
        
        # Update plot data
        line.set_data(times, voltages)
        
        # Adjust plot limits
        ax.relim()
        ax.autoscale_view()
        
        # Redraw the plot
        fig.canvas.draw()
        fig.canvas.flush_events()
        
        # Print the measurement (optional)
        # print(f"Voltage: {volt} V")
        
        # Pause for a short time before the next measurement
        time.sleep(0.5)

except visa.VisaIOError as e:
    print(f"VISA error: {e}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the connection to the instrument, if open
    if 'dmm' in locals():
        dmm.close()
        print("Connection to DMM closed.")
#############

# import pyvisa as visa
# import time
# import numpy as np  # Import numpy for calculations

# # Initialize an empty list to store the voltage measurements
# voltage_values = []
# timestamps = []  # Add a new list for timestamps

# # Desired sleep duration between measurements (in seconds)
# sleep_duration = 0.5

# # Calculate the expected sampling rate in Hz before starting the measurement loop
# expected_sampling_rate = 1 / sleep_duration

# # Initialize the resource manager
# rm = visa.ResourceManager()
# visa_address = 'USB0::0x0957::0x1A07::MY53206340::INSTR'

# # Open a session to the device
# inst = rm.open_resource(visa_address)  # replace 'GPIB0::15::INSTR' with your actual instrument address

# # Set the multimeter to measure voltage in DC mode
# inst.write(":CONF:VOLT:DC")

# try:
#     while True:
#         # Get the current time before taking a measurement
#         timestamp = time.time()
#         timestamps.append(timestamp)

#         # Read and print the voltage measurement
#         # voltage = inst.query_ascii_values(":READ?")
#         voltage = inst.query(":READ?")

#         voltage_values.append(voltage[0])
#         print(f"Voltage: {voltage_values[-1]} V")

#         # Wait for the desired sleep duration before taking the next measurement
#         time.sleep(sleep_duration)
# except KeyboardInterrupt:
#     # Close the session when done (this will also release the instrument)
#     inst.close()

# # Calculate the actual sampling rate in Hz after interrupting the measurement
# time_differences = np.diff(timestamps)  # Calculate time differences between consecutive measurements
# actual_sampling_rate = 1 / np.mean(time_differences)  # Calculate the average sampling rate
# print(f"Expected Sampling Rate: {expected_sampling_rate} Hz")
# print(f"Actual Sampling Rate: {actual_sampling_rate} Hz")