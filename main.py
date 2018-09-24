# main.py -- put your code here!
from pyb import Pin, ADC, UART
adc = ADC(Pin('X5'))
L1 = Pin('X1', pyb.Pin.OUT_PP)
L2 = Pin('X2', pyb.Pin.OUT_PP)
L3 = Pin('X3', pyb.Pin.OUT_PP)
L4 = Pin('X4', pyb.Pin.OUT_PP)
L5 = Pin('X6', pyb.Pin.OUT_PP)
while True:
    x = adc.read()
    if x > 110 and x < 300:
        L1.high()
    elif x > 301 and x < 500:
        L1.high()
        L2.high()
    elif x > 501 and x < 700:
        L1.high()
        L2.high()
        L3.high()
    elif x > 701 and x < 1000:
        L1.high()
        L2.high()
        L3.high()
        L4.high()
        L5.high()
    else:
        L2.low()
        L3.low()
        L4.low()
        L5.low()
        L1.low()

