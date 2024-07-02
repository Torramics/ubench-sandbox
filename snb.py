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
    # device = "SimDev1" # NI cRIO-9076

    # channel = "AO0"
    channel = "ao0"

    channel2 = "AO1"


    # update this here
    min_voltage = 0
    # max_voltage = 10

    # Instantiate the generator
    wave_gen = WaveformGenerator(device, channel)
    # wave_gen2 = WaveformGenerator(device, channel2)
    return channel, channel2, device, min_voltage, wave_gen


@app.cell
def __(mo):
    max_voltage = mo.ui.number(
        start = 0, 
        stop = 10,
        step = 0.2,
        value = 10,
        label = "### Max voltage out")

    max_voltage
    return max_voltage,


@app.cell
def __(mo):
    min_press = mo.ui.number(
        start = -14, 
        stop = 0,
        step = 0.2,
        value = -2,
        label = "### Min pressure (PSI)")

    min_press
    return min_press,


@app.cell
def __(mo):
    max_press = mo.ui.number(
        start = 0, 
        stop = 14,
        step = 0.2,
        value = 2,
        label = "### Max pressure (PSI)")

    max_press
    return max_press,


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
        Returns voltage from psi conversion as a float.
        """
        return float(round(abs((1/2.8) * (psi + 14.0)), 2))
    return voltage,


@app.cell
def __(mo):
    mo.md("# Proportional Air Flow Controller 💨")
    return


@app.cell
def __(mo):
    # flow 1 state
    getter, setter = mo.state(0.0)
    return getter, setter


@app.cell
def __(getter, mo):
    mo.md(f"{getter()}")
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
def __(mo, volts):
    mo.md(f"{volts} V")
    return


@app.cell
def __(getter, max_press, min_press, mo, setter):
    pressure =  mo.ui.slider(
        # start= min_voltage, 
        # stop = max_voltage,
        # start = -14.00,
        start = min_press.value,
        # stop = 14.00,
        stop = max_press.value,
        step = 0.05,
        full_width = True, 
        show_value = True,
        value = getter(),
        # orientation = 'vertical',
        on_change = setter,
        label = "### PSI"
    )

    pressure
    return pressure,


@app.cell
def __(getter, max_press, min_press, mo, setter):
    pres_num = mo.ui.number(
        # -14.00,
        # 14.00,
        start = min_press.value,
        stop = max_press.value,
        step = 0.05,
        value=getter(),
        on_change=setter,
        # label = "### PSI"
    )

    pres_num
    return pres_num,


@app.cell
def __():
    # [pressure, pres_num, phase, frequency]
    return


@app.cell
def __(button, mo):
    mo.stop(not button.value, "Click 'run' to generate a random number")
    return


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
        label="## FLOW 1",
    )

    radiogroup
    return radiogroup,


@app.cell
def __(
    button,
    duration,
    frequency,
    max_voltage,
    phase,
    pressure,
    radiogroup,
    voltage,
    wave_gen,
):
    volts = min(voltage(pressure.value), max_voltage.value)

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
        # orientation = 'vertical',
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
def __(max_press, min_press, mo):
    pressure2 =  mo.ui.slider(
        # start= min_voltage, 
        # stop = max_voltage,
        # start = -14,
        # stop = 14,
        start = min_press.value,
        stop = max_press.value,
        step = 1,
        full_width = True, 
        show_value = True,
        value = 0,
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
        label="## FLOW 2",
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
    frequency2,
    max_voltage,
    phase2,
    pressure2,
    radiogroup2,
    voltage,
    wave_gen2,
):
    # volts2 = voltage(pressure2.value)
    volts2 = min(voltage(pressure2.value), max_voltage.value)

    if radiogroup2.value == 'sin':
        wave_gen2.sin(frequency=frequency2.value, amplitude=volts2, phase=phase2.value, duration=duration.value)
    elif radiogroup2.value == 'square':
        wave_gen2.square(frequency=frequency2.value, amplitude=volts2, phase=phase2.value, duration=duration.value)
    elif radiogroup2.value == 'triangle':
        wave_gen2.triangle(frequency=frequency2.value, amplitude=volts2, phase=phase2.value, duration=duration.value)
    elif radiogroup2.value == 'constant':
        wave_gen2.constant(voltage=volts2)

    button2
    return volts2,


@app.cell
def __(mo):
    button2 = mo.ui.run_button()
    return button2,


@app.cell
def __(mo):
    mo.md(
        rf"""
        # Analog Part
        -----------------
        """
    )
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
