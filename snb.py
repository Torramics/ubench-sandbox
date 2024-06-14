import marimo

__generated_with = "0.6.13"
app = marimo.App(layout_file="layouts/snb.grid.json")


@app.cell
def __():
    import marimo as mo
    from wave_gen import WaveformGenerator
    import numpy as np
    return WaveformGenerator, mo, np


@app.cell
def __(WaveformGenerator):
    device = "cDAQ1Mod1"
    channel = "AO0"
    channel2 = "AO1"

    # update this here
    min_voltage = 0
    max_voltage = 10

    # Instantiate the generator
    wave_gen = WaveformGenerator(device, channel)
    wave_gen2 = WaveformGenerator(device, channel2)
    return (
        channel,
        channel2,
        device,
        max_voltage,
        min_voltage,
        wave_gen,
        wave_gen2,
    )


@app.cell
def __():
    # Make a generator for each proportional air channel - example usage:

    # Generate and output different waveforms
    # wave_gen.sin(frequency=0.2, pressure=10, phase=0, duration=duration.value)
    # wave_gen.square(frequency=0.5, pressure=pressure.value, phase=0, duration=30)
    # wave_gen.triangle(frequency=0.5, pressure=5, phase=0, duration=12)
    return


@app.cell
def __():
    def voltage(psi):
        """
        returns voltage from psi conversion
        """
        return round(abs((1/2.8) * (psi + 14)))
    return voltage,


@app.cell
def __(mo):
    mo.md("# Proportional Air Wave Generator 💨")
    return


@app.cell
def __(mo):
    mo.md("## Flow 1")
    return


@app.cell
def __(mo):
    duration = mo.ui.number(
        start = 0, 
        stop = 100,
        label = "### Duration (secs)\n")

    duration
    return duration,


@app.cell
def __(mo):
    pressure =  mo.ui.slider(
        # start= min_voltage, 
        # stop = max_voltage,
        start = -14,
        stop = 14,
        step = 1,
        full_width = True, 
        show_value = True,
        orientation = 'vertical',
        label = "### PSI"
    )

    pressure
    return pressure,


@app.cell
def __(mo):
    frequency = mo.ui.slider(
        start= 0, 
        stop = 1, 
        step=0.1,
        full_width = True, 
        show_value = True,
        orientation = 'horizontal',
        label = "### f (hz)") # Frequency of breathing cycles per second

    frequency
    return frequency,


@app.cell
def __(mo):
    radiogroup = mo.ui.radio(
        options={
            "sinusoidal": "sin", 
            "square": "square", 
            "triangle": "triangle",
            "constant": "constant"
        },
        # value="two",
        label="## Pick a waveform",
    )

    radiogroup
    return radiogroup,


@app.cell
def __(
    button,
    duration,
    frequency,
    phase,
    pressure,
    radiogroup,
    voltage,
    wave_gen,
):
    volts = voltage(pressure.value)

    if radiogroup.value == 'sin':
        wave_gen.sin(frequency=frequency.value, amplitude=volts, phase=phase.value, duration=duration.value)
    elif radiogroup.value == 'square':
        wave_gen.square(frequency=frequency.value, amplitude=volts, phase=phase.value, duration=duration.value)
    elif radiogroup.value == 'triangle':
        wave_gen.triangle(frequency=frequency.value, amplitude=volts, phase=phase.value, duration=duration.value)
    elif radiogroup.value == 'constant':
        wave_gen.constant(voltage=volts)

    button
    return volts,


@app.cell
def __(mo, np):
    # Create a slider for the phase using radians (π)
    phase = mo.ui.slider(
        start = 0,
        stop = 2 * np.pi, 
        step = np.pi / 4,
        full_width = True, 
        show_value = True,
        orientation = 'vertical',
        label = "### φ (rad)"
                        )  # Phase in radians (0 to 2π)

    phase
    return phase,


@app.cell
def __(mo):
    # a button that when clicked will have its value set to True;
    # any cells referencing that button will automatically run.
    button = mo.ui.run_button()
    return button,


@app.cell
def __(mo):
    mo.md(rf"## Flow 2")
    return


@app.cell
def __(mo):
    pressure2 =  mo.ui.slider(
        # start= min_voltage, 
        # stop = max_voltage,
        start = -14,
        stop = 14,
        step = 1,
        full_width = True, 
        show_value = True,
        orientation = 'vertical',
        label = "### PSI"
    )

    pressure2
    return pressure2,


@app.cell
def __(mo):
    frequency2 = mo.ui.slider(
        start= 0, 
        stop = 1, 
        step=0.1,
        full_width = True, 
        show_value = True,
        orientation = 'horizontal',
        label = "### f (hz)") # Frequency of breathing cycles per second

    frequency2
    return frequency2,


@app.cell
def __(mo):
    radiogroup2 = mo.ui.radio(
        options={
            "sinusoidal": "sin", 
            "square": "square", 
            "triangle": "triangle",
            "constant": "constant"
        },
        # value="two",
        label="## Pick a waveform",
    )

    radiogroup2
    return radiogroup2,


