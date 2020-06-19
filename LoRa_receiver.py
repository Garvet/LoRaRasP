#!/usr/bin/env python3
# coding=utf-8
import RPi.GPIO as GPIO
import SPI_LoRa as LoRa
import time
import json
import packet_analyzer as analyzer


def close_pin():
    GPIO.cleanup(pin_reset)
    if not (pin_dio0 is None):
        GPIO.cleanup(pin_dio0)
    if not (pin_dio1 is None):
        GPIO.cleanup(pin_dio1)
    if not (pin_dio3 is None):
        GPIO.cleanup(pin_dio3)


file = '/home/pi/Documents/text.txt'
frequency = 4330E5
GPIO_mode = GPIO.BOARD
pin_reset = 22
SPI_bus = 0
SPI_nss = 0
pin_dio0 = 36
pin_dio1 = 38
pin_dio3 = None


connection = analyzer.init_connect()
GPIO.setmode(GPIO_mode)
lora = LoRa.LoRaClass(pin_reset=pin_reset, spi_bus=SPI_bus, spi_nss=SPI_nss,
                      pin_dio0=pin_dio0, pin_dio1=pin_dio1, pin_dio3=pin_dio3)
if lora.begin(frequency=frequency, SyncWord=0x34):
    print('Error: not LoRa-module')
    analyzer.exit_connect(connection)
    exit(1)
try:
    input_json = []
    data = {'address': [], 'number': []}
    while True:
        receiver = lora.receiver_packet(file_name=file)
        if len(receiver) > 0:
            json_str = str(receiver[-1])
            try:
                packet = json.loads(json_str)
                analyzer.data_handler(packet=packet, data=data, connection=connection, file_name=file)
            except Exception as exception:
                print(json_str)
                print('Error: ' + str(exception))

except Exception as exception:
    print('Error: ' + str(exception))
finally:
    analyzer.exit_connect(connection)
    close_pin()

