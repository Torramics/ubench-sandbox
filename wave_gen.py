import numpy as np
import nidaqmx
from nidaqmx.constants import AcquisitionType

class WaveformGenerator:
    def __init__(self, device, channel, min_v=0, max_v=10):
        self.device = device
        self.channel = f"{device}/{channel}"
        self.min_v = min_v
        self.max_v = max_v

    def _generate_waveform(self, waveform_function, frequency, amplitude, phase, duration, fs=8000):
        t = np.linspace(0, duration, int(fs * duration), endpoint=False)
        waveform = waveform_function(2 * np.pi * frequency * t + phase)
        midpoint = (self.max_v + self.min_v) / 2
        effective_amplitude = min(amplitude, (self.max_v - self.min_v) / 2)
        waveform = effective_amplitude * waveform + midpoint
        return waveform

    def _output_waveform(self, waveform, duration, fs=8000):
        with nidaqmx.Task() as task:
            task.ao_channels.add_ao_voltage_chan(self.channel, min_val=self.min_v, max_val=self.max_v)
            task.timing.cfg_samp_clk_timing(rate=fs, sample_mode=AcquisitionType.FINITE, samps_per_chan=len(waveform))
            task.write(waveform, auto_start=True)
            task.wait_until_done(timeout=duration + 1)

    def sin(self, frequency, amplitude, phase, duration):
        waveform = self._generate_waveform(np.sin, frequency, amplitude, phase, duration)
        self._output_waveform(waveform, duration)

    def square(self, frequency, amplitude, phase, duration):
        def square_wave(x):
            return np.sign(np.sin(x))
        waveform = self._generate_waveform(square_wave, frequency, amplitude, phase, duration)
        self._output_waveform(waveform, duration)

    def triangle(self, frequency, amplitude, phase, duration):
        def triangle_wave(x):
            return 2 * (x / np.pi - np.floor(x / np.pi + 0.5)) * ((-1) ** np.floor(x / np.pi + 0.5))
        waveform = self._generate_waveform(triangle_wave, frequency, amplitude, phase, duration)
        self._output_waveform(waveform, duration)