@app.cell
def __(mo, np):
    # Create a slider for the phase using radians (π)
    phase2 = mo.ui.slider(
        start = 0,
        stop = 2 * np.pi, 
        step = np.pi / 4,
        full_width = True, 
        show_value = True,
        orientation = 'vertical',
        label = "### φ (rad)"
                        )  # Phase in radians (0 to 2π)

    phase2
    return phase2,


@app.cell
def __(
    button2,
    duration,
    frequency,
    frequency2,
    phase2,
    pressure2,
    radiogroup2,
    voltage,
    wave_gen,
    wave_gen2,
):
    volts2 = voltage(pressure2.value)

    if radiogroup2.value == 'sin':
        wave_gen2.sin(frequency=frequency2.value, amplitude=volts2, phase=phase2.value, duration=duration.value)
    elif radiogroup2.value == 'square':
        wave_gen.square(frequency=frequency.value, amplitude=volts2, phase=phase2.value, duration=duration.value)
    elif radiogroup2.value == 'triangle':
        wave_gen.triangle(frequency=frequency2.value, amplitude=volts2, phase=phase2.value, duration=duration.value)
    elif radiogroup2.value == 'constant':
        wave_gen.constant(voltage=volts2)

    button2
    return volts2,


@app.cell
def __(mo):
    button2 = mo.ui.run_button()
    return button2,


@app.cell
def __():
    # AGILENT PART
    return


@app.cell
def __():
    # import pyvisa as visa
    # import time

    # # Create a resource manager
    # rm = visa.ResourceManager()
    # # read_voltage = 0.0
    # # Replace the VISA address below with the one you found
    # visa_address = 'USB0::0x0957::0x1A07::MY53206340::INSTR'

    # # Open a connection to the instrument
    # dmm = rm.open_resource(visa_address)

    # # Set a longer timeout (e.g., 5000 ms)
    # dmm.timeout = 50000
    # print(dmm.query('*IDN?'))
    # # dmm.write("*RST")
    # # dmm.write('DISP:VIEW TCHart')
    # # dmm.write('CONF:VOLT:DC')
    # # dmm.write('VOLT:DC:NPLC 100')
    # # dmm.write("TRIG:SOUR INT")
    # # Set the instrument to measure DC voltage
    # # dmm.write('CONF:VOLT:DC')
    # # read_voltage = dmm.query('READ?')

    # # # Print the voltage 10 times per second
    # # try:
    # #     while True:
    # #         try:
    # #             read_voltage = instrument.query('READ?')
    # #             print(f"Current Voltage: {read_voltage} V")
    # #         except visa.VisaIOError as e:
    # #             print(f"Error reading voltage: {e}")
    # #         time.sleep(0.1)  # 0.1 seconds delay to print 10 times per second
    # # except KeyboardInterrupt:
    # #     print("Measurement stopped.")
    return


@app.cell
def __():
    return


@app.cell
def __():
    # derp = dmm.query('MEAS:VOLT:DC?')
    return


@app.cell
def __():
    # mo.md(
    #     f"""
    #     Agilent voltage:
    #     {derp} V
    #     """
    # )
    return


@app.cell
def __():
    # Close the connection
    # instrument.close()
    return


@app.cell
def __():
    # import datetime as dt
    # import matplotlib.pyplot as plt
    # import matplotlib.animation as animation
    # import pyvisa as visa

    # # Create figure for plotting
    # fig, ax = plt.subplots()
    # xs = []
    # ys = []

    # # Create a resource manager
    # rm = visa.ResourceManager()

    # # Replace the VISA address below with the one you found
    # visa_address = 'USB0::0x0957::0x1A07::MY53206340::INSTR'

    # # Open a connection to the instrument
    # instrument = rm.open_resource(visa_address)

    # # Set the instrument to measure DC voltage
    # instrument.write('CONF:VOLT:DC')

    # # This function is called periodically from FuncAnimation
    # def animate(i):
    #     global xs, ys
    #     try:
    #         agilent_voltage = float(instrument.query('READ?'))
    #         print(f"Voltage reading: {agilent_voltage} V")

    #         current_time = dt.datetime.now().strftime('%H:%M:%S.%f')
    #         xs.append(current_time)
    #         ys.append(agilent_voltage)

    #         xs = xs[-20:]
    #         ys = ys[-20:]

    #         ax.clear()
    #         ax.plot(xs, ys)

    #         plt.xticks(rotation=45, ha='right')
    #         plt.subplots_adjust(bottom=0.30)
    #         plt.title('Agilent Voltage over Time')
    #         plt.ylabel('Voltage (V)')

    #         print(f"Plot updated with {len(xs)} points.")
    #     except Exception as e:
    #         print(f"Error reading voltage: {e}")

    # # Set up plot to call animate() function periodically
    # ani = animation.FuncAnimation(fig, animate, interval=1000, cache_frame_data=False)

    # # Render the plot using Marimo interactive viewer
    # mo.mpl.interactive(fig)
    return


@app.cell
def __():
    # mo.mpl.interactive(plt.gca)
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
