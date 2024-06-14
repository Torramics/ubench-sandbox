import marimo

__generated_with = "0.6.13"
app = marimo.App()


@app.cell
def __():
    import marimo as mo
    return mo,


@app.cell
def __():
    import pyvisa as visa
    import time

    # Create a resource manager
    rm = visa.ResourceManager()

    visa_address = 'USB0::0x0957::0x1A07::MY53206340::INSTR'

    # Open a connection to the instrument
    dmm = rm.open_resource(visa_address)

    # Set a longer timeout (e.g., 5000 ms)
    # dmm.timeout = 50000
    # print(dmm.query('*IDN?'))

    while True:
        derp = dmm.query('MEAS:VOLT:DC?')
        # print(derp)
        time.sleep(0.2)
    return derp, dmm, rm, time, visa, visa_address


@app.cell
def __(derp, mo):
    mo.md(f"# {derp} v")
    return


@app.cell
def __():


    return


if __name__ == "__main__":
    app.run()
