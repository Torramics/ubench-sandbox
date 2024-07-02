import marimo

__generated_with = "0.6.13"
app = marimo.App()


@app.cell
def __():
    import marimo as mo
    return mo,


@app.cell
def __():
    # import pyvisa as visa
    # import time

    # # Create a resource manager
    # rm = visa.ResourceManager()

    # visa_address = 'USB0::0x0957::0x1A07::MY53206340::INSTR'

    # # Open a connection to the instrument
    # dmm = rm.open_resource(visa_address)

    # # Set a longer timeout (e.g., 5000 ms)
    # # dmm.timeout = 50000
    # # print(dmm.query('*IDN?'))
    # derp = "" #dmm.query('MEAS:VOLT:DC?') ### string
    #     # print(derp)
    # voltages = []

    # while True:
    #     derp = dmm.query('MEAS:VOLT:DC?')
    #     voltages.append(float(derp))  # Assuming derp is a string representing voltage
    #     # print(derp)
    #     time.sleep(0.2)

    # # print length(voltages)
    return


@app.cell
def __(mo):
    getter, setter = mo.state(0.000000)
    return getter, setter


@app.cell
def __():
    # mo.md(f"# {voltages[-1]} v")
    return


@app.cell
def __():
    # import pyvisa as visa
    # import time
    # import matplotlib.pyplot as plt
    # from collections import deque

    # # Initialize PyVISA resource manager
    # rm = visa.ResourceManager()

    # # Specify the VISA address of your instrument
    # visa_address = 'USB0::0x0957::0x1A07::MY53206340::INSTR'

    # # Initialize plot
    # plt.ion()  # Turn on interactive mode
    # fig, ax = plt.subplots()
    # line, = ax.plot([], [], 'b-', label='Voltage (V)')
    # ax.set_xlabel('Time')
    # ax.set_ylabel('Voltage (V)')
    # ax.set_title('Live Voltage Measurement')
    # ax.grid(True)
    # ax.legend()

    # # Initialize deque for storing data
    # max_points = 100  # Adjust based on how many points you want to display
    # times = deque(maxlen=max_points)
    # voltages = deque(maxlen=max_points)

    # try:
    #     # Open a connection to the instrument
    #     dmm = rm.open_resource(visa_address)

    #     # Set a longer timeout (in milliseconds) to handle slower measurements
    #     dmm.timeout = 10000  # 10 seconds timeout

    #     # Clear any previous data in the input buffer
    #     dmm.clear()

    #     # Main loop for continuous data acquisition
    #     while True:
    #         # Query the instrument for DC voltage measurement
    #         derp = dmm.query('MEAS:VOLT:DC?')

    #         # Convert the measurement to float and append to the deque
    #         volt = float(derp)
    #         voltages.append(volt)

    #         # Append current time to deque
    #         times.append(time.time())

    #         # Update plot data
    #         line.set_data(times, voltages)

    #         # Adjust plot limits
    #         ax.relim()
    #         ax.autoscale_view()

    #         # Redraw the plot
    #         fig.canvas.draw()
    #         fig.canvas.flush_events()

    #         # Print the measurement (optional)
    #         # print(f"Voltage: {volt} V")

    #         # Pause for a short time before the next measurement
    #         time.sleep(0.2)

    # except visa.VisaIOError as e:
    #     print(f"VISA error: {e}")

    # except Exception as e:
    #     print(f"An error occurred: {e}")

    # finally:
    #     # Close the connection to the instrument, if open
    #     if 'dmm' in locals():
    #         dmm.close()
    #         print("Connection to DMM closed.")
    return


@app.cell
def __():
    import pyvisa as visa
    import time

    # Initialize an empty list to store the voltage measurements
    voltage_values = []

    # Initialize the resource manager
    rm = visa.ResourceManager()
    visa_address = 'USB0::0x0957::0x1A07::MY53206340::INSTR'

    # Open a session to the device
    inst = rm.open_resource(visa_address)  # replace 'GPIB0::15::INSTR' with your actual instrument address

    # Set the multimeter to measure voltage in DC mode
    inst.write(":CONF:VOLT:DC")

    try:
        while True:
            # Read and print the voltage measurement
            voltage = inst.query_ascii_values(":READ?")
            print(f"Voltage: {voltage[0]} V")

            # Append the voltage measurement to the list
            voltage_values.append(voltage[0])

            # Wait for 100ms before taking the next measurement
            time.sleep(0.01)
    except KeyboardInterrupt:
        # Close the session when done (this will also release the instrument)
        inst.close()
    return inst, rm, time, visa, visa_address, voltage, voltage_values


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
