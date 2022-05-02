while True:

    val = pins.analog_read_pin(AnalogPin.P0)
    basic.show_number(val)
    serial.write_value("val", val)