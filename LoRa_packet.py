#!/usr/bin/env python3
# coding=utf-8
import struct


class LoRaPacket:
    def __init__(self, data=None, rssi=None, snr=None):
        self.data = self.len = self.rssi = self.snr = None
        self.set_packet(data=data, rssi=rssi, snr=snr)

    def set_packet(self, data=None, rssi=None, snr=None):
        self.data = data
        if data is None:
            self.len = 0
        else:
            if isinstance(data, list):
                self.len = len(data)
            else:
                self.len = 1
        self.rssi = rssi
        self.snr = snr

    def get_float(self, reg_start):
        if (reg_start + 4) > self.len:
            return True
        reg_float = self.data[reg_start:reg_start + 4]  # [0x64, 0xD8, 0x6E, 0x3F]
        byt = bytearray(reg_float)
        value = struct.unpack('<f', byt)[0]
        return value

    def set_float(self, reg_start, value):
        if ((reg_start + 4) > self.len) or not(isinstance(value, float)):
            return True
        byt = struct.pack('f', value)
        for i in range(len(byt)):
            self.data[reg_start + i] = int(byt[i])
        return False

    def __len__(self):
        return self.len

    def __str__(self):
        result = ''
        for num in range(self.len):
            result = result + chr(self.data[num])
        return result

    def __getitem__(self, num):  # - доступ по индексу (или ключу).
        if (not isinstance(num, int)) or (num > self.len - 1):
            return False
        return self.data[num]

    def __setitem__(self, num, value):  # - назначение элемента по индексу.
        if (not isinstance(num, int)) or (num > self.len - 1):
            return
        if (not isinstance(value, int)) or (value > 0xFF):
            return
        self.data[num] = value

