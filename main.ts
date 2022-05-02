let val: number;
while (true) {
    val = pins.analogReadPin(AnalogPin.P0)
    basic.showNumber(val)
}
