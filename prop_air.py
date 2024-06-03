import marimo

__generated_with = "0.6.13"
app = marimo.App(layout_file="layouts/marimo-daq.grid.json")


@app.cell
def __(mo):
    mo.md("# Proportional Air Valves")
    return


@app.cell
def __():
    import marimo as mo
    import nidaqmx
    from nidaqmx.constants import AcquisitionType
    import logging
    from time import sleep, time
    import time
    import numpy as np

    # Setup logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    device_id = "cDAQ1Mod1"
    pin_output = "AO0"
    return (
        AcquisitionType,
        device_id,
        logging,
        mo,
        nidaqmx,
        np,
        pin_output,
        sleep,
        time,
    )


@app.cell
def __(device_id, pin_output):
    channel = f'{device_id}/{pin_output}'
    return channel,


@app.cell
def __(mo):
    get_state, set_state = mo.state(0)
    return get_state, set_state


@app.cell
def __():
    # output V is set match the input value. (NEEDS CALIBRATION) LATENCY? ACCURACY?
    return


@app.cell
def __(mo):
    mo.md("Constant Voltage")
    return


@app.cell
def __(get_state, max_voltage, min_voltage, mo, set_state):
    slider = mo.ui.slider(
        start=min_voltage, 
        stop=max_voltage, 
        step= 0.2, 
        value=get_state(), 
        on_change=set_state,
        full_width = True, 
        show_value = True,
        orientation = 'vertical',
        label = "### S&B Controller (V)"
    )

    slider
    return slider,


@app.cell
def __(get_state, mo, set_state):
    # updating the state through the number will recreate the slider (above)
    number = mo.ui.number(0, 10, value=get_state(), on_change=set_state)
    number
    return number,


@app.cell
def __(get_state, mo):
    mo.md(f"### {get_state()} V")
    return


@app.cell
def __(channel, set_voltage, slider):
    set_voltage(channel, slider.value)
    return


@app.cell
def __():
    max_voltage = 10.0  # High state voltage
    min_voltage = 0.0    # Low state voltage
    return max_voltage, min_voltage


@app.cell
def __(nidaqmx):
    def set_voltage(channel, voltage):
        with nidaqmx.Task() as task:
            task.ao_channels.add_ao_voltage_chan(channel, min_val=-10.0, max_val=10.0)
            task.write(voltage)

            # logging.info(f"Voltage set to {voltage:.2f} V on channel {channel}")
    return set_voltage,


@app.cell
def __(max_voltage, min_voltage, np, set_voltage, time):
    def breathe(channel, duration, frequency):
        """Generates a breathing effect using a sinusoidal voltage pattern."""
        period = 1 / frequency
        start_time = time.time()
        current_time = 0

        while current_time < duration:
            current_time = time.time() - start_time
            # Calculate the sine wave pattern
            sine_value = (np.sin(2 * np.pi * frequency * current_time) + 1) / 2  # Normalize to 0 to 1
            voltage = min_voltage + (max_voltage - min_voltage) * sine_value
            set_voltage(channel, voltage)
            time.sleep(0)  # Update interval
    return breathe,


@app.cell
def __(duration, mo):
    mo.md(f"## Duration ({duration.value} sec)")
    return


@app.cell
def __(mo):
    duration = mo.ui.number(0, 100).form()  # Duration to run the breathing effect in seconds
    duration
    return duration,


@app.cell
def __(frequency, mo):
    mo.md(f"## Frequency {frequency.value} /sec")
    return


@app.cell
def __(mo):
    frequency = mo.ui.slider(0, 1, step=0.1).form()  # Frequency of breathing cycles per second
    frequency
    return frequency,


@app.cell
def __(breathe, channel, duration, e, frequency, logging):
    try:
        logging.info("Starting breathing output... \n breathing...")
        breathe(channel, duration.value, frequency.value)
    except Exception as e:
        logging.error(f"An error occurred while generating the breathing effect: {e}")
    return


@app.cell
def __(amplitude, mo):
    mo.md(f"### Amplitude: {amplitude.value}")
    return


@app.cell
def __(max_voltage, min_voltage, mo):
    amplitude =  mo.ui.slider(start= min_voltage, stop = max_voltage, step = 1)
    amplitude
    return amplitude,


@app.cell
def __(amplitude):
    amp_offset = 2 # phase
    offset_v_min = amp_offset - amplitude.value
    offset_v_max = amp_offset + amplitude.value
    print(offset_v_max)
    return amp_offset, offset_v_max, offset_v_min


@app.cell
def __():
    return


@app.cell
def __(mo):
    mo.md(
        f"""
        # S&B 5k
        >We need some thangs:

        - Amplitude (min V / max V)
        - Offset (phase)
        - Frequency
        - Duty cycle
        """
    )
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
