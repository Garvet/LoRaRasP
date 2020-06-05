#!/usr/bin/env python3
# coding=utf-8
import spidev as spi
import LoRa_register as LoRa
import time
import LoRa_packet
import RPi.GPIO as GPIO

# modes
MODE_SLEEP = 0x00  # Спящий режим
MODE_STDBY = 0x01  # Режим ожидания
MODE_FSTX = 0x02  # Синтез частот TX
MODE_TX = 0x03  # Передача пакета
MODE_FSRX = 0x04  # Синтез частот RX
MODE_RX_CONTINUOUS = 0x05  # Непрерывное получение
MODE_RX_SINGLE = 0x06  # Единичное получение
MODE_CAD = 0x07  # Обнаружение активности канала

# PaDac
RF_PADAC_20DBM_ON = 0x07
RF_PADAC_20DBM_OFF = 0x04

# DetectionThreshold
DT_SF6 = 0x0C
DT_SF7_12 = 0x0A
# DetectionOptimize
DO_SF6 = 0x05
DO_SF7_12 = 0x03


class LoRaClass:
    def __init__(self, pin_reset, SPI=None, spi_nss=0, spi_bus=0, pin_dio0=None, pin_dio1=None, pin_dio3=None):
        # шина SPI
        if SPI is None:
            self._spi = spi.SpiDev()
            self._spi_start = True
        else:
            self._spi = SPI
            self._spi_start = False
        self._spi_bus = spi_bus  # num
        # выходы
        self._nss = spi_nss
        self._reset = pin_reset
        self._dio0 = pin_dio0
        self._dio1 = pin_dio1
        self._dio3 = pin_dio3
        # данные
        self._frequency = int(434E6)  # 0
        self.FifoTxBaseAddr = 0x80
        self.packet_length = 0
        self.field = LoRa.LoRaRegister(read_fun=self._read_register, write_fun=self._write_register)
        self.packet = None

    def field_set(self, field, value, write=True):
        result = self.field.set_field_value(field, value)
        if write:
            result = self.field.register_write(field=field, error_clear=True)
        return result

    def field_get(self, field, read=False):
        err, result = self.field.get_field_value(field=field, read=read)
        if isinstance(field, list):
            return result
        else:
            if field in result:
                return result[field]
            else:
                return None

    def begin(self, frequency, paboost=False, signal_power=14, SF=11, SBW=125E3, SyncWord=0x4A):
        # настройка выходов
        GPIO.setup(self._reset, GPIO.OUT)
        GPIO.output(self._reset, GPIO.HIGH)
        if not(self._dio0 is None):
            GPIO.setup(self._dio0, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        if not(self._dio1 is None):
            GPIO.setup(self._dio1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        # запуск модуля
        GPIO.output(self._reset, GPIO.LOW)
        time.sleep(0.020)
        GPIO.output(self._reset, GPIO.HIGH)
        time.sleep(0.050)
        # запуск SPI
        self._spi.open(self._spi_bus, self._nss)
        self._spi.max_speed_hz = 500000
        # проверка версии LoRa-модуля
        version = self.field_get(LoRa.Version)
        if version != 0x12:
            return True
        # переход в режим сна/настройки
        self.mode_sleep()
        # установка частоты работы модуля
        self.set_frequency(int(frequency))
        # установка адресов памяти TX и RX
        self.field_set(LoRa.FifoRxBaseAddr, 0x00)
        self.field_set(LoRa.FifoTxBaseAddr, self.FifoTxBaseAddr)
        # настройка LNA
        self.field_set(LoRa.LnaBoostHf, 0x03)
        # установка автоматического AGC
        self.field_set([LoRa.LowDataRateOptimize, LoRa.AgcAutoOn], [0, 1])
        # установкасилы сигнала на 14 дБ
        self.set_TX_power(signal_power, paboost)
        # установка силы коэффициента распространения SF
        self.set_spreading_factor(SF)
        # установка пропускной способности
        self.set_signal_bandwidth(SBW)
        # установка кодового слова 0x4A
        self.field_set(LoRa.SyncWord, SyncWord)
        # включение проверки ошибки пакета
        self.crc_enable()
        # переход в режим ожидания
        self.mode_STDBY()
        return False

    def end(self):
        # переход в режим сна
        self.mode_sleep()
        # остановка SPI, если создавалась классом
        if self._spi_start:
            self._spi.close()

    def set_mode(self, mode):
        return self.field_set([LoRa.LongRangeMode, LoRa.LowFrequencyModeOn, LoRa.Mode], [1, 0, mode])

    # Режим сна/настройки
    def mode_sleep(self):
        return self.set_mode(MODE_SLEEP)

    # Режим ожидания
    def mode_STDBY(self):
        return self.set_mode(MODE_STDBY)

    # Режим отправки
    def mode_TX(self):
        if not(self._dio0 is None):
            self.field_set(LoRa.Dio0Mapping, 1)
        return self.set_mode(MODE_TX)

    # Режим непрерывного приёма
    def mode_RX_continuous(self):
        if not(self._dio0 is None):
            self.field_set(LoRa.Dio0Mapping, 0)
        if not(self._dio1 is None):
            self.field_set(LoRa.Dio1Mapping, 0)
        return self.set_mode(MODE_RX_CONTINUOUS)

    # Режим единичного приёма
    def mode_RX_single(self):
        if not(self._dio0 is None):
            self.field_set(LoRa.Dio0Mapping, 0)
        if not(self._dio1 is None):
            self.field_set(LoRa.Dio1Mapping, 0)
        return self.set_mode(MODE_RX_SINGLE)

    # Режим проверки сети
    def mode_CAD(self):
        if not(self._dio0 is None):
            self.field_set(LoRa.Dio0Mapping, 2)
        if not(self._dio1 is None):
            self.field_set(LoRa.Dio1Mapping, 2)
        return self.set_mode(MODE_CAD)

    # Установка силы отправляемого пакета
    def set_TX_power(self, power, paboost, max_power=0x07):
        if not(isinstance(paboost, bool)):
            return True
        if max_power < 0x01:
            max_power = 0x01
        elif max_power > 0x07:
            max_power = 0x07
        self.field.register_read([LoRa.PaDac, LoRa.PaSelect, LoRa.MaxPower, LoRa.OutputPower])
        # Изменение бита PABOOST
        if paboost:
            pa_select = 1
            min_power_value = 2
            max_power_value = 20
            if power > 17:
                power_adjustment = -5
            else:
                power_adjustment = -2
        else:
            pa_select = 0
            min_power_value = -1
            max_power_value = 14
            power_adjustment = 1
        # Проверка выхода силы сигнала за диапазон
        if power < min_power_value:
            power = min_power_value
        if power > max_power_value:
            power = max_power_value
        # Корректировка параметра
        power += power_adjustment
        # Настройка флага высокого сигнала
        if power > 17:
            pa_dac = RF_PADAC_20DBM_ON
        else:
            pa_dac = RF_PADAC_20DBM_OFF

        # Передача настроек
        return self.field_set([LoRa.PaDac, LoRa.PaSelect, LoRa.MaxPower, LoRa.OutputPower],
                              [pa_dac, pa_select, max_power, power])

    # Установка частоты радиосигнала
    def set_frequency(self, frequency):
        self._frequency = frequency
        frf = int((frequency << 19) / 32000000)
        return self.field_set(LoRa.Frf, frf)

    # Установка силы коэффициента распространения SF
    def set_spreading_factor(self, SF):
        if SF < 6:
            SF = 6
        elif SF > 12:
            SF = 12
        if SF == 6:
            detection_optimize = DO_SF6
            detection_threshold = DT_SF6
        else:
            detection_optimize = DO_SF7_12
            detection_threshold = DT_SF7_12
        return self.field_set([LoRa.DetectionOptimize, LoRa.DetectionThreshold, LoRa.SpreadingFactor],
                              [detection_optimize, detection_threshold, SF])

    # Установка пропускной способности
    def set_signal_bandwidth(self, sbw):
        if sbw <= 7.8E3:
            bw = 0
        elif sbw <= 10.4E3:
            bw = 1
        elif sbw <= 15.6E3:
            bw = 2
        elif sbw <= 20.8E3:
            bw = 3
        elif sbw <= 31.25E3:
            bw = 4
        elif sbw <= 41.7E3:
            bw = 5
        elif sbw <= 62.5E3:
            bw = 6
        elif sbw <= 125E3:
            bw = 7
        elif sbw <= 250E3:
            bw = 8
        else:
            bw = 9
        return self.field_set(LoRa.Bw, bw)

    def setPreambleLength(self, length):
        return self.field_set(LoRa.PreambleLength, length)

    def set_sync_word(self, SW):
        return self.field_set(LoRa.SyncWord, SW)

    def crc_enable(self):
        return self.field_set(LoRa.RxPayloadCrcOn, 1)

    def crc_disable(self):
        return self.field_set(LoRa.RxPayloadCrcOn, 0)

    def _read_register(self, address):
        return self._single_transfer(address & 0x7f, 0x00)

    def _write_register(self, address, value):
        self._single_transfer(address | 0x80, value)

    def _single_transfer(self, address, value):
        response = self._spi.xfer2([address, value])[1]
        return response

    # Приём пакета
    def receiver_packet(self, count=1, wait=1000, rssi=False, snr=False):
        if (not isinstance(count, int)) or (count < 0):
            return True
        self.packet = []
        # if count > 1:
        #     pass
        #     # много пакетов
        # else:
        for num in range(count):
            self.mode_RX_single()
            rx_done = 0
            crc_err = 0
            for cycle in range(wait):
                time.sleep(0.01)
                # if (self._dio0 is None) or (self._dio1 is None):
                #     result = self.field_get([LoRa.RxTimeout, LoRa.RxDone], read=True)
                #     rx_timeout = result[LoRa.RxTimeout]
                #     rx_done = result[LoRa.RxDone]
                # else:
                #     rx_timeout = 0
                #     # rx_done = digitalRead(_dio0);
                result = self.field_get([LoRa.RxTimeout, LoRa.RxDone, LoRa.PayloadCrcError], read=True)
                rx_timeout = result[LoRa.RxTimeout]
                rx_done = result[LoRa.RxDone]
                crc_err = result[LoRa.PayloadCrcError]
                if rx_timeout > 0:
                    self.field.clear_flags(LoRa.RxTimeout)
                    self.mode_RX_single()
                if rx_done > 0:
                    break
            if (rx_done > 0) and (crc_err == 0):
                self.field.clear_flags(LoRa.RxDone)
                self.packet.append(self.read_packet_data(rssi=rssi, snr=snr))
            else:
                self.field.clear_flags([LoRa.RxDone, LoRa.ValidHeader, LoRa.PayloadCrcError])
            self.mode_sleep()
        return self.packet

    # Содержание последнего принятого пакета
    def read_packet_data(self, rssi=False, snr=False):
        if rssi:
            rssi = self.packet_rssi()
        else:
            rssi = None
        if snr:
            snr = self.packet_snr()
        else:
            snr = None
        length = self.field_get(LoRa.FifoRxBytesNb, read=True)
        adr = self.field_get(LoRa.FifoRxCurrentAddr)
        self.field_set(LoRa.FifoAddrPtr, adr)
        data = []
        for num in range(length):
            data.append(self.field_get(LoRa.Fifo, read=True))
        packet = LoRa_packet.LoRaPacket(data=data, rssi=rssi, snr=snr)
        return packet

    # RSSI последнего принятого пакета
    def packet_rssi(self):
        rssi = self.field_get(LoRa.PacketRssi, read=True)
        if self._frequency < int(868E6):
            rssi -= 164
        else:
            rssi -= 157
        return rssi

    # SNR последнего принятого пакета
    def packet_snr(self):
        snr = self.field_get(LoRa.PacketSnr, read=True) * 0.25
        return snr

    # Отправка пакета
    def sender_packet(self, packet, wait=True):
        self.packet_begin()
        if self.packet_write(packet):
            return True
        if self.packet_end(wait=wait):
            return True
        return False

    # Объявление пакета
    def packet_begin(self):
        self.mode_STDBY()
        self.field_set(LoRa.FifoAddrPtr, self.FifoTxBaseAddr)
        self.packet_length = 0
        return False

    # Отправка данных в пакет buffer, size=None? (len)
    def packet_write(self, packet):
        if not(isinstance(packet, list)):
            data = [packet]
        else:
            data = packet
        if len(data) + self.packet_length > 255:
            return True
        self.packet_length += len(data)
        for symbol in data:
            self.field_set(LoRa.Fifo, symbol)
        self.field_set(LoRa.PayloadLength, self.packet_length)
        return False

    # Отправка пакета
    def packet_end(self, wait=True, sleep=False):
        self.mode_TX()
        result = False
        if wait:
            tx_done = 0
            for cycle in range(1000):
                time.sleep(0.01)
                # if self._dio0 is None:
                #     tx_done = self.field_get(LoRa.TxDone, read=True)
                # else:
                #     pass
                #     # tx_done = digitalRead(_dio0);
                tx_done = self.field_get(LoRa.TxDone, read=True)
                if tx_done > 0:
                    self.field.clear_flags(LoRa.TxDone)
                    break
            if tx_done == 0:
                result = True
            if sleep:
                self.mode_sleep()
        return result
