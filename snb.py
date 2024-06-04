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

    # update this here
    min_voltage = 0
    max_voltage = 10

    # Instantiate the generator
    wave_gen = WaveformGenerator(device, channel)
    return channel, device, max_voltage, min_voltage, wave_gen


@app.cell
def __():
    # Make a generator for each proportional air channel - example usage:

    # Generate and output different waveforms
    # wave_gen.sin(frequency=0.2, amplitude=10, phase=0, duration=duration.value)
    # wave_gen.square(frequency=0.5, amplitude=amplitude.value, phase=0, duration=30)
    # wave_gen.triangle(frequency=0.5, amplitude=5, phase=0, duration=12)
    return


@app.cell
def __(mo):
    mo.md(
        """
        # Proportional Air 
        # wave generator
        """
    )
    return


@app.cell
def __(mo):
    duration = mo.ui.number(
        start = 0, 
        stop = 100,
        label = "### Duration (secs)\n").form() 
    duration
    return duration,


@app.cell
def __(max_voltage, min_voltage, mo):
    amplitude =  mo.ui.slider(
        start= min_voltage, 
        stop = max_voltage, 
        step = 1,
        full_width = True, 
        show_value = True,
        orientation = 'vertical',
        label = "### Amplitude"
    )

    amplitude
    return amplitude,


@app.cell
def __(mo):
    frequency = mo.ui.slider(
        start= 0, 
        stop = 1, 
        step=0.1,
        full_width = True, 
        show_value = True,
        orientation = 'horizontal',
        label = "### Frequency / sec") # Frequency of breathing cycles per second
    frequency
    return frequency,


@app.cell
def __(mo):
    radiogroup = mo.ui.radio(
        options={"sinusoidal": "sin"
    , "square": "square", "triangle": "triangle"},
        # value="two",
        label="## Pick a waveform",
    )

    radiogroup
    return radiogroup,


@app.cell
def __(amplitude, duration, frequency, phase, radiogroup, wave_gen):
    if radiogroup.value == 'sin':
        wave_gen.sin(frequency=frequency.value, amplitude=amplitude.value, phase=phase.value, duration=duration.value)
    elif radiogroup.value == 'square':
        wave_gen.square(frequency=frequency.value, amplitude=amplitude.value, phase=phase.value, duration=duration.value)
    elif radiogroup.value == 'triangle':
        wave_gen.triangle(frequency=frequency.value, amplitude=amplitude.value, phase=phase.value, duration=duration.value)
    return


@app.cell
def __(mo, np):
    # Create a slider for the phase using radians (π)
    phase = mo.ui.slider(
        start = 0,
        stop = 2 * np.pi, 
        step=np.pi / 4,
        full_width = True, 
        show_value = True,
        orientation = 'vertical',
        label = "### Phase (rad)"
                        )  # Phase in radians (0 to 2π)
    phase
    return phase,


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
