import nidaqmx
import numpy as np
import time

# Device: SimDev1
# ao_channel = "SimDev1/ao0"
# ai_channel = "SimDev1/ai0" 

def generate_sine_wave(sample_rate, frequency, duration, amplitude=5.0):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    return amplitude * np.sin(2 * np.pi * frequency * t)

def analog_output(task_name, channel, data, sample_rate):
    with nidaqmx.Task(task_name) as task:
        task.ao_channels.add_ao_voltage_chan(channel, min_val=-10.0, max_val=10.0)
        task.timing.cfg_samp_clk_timing(rate=sample_rate, sample_mode=nidaqmx.constants.AcquisitionType.CONTINUOUS)
        task.write(data, auto_start=False)
        task.start()
        time.sleep(len(data) / sample_rate)
        task.stop()

def analog_input(task_name, channel, sample_rate, duration):
    num_samples = int(sample_rate * duration)
    with nidaqmx.Task(task_name) as task:
        task.ai_channels.add_ai_voltage_chan(channel, min_val=-10.0, max_val=10.0)
        task.timing.cfg_samp_clk_timing(rate=sample_rate, sample_mode=nidaqmx.constants.AcquisitionType.CONTINUOUS)
        data = task.read(number_of_samples_per_channel=num_samples)
        return np.array(data)

def list_available_channels():
    system = nidaqmx.system.System.local()
    for device in system.devices:
        print(f"Device: {device.name}")
        for ai_channel in device.ai_physical_chans:
            print(f"  AI Channel: {ai_channel.name}")
        for ao_channel in device.ao_physical_chans:
            print(f"  AO Channel: {ao_channel.name}")

def main():
    # List available channels for verification
    list_available_channels()

    sample_rate = 1000.0  # Samples per second
    frequency = 1.0       # Frequency of the sine wave
    duration = 5.0        # Duration in seconds

    # Generate waveform data
    output_data = generate_sine_wave(sample_rate, frequency, duration)

    # Perform Analog Output
    ao_channel = "SimDev1/ao0"  # Replace with your actual AO channel if available
    print("Starting Analog Output...")
    analog_output("AnalogOutputTask", ao_channel, output_data, sample_rate)
    print("Analog Output Completed")

    # Perform Analog Input
    ai_channel = "SimDev1/ai0"  # Replace with your actual AI channel if available
    print("Starting Analog Input...")
    input_data = analog_input("AnalogInputTask", ai_channel, sample_rate, duration)
    print("Analog Input Completed")
    
    # Display Input Data
    print("Input Data:")
    print(input_data)

if __name__ == "__main__":
    main()
