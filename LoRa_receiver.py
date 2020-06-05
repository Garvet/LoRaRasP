#!/usr/bin/env python3
# coding=utf-8
import RPi.GPIO as GPIO
import SPI_LoRa as LoRa
import time
import json
import packet_analyzer as analyzer

frequency = 4330E5
GPIO_mode = GPIO.BOARD
pin_reset = 22
SPI_bus = 0
SPI_nss = 0
# pin_dio0 = None
# pin_dio1 = None
# pin_dio3 = None

connection = analyzer.init_connect()
GPIO.setmode(GPIO_mode)
lora = LoRa.LoRaClass(pin_reset=pin_reset, spi_bus=SPI_bus, spi_nss=SPI_nss)
lora.begin(frequency=frequency, SyncWord=0x34)
try:
    input_json = []
    data = {'address': [], 'number': []}
    while True:
        receiver = lora.receiver_packet()
        if len(receiver) > 0:
            json_str = str(receiver[-1])
            try:
                packet = json.loads(json_str)
                analyzer.data_handler(packet=packet, data=data, connection=connection)
            except Exception as exception:
                print(json_str)
                print('Error: ' + str(exception))

except Exception:
    analyzer.exit_connect(connection)
    GPIO.cleanup()

