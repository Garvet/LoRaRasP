#!/usr/bin/env python3
# coding=utf-8
import address_fields as adr_fields

#   ----- ----- ----- - - - - - - - - - ----- ----- -----
# ----- ----- ----- Список регистров LoRa ----- ----- -----
#   ----- ----- ----- - - - - - - - - - ----- ----- -----
REG_FIFO = 0x00
# --- Общие регистры настроек ---
REG_OP_MODE = 0x01
REG_FRF_MSB = 0x06
REG_FRF_MID = 0x07
REG_FRF_LSB = 0x08
# --- Регистры для блоков RF ---
REG_PA_CONFIG = 0x09
REG_PA_RAMP = 0x0A
REG_LR_OCP = 0X0B
REG_LNA = 0x0C
# --- Страница регистров LoRa ---
REG_FIFO_ADDR_PTR = 0x0D
REG_FIFO_TX_BASE_ADDR = 0x0E
REG_FIFO_RX_BASE_ADDR = 0x0F
REG_FIFO_RX_CURRENT_ADDR = 0x10
REG_IRQ_FLAGS_MASK = 0x11
REG_IRQ_FLAGS = 0x12
REG_RX_NB_BYTES = 0x13
REG_RX_HEADER_CNT_VALUE_MSB = 0x14
REG_RX_HEADER_CNT_VALUE_LSB = 0x15
REG_RX_PACKET_CNT_VALUE_MSB = 0x16
REG_RX_PACKET_CNT_VALUE_LSB = 0x17
REG_MODEM_STAT = 0x18
REG_PKT_SNR_VALUE = 0x19
REG_PKT_RSSI_VALUE = 0x1A
REG_RSSI_VALUE = 0x1B
REG_HOP_CHANNEL = 0x1C
REG_MODEM_CONFIG_1 = 0x1D
REG_MODEM_CONFIG_2 = 0x1E
REG_SYMB_TIMEOUT_LSB = 0x1F
REG_PREAMBLE_MSB = 0x20
REG_PREAMBLE_LSB = 0x21
REG_PAYLOAD_LENGTH = 0x22
REG_MAX_PAYLOAD_LENGTH = 0x23
REG_HOP_PERIOD = 0x24
REG_FIFI_RX_BYTE_ADDR = 0x25
REG_MODEM_CONFIG_3 = 0x26
REG_PPM_CORRECTION = 0x27
REG_FEI_MSB = 0x28
REG_FEI_MID = 0x29
REG_FEI_LSB = 0x2A
REG_RSSI_WIDEBAND = 0x2C
REG_DETECTION_OPTIMIZE = 0x31
REG_INVERT_IQ = 0x33
REG_DETECTION_THRESHOLD = 0x37
REG_SYNC_WORD = 0x39
# --- Регистры управления IO ---
REG_DIO_MAPPING_1 = 0x40
REG_DIO_MAPPING_2 = 0x41
# --- Регистр версий ---
REG_VERSION = 0x42
# --- Дополнительные регистры ---
REG_PLL_HOP = 0x44
REG_TCXO = 0x4B
REG_PA_DAC = 0x4D
REG_FORMER_TEMP = 0x5B
REG_BITRATE_FRAC = 0x5D
REG_AGC_REF = 0x61
REG_AGC_THRESH_1 = 0x62
REG_AGC_THRESH_2 = 0x63
REG_AGC_THRESH_3 = 0x64
REG_PLL_HF = 0x70


#   ----- ----- ----- - - - - - - ----- ----- -----
# ----- ----- ----- Поля и регистры ----- ----- -----
#   ----- ----- ----- - - - - - - ----- ----- -----

# --- --- --- Регистр очереди --- --- ---
# - REG_FIFO -
Fifo = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_FIFO, bit_count=8, bit_bias=0)],
                     min_value=0x00, max_value=0xFF, mode='rw')

# --- --- --- Общие регистры настроек --- --- ---
# - REG_OP_MODE -
LongRangeMode = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_OP_MODE, bit_count=1, bit_bias=7)],
                     min_value=0x00, max_value=0x01, mode='rw')
AccessSharedReg = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_OP_MODE, bit_count=1, bit_bias=6)],
                     min_value=0x00, max_value=0x01, mode='rw')
LowFrequencyModeOn = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_OP_MODE, bit_count=1, bit_bias=3)],
                     min_value=0x00, max_value=0x01, mode='rw')
Mode = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_OP_MODE, bit_count=3, bit_bias=0)],
                     min_value=0x00, max_value=0x07, mode='rw')

# - REG_FRF_* -
Frf = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_FRF_LSB, bit_count=8, bit_bias=0),
                               adr_fields.Register(address=REG_FRF_MID, bit_count=8, bit_bias=0),
                               adr_fields.Register(address=REG_FRF_MSB, bit_count=8, bit_bias=0)],
                     min_value=0x000000, max_value=0xFFFFFF, mode='rw')


# --- --- --- Регистры для блоков RF --- --- ---
# - REG_PA_CONFIG -
PaSelect = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_PA_CONFIG, bit_count=1, bit_bias=7)],
                     min_value=0x00, max_value=0x01, mode='rw')
MaxPower = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_PA_CONFIG, bit_count=3, bit_bias=4)],
                     min_value=0x00, max_value=0x07, mode='rw')
OutputPower = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_PA_CONFIG, bit_count=4, bit_bias=0)],
                     min_value=0x00, max_value=0x0F, mode='rw')
# - REG_PA_RAMP -
PaRamp = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_PA_RAMP, bit_count=4, bit_bias=0)],
                     min_value=0x00, max_value=0x0F, mode='rw')
# - REG_LR_OCP -
OcpOn = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_LR_OCP, bit_count=1, bit_bias=5)],
                     min_value=0x00, max_value=0x01, mode='rw')
OcpTrim = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_LR_OCP, bit_count=5, bit_bias=0)],
                     min_value=0x00, max_value=0x1F, mode='rw')
# - REG_LNA -
LnaGain = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_LNA, bit_count=3, bit_bias=5)],
                     min_value=0x01, max_value=0x06, mode='rw')
LnaBoostLf = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_LNA, bit_count=2, bit_bias=3)],
                     min_value=0x00, max_value=0x00, mode='rw')
LnaBoostHf = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_LNA, bit_count=2, bit_bias=0)],
                     min_value=0x00, max_value=0x03, mode='rw', reserved_value=[0x01, 0x02])


# --- --- --- Страница регистров LoRa --- --- ---
# - REG_FIFO_ADDR_PTR -
FifoAddrPtr = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_FIFO_ADDR_PTR, bit_count=8, bit_bias=0)],
                     min_value=0x00, max_value=0xFF, mode='rw')
# - REG_FIFO_TX_BASE_ADDR -
FifoTxBaseAddr = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_FIFO_TX_BASE_ADDR, bit_count=8, bit_bias=0)],
                     min_value=0x00, max_value=0xFF, mode='rw')
# - REG_FIFO_RX_BASE_ADDR -
FifoRxBaseAddr = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_FIFO_RX_BASE_ADDR, bit_count=8, bit_bias=0)],
                     min_value=0x00, max_value=0xFF, mode='rw')
# - REG_FIFO_RX_CURRENT_ADDR -
FifoRxCurrentAddr = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_FIFO_RX_CURRENT_ADDR, bit_count=8, bit_bias=0)],
                     min_value=0x00, max_value=0xFF, mode='r')
# - REG_IRQ_FLAGS_MASK -
RxTimeoutMask = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_IRQ_FLAGS_MASK, bit_count=1, bit_bias=7)],
                     min_value=0x00, max_value=0x01, mode='rw')
RxDoneMask = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_IRQ_FLAGS_MASK, bit_count=1, bit_bias=6)],
                     min_value=0x00, max_value=0x01, mode='rw')
PayloadCrcErrorMask = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_IRQ_FLAGS_MASK, bit_count=1, bit_bias=5)],
                     min_value=0x00, max_value=0x01, mode='rw')
ValidHeaderMask = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_IRQ_FLAGS_MASK, bit_count=1, bit_bias=4)],
                     min_value=0x00, max_value=0x01, mode='rw')
TxDoneMask = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_IRQ_FLAGS_MASK, bit_count=1, bit_bias=3)],
                     min_value=0x00, max_value=0x01, mode='rw')
CadDoneMask = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_IRQ_FLAGS_MASK, bit_count=1, bit_bias=2)],
                     min_value=0x00, max_value=0x01, mode='rw')
FhssChangeChannelMask = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_IRQ_FLAGS_MASK, bit_count=1, bit_bias=1)],
                     min_value=0x00, max_value=0x01, mode='rw')
CadDetectedMask = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_IRQ_FLAGS_MASK, bit_count=1, bit_bias=0)],
                     min_value=0x00, max_value=0x01, mode='rw')
# - REG_IRQ_FLAGS -
RxTimeout = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_IRQ_FLAGS, bit_count=1, bit_bias=7)],
                     min_value=0x00, max_value=0x01, mode='rc')
RxDone = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_IRQ_FLAGS, bit_count=1, bit_bias=6)],
                     min_value=0x00, max_value=0x01, mode='rc')
PayloadCrcError = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_IRQ_FLAGS, bit_count=1, bit_bias=5)],
                     min_value=0x00, max_value=0x01, mode='rc')
ValidHeader = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_IRQ_FLAGS, bit_count=1, bit_bias=4)],
                     min_value=0x00, max_value=0x01, mode='rc')
TxDone = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_IRQ_FLAGS, bit_count=1, bit_bias=3)],
                     min_value=0x00, max_value=0x01, mode='rc')
CadDone = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_IRQ_FLAGS, bit_count=1, bit_bias=2)],
                     min_value=0x00, max_value=0x01, mode='rc')
FhssChangeChannel = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_IRQ_FLAGS, bit_count=1, bit_bias=1)],
                     min_value=0x00, max_value=0x01, mode='rc')
CadDetected = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_IRQ_FLAGS, bit_count=1, bit_bias=0)],
                     min_value=0x00, max_value=0x01, mode='rc')
# - REG_RX_NB_BYTES -
FifoRxBytesNb = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_RX_NB_BYTES, bit_count=8, bit_bias=0)],
                     min_value=0x00, max_value=0xFF, mode='r')
# - REG_RX_HEADER_CNT_VALUE_* -
ValidHeaderCnt = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_RX_HEADER_CNT_VALUE_LSB, bit_count=8, bit_bias=0),
                               adr_fields.Register(address=REG_RX_HEADER_CNT_VALUE_MSB, bit_count=8, bit_bias=0)],
                     min_value=0x0000, max_value=0xFFFF, mode='r')
# - REG_RX_PACKET_CNT_VALUE_* -
ValidPacketCnt = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_RX_PACKET_CNT_VALUE_LSB, bit_count=8, bit_bias=0),
                               adr_fields.Register(address=REG_RX_PACKET_CNT_VALUE_MSB, bit_count=8, bit_bias=0)],
                     min_value=0x0000, max_value=0xFFFF, mode='rc')
# - REG_MODEM_STAT -
RxCodingRate = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_MODEM_STAT, bit_count=3, bit_bias=5)],
                     min_value=0x00, max_value=0x07, mode='r')
ModemStatus = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_MODEM_STAT, bit_count=5, bit_bias=0)],
                     min_value=0x00, max_value=0x1F, mode='r')
# - REG_PKT_SNR_VALUE -
PacketSnr = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_PKT_SNR_VALUE, bit_count=8, bit_bias=0)],
                     min_value=0x00, max_value=0xFF, mode='r')
# - REG_PKT_RSSI_VALUE -
PacketRssi = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_PKT_RSSI_VALUE, bit_count=8, bit_bias=0)],
                     min_value=0x00, max_value=0xFF, mode='r')
# - REG_RSSI_VALUE -
Rssi = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_RSSI_VALUE, bit_count=8, bit_bias=0)],
                     min_value=0x00, max_value=0xFF, mode='r')
# - REG_HOP_CHANNEL -
PllTimeout = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_HOP_CHANNEL, bit_count=1, bit_bias=7)],
                     min_value=0x00, max_value=0x01, mode='r')
CrcOnPayload = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_HOP_CHANNEL, bit_count=1, bit_bias=6)],
                     min_value=0x00, max_value=0x01, mode='r')
FhssPresentChannel = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_HOP_CHANNEL, bit_count=6, bit_bias=0)],
                     min_value=0x00, max_value=0x3F, mode='r')
# - REG_MODEM_CONFIG_1 -
Bw = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_MODEM_CONFIG_1, bit_count=4, bit_bias=4)],
                     min_value=0x00, max_value=0x09, mode='rw')
CodingRate = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_MODEM_CONFIG_1, bit_count=3, bit_bias=1)],
                     min_value=0x01, max_value=0x04, mode='rw')
ImplicitHeaderModeOn = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_MODEM_CONFIG_1, bit_count=1, bit_bias=0)],
                     min_value=0x00, max_value=0x01, mode='rw')
# - REG_MODEM_CONFIG_2 -
SpreadingFactor = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_MODEM_CONFIG_2, bit_count=4, bit_bias=4)],
                     min_value=0x06, max_value=0x0C, mode='rw')
TxContinuousMode = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_MODEM_CONFIG_2, bit_count=1, bit_bias=3)],
                     min_value=0x00, max_value=0x01, mode='rw')
RxPayloadCrcOn = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_MODEM_CONFIG_2, bit_count=1, bit_bias=2)],
                     min_value=0x00, max_value=0x01, mode='rw')
# - REG_SYMB_TIMEOUT_* -
SymbTimeout = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_SYMB_TIMEOUT_LSB, bit_count=8, bit_bias=0),
                               adr_fields.Register(address=REG_MODEM_CONFIG_2, bit_count=2, bit_bias=0)],
                     min_value=0x0000, max_value=0x03FF, mode='rw')
# - REG_PREAMBLE_* -
PreambleLength = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_PREAMBLE_LSB, bit_count=8, bit_bias=0),
                               adr_fields.Register(address=REG_PREAMBLE_MSB, bit_count=8, bit_bias=0)],
                     min_value=0x0000, max_value=0xFFFF, mode='rw')
# - REG_PAYLOAD_LENGTH -
PayloadLength = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_PAYLOAD_LENGTH, bit_count=8, bit_bias=0)],
                     min_value=0x01, max_value=0xFF, mode='rw')
# - REG_MAX_PAYLOAD_LENGTH -
PayloadMaxLength = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_MAX_PAYLOAD_LENGTH, bit_count=8, bit_bias=0)],
                     min_value=0x00, max_value=0xFF, mode='rw')
# - REG_HOP_PERIOD -
FreqHoppingPeriod = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_HOP_PERIOD, bit_count=8, bit_bias=0)],
                     min_value=0x00, max_value=0xFF, mode='rw')
# - REG_FIFI_RX_BYTE_ADDR -
FifoRxByteAddrPtr = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_FIFI_RX_BYTE_ADDR, bit_count=8, bit_bias=0)],
                     min_value=0x00, max_value=0xFF, mode='r')
# - REG_MODEM_CONFIG_3 -
LowDataRateOptimize = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_MODEM_CONFIG_3, bit_count=1, bit_bias=3)],
                     min_value=0x00, max_value=0x01, mode='rw')
AgcAutoOn = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_MODEM_CONFIG_3, bit_count=1, bit_bias=2)],
                     min_value=0x00, max_value=0x01, mode='rw')
# - REG_PPM_CORRECTION -
PpmCorrection = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_PPM_CORRECTION, bit_count=8, bit_bias=0)],
                     min_value=0x00, max_value=0xFF, mode='rw')
# - REG_FEI_* -
FreqError = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_FEI_LSB, bit_count=8, bit_bias=0),
                               adr_fields.Register(address=REG_FEI_MID, bit_count=8, bit_bias=0),
                               adr_fields.Register(address=REG_FEI_MSB, bit_count=4, bit_bias=0)],
                     min_value=0x000000, max_value=0x0FFFFF, mode='r')
# - REG_RSSI_WIDEBAND -
RssiWideband = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_RSSI_WIDEBAND, bit_count=8, bit_bias=0)],
                     min_value=0x00, max_value=0xFF, mode='r')
# - REG_DETECTION_OPTIMIZE -
DetectionOptimize = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_DETECTION_OPTIMIZE, bit_count=3, bit_bias=0)],
                     min_value=0x03, max_value=0x05, mode='rw', reserved_value=[0x04])
# - REG_INVERT_IQ -
InvertIQ = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_INVERT_IQ, bit_count=1, bit_bias=6)],
                     min_value=0x00, max_value=0x01, mode='rw')
# - REG_DETECTION_THRESHOLD -
DetectionThreshold = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_DETECTION_THRESHOLD, bit_count=8, bit_bias=0)],
                     min_value=0x0A, max_value=0x0C, mode='rw', reserved_value=[0x0B])
# - REG_SYNC_WORD -
SyncWord = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_SYNC_WORD, bit_count=8, bit_bias=0)],
                     min_value=0x00, max_value=0xFF, mode='rw')  # , reserved_value=[0x34])


# --- --- --- Регистры управления IO --- --- ---
# - REG_DIO_MAPPING_1 -
Dio0Mapping = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_DIO_MAPPING_1, bit_count=2, bit_bias=6)],
                     min_value=0x00, max_value=0x03, mode='rw')
Dio1Mapping = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_DIO_MAPPING_1, bit_count=2, bit_bias=4)],
                     min_value=0x00, max_value=0x03, mode='rw')
Dio2Mapping = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_DIO_MAPPING_1, bit_count=2, bit_bias=2)],
                     min_value=0x00, max_value=0x03, mode='rw')
Dio3Mapping = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_DIO_MAPPING_1, bit_count=2, bit_bias=0)],
                     min_value=0x00, max_value=0x03, mode='rw')
# - REG_DIO_MAPPING_2 -
Dio4Mapping = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_DIO_MAPPING_2, bit_count=2, bit_bias=6)],
                     min_value=0x00, max_value=0x03, mode='rw')
Dio5Mapping = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_DIO_MAPPING_2, bit_count=2, bit_bias=4)],
                     min_value=0x00, max_value=0x03, mode='rw')
MapPreambleDetect = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_DIO_MAPPING_2, bit_count=1, bit_bias=0)],
                     min_value=0x00, max_value=0x01, mode='rw')


# --- --- --- Регистр версий --- --- ---
# - REG_VERSION -
Version = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_VERSION, bit_count=8, bit_bias=0)],
                     min_value=0x00, max_value=0xFF, mode='r')


# --- --- --- Дополнительные регистры --- --- ---
# - REG_PLL_HOP -
FastHopOn = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_PLL_HOP, bit_count=1, bit_bias=7)],
                     min_value=0x00, max_value=0x01, mode='rw')
# - REG_TCXO -
TcxoInputOn = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_TCXO, bit_count=1, bit_bias=4)],
                     min_value=0x00, max_value=0x01, mode='rw')
# - REG_PA_DAC -
PaDac = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_PA_DAC, bit_count=3, bit_bias=0)],
                     min_value=0x04, max_value=0x07, mode='rw', reserved_value=[0x05, 0x06])
# - REG_FORMER_TEMP -
FormerTemp = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_FORMER_TEMP, bit_count=8, bit_bias=0)],
                     min_value=0x00, max_value=0xFF, mode='r')
# - REG_BITRATE_FRAC -
BitRateFrac = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_BITRATE_FRAC, bit_count=4, bit_bias=0)],
                     min_value=0x00, max_value=0x0F, mode='rw')
# - REG_AGC_REF -
AgcReferenceLevel = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_AGC_REF, bit_count=6, bit_bias=0)],
                     min_value=0x00, max_value=0x3F, mode='rw')
# - REG_AGC_THRESH_1 -
AgcStep1 = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_AGC_THRESH_1, bit_count=5, bit_bias=0)],
                     min_value=0x00, max_value=0x1F, mode='rw')
# - REG_AGC_THRESH_2 -
AgcStep2 = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_AGC_THRESH_2, bit_count=4, bit_bias=4)],
                     min_value=0x00, max_value=0x0F, mode='rw')
AgcStep3 = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_AGC_THRESH_2, bit_count=4, bit_bias=0)],
                     min_value=0x00, max_value=0x0F, mode='rw')
# - REG_AGC_THRESH_3 -
AgcStep4 = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_AGC_THRESH_3, bit_count=4, bit_bias=4)],
                     min_value=0x00, max_value=0x0F, mode='rw')
AgcStep5 = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_AGC_THRESH_3, bit_count=4, bit_bias=0)],
                     min_value=0x00, max_value=0x0F, mode='rw')
# - REG_PLL_HF -
PllBandwidth = \
    adr_fields.Field(register=[adr_fields.Register(address=REG_PLL_HF, bit_count=2, bit_bias=6)],
                     min_value=0x00, max_value=0x03, mode='rw')


ALL_REGISTER = \
    [REG_FIFO, REG_OP_MODE, REG_FRF_MSB, REG_FRF_MID, REG_FRF_LSB, REG_PA_CONFIG,
     REG_PA_RAMP, REG_LR_OCP, REG_LNA, REG_FIFO_ADDR_PTR, REG_FIFO_TX_BASE_ADDR,
     REG_FIFO_RX_BASE_ADDR, REG_FIFO_RX_CURRENT_ADDR, REG_IRQ_FLAGS_MASK,
     REG_IRQ_FLAGS, REG_RX_NB_BYTES, REG_RX_HEADER_CNT_VALUE_MSB,
     REG_RX_HEADER_CNT_VALUE_LSB, REG_RX_PACKET_CNT_VALUE_MSB,
     REG_RX_PACKET_CNT_VALUE_LSB, REG_MODEM_STAT, REG_PKT_SNR_VALUE,
     REG_PKT_RSSI_VALUE, REG_RSSI_VALUE, REG_HOP_CHANNEL, REG_MODEM_CONFIG_1,
     REG_MODEM_CONFIG_2, REG_SYMB_TIMEOUT_LSB, REG_PREAMBLE_MSB, REG_PREAMBLE_LSB,
     REG_PAYLOAD_LENGTH, REG_MAX_PAYLOAD_LENGTH, REG_HOP_PERIOD,
     REG_FIFI_RX_BYTE_ADDR, REG_MODEM_CONFIG_3, REG_PPM_CORRECTION, REG_FEI_MSB,
     REG_FEI_MID, REG_FEI_LSB, REG_RSSI_WIDEBAND, REG_DETECTION_OPTIMIZE,
     REG_INVERT_IQ, REG_DETECTION_THRESHOLD, REG_SYNC_WORD, REG_DIO_MAPPING_1,
     REG_DIO_MAPPING_2, REG_VERSION, REG_PLL_HOP, REG_TCXO, REG_PA_DAC,
     REG_FORMER_TEMP, REG_BITRATE_FRAC, REG_AGC_REF, REG_AGC_THRESH_1,
     REG_AGC_THRESH_2, REG_AGC_THRESH_3, REG_PLL_HF]

ALL_FIELD = \
    [Fifo, LongRangeMode, AccessSharedReg, LowFrequencyModeOn, Mode, Frf, PaSelect,
     MaxPower, OutputPower, PaRamp, OcpOn, OcpTrim, LnaGain, LnaBoostLf, LnaBoostHf,
     FifoAddrPtr, FifoTxBaseAddr, FifoRxBaseAddr, FifoRxCurrentAddr, RxTimeoutMask,
     RxDoneMask, PayloadCrcErrorMask, ValidHeaderMask, TxDoneMask, CadDoneMask,
     FhssChangeChannelMask, CadDetectedMask, RxTimeout, RxDone, PayloadCrcError,
     ValidHeader, TxDone, CadDone, FhssChangeChannel, CadDetected, FifoRxBytesNb,
     ValidHeaderCnt, ValidPacketCnt, RxCodingRate, ModemStatus, PacketSnr, PacketRssi,
     Rssi, PllTimeout, CrcOnPayload, FhssPresentChannel, Bw, CodingRate,
     ImplicitHeaderModeOn, SpreadingFactor, TxContinuousMode, RxPayloadCrcOn,
     SymbTimeout, PreambleLength, PayloadLength, PayloadMaxLength, FreqHoppingPeriod,
     FifoRxByteAddrPtr, LowDataRateOptimize, AgcAutoOn, PpmCorrection, FreqError,
     RssiWideband, DetectionOptimize, InvertIQ, DetectionThreshold, SyncWord,
     Dio0Mapping, Dio1Mapping, Dio2Mapping, Dio3Mapping, Dio4Mapping, Dio5Mapping,
     Version, FastHopOn, TcxoInputOn, PaDac, FormerTemp, BitRateFrac, AgcReferenceLevel,
     AgcStep1, AgcStep2, AgcStep3, AgcStep4, AgcStep5, PllBandwidth]


# Функции должны принимать следующие параметры: значение=read_fun(адрес), write_fun(адрес, значение)
class LoRaRegister:
    def __init__(self, read_fun, write_fun):
        self._error = []
        self._register = {}
        self._send = False
        self._function = {'read': read_fun, 'write': write_fun}
        self.flags = [RxTimeout, RxDone, PayloadCrcError, ValidHeader, TxDone, CadDone, FhssChangeChannel, CadDetected]

    def clear(self):
        self._error = []
        self._register = {}
        self._send = False

    def set_function(self, read_fun, write_fun):
        self._function = {'read': read_fun, 'write': write_fun}

    def get_register(self):
        return self._register

    def get_error(self):
        return self._error

    def get_send(self):
        return self._send

    def get_function(self):
        return self._function

    def check_error(self):
        for num in range(len(self._error)):
            if self._error[num]['important']:
                return True
        return False

    def field_formatting(self, field):
        if not(isinstance(field, list)):
            fields = [field]
        else:
            fields = field
        new_error = False
        error_fields = []
        correct_fields = []
        for num, field in enumerate(fields):
            if not(field in ALL_FIELD):
                self._error.append({'important': False, 'name': 'ValueError',
                                    'text': 'field[' + str(num) + '] not correct', 'value': field})
                new_error = True
                error_fields.append(num)
            else:
                correct_fields.append(field)
        return new_error, correct_fields, error_fields

    @staticmethod
    def check_read(fields):
        bit_count = {}
        check_field = []
        registers = []
        for field in fields:
            if not(field in check_field):
                check_field.append(field)
                for register in field.register:
                    if not(register.address in registers):
                        registers.append(register.address)
                        bit_count[register.address] = 0
                    bit_count[register.address] |= register.mask
                # for field_reg in field['reg']:
                #     if field_reg['address'] in bit_count:
                #         bit_count[field_reg['address']] += field_reg['bit']
        reg_read = []
        reg_not_read = []
        for register in bit_count:
            if bit_count[register] == 0xFF:
                reg_not_read.append(register)
            else:
                reg_read.append(register)
        return reg_read, reg_not_read

    @staticmethod
    def field_registers(field):
        registers = []
        for register in field.register:
            if not(register.address in registers):
                registers.append(register.address)
        return registers

    # Проверка отсутствия в классе регистров полей (вывод: отсутствующие поля)
    def check_missing_register(self, fields):
        check = []
        for field in fields:
            for register in self.field_registers(field):
                if not (register in self._register):
                    check.append(register)
        return check

    # field - поле(я) данных, value - значение(я) поля(ей)
    def set_field_value(self, field, value):
        new_error, fields, num_error = self.field_formatting(field=field)
        if not(isinstance(value, list)):
            values = [value]
        else:
            values = value
        if not (len(fields) == len(values)):
            if not ((len(fields) + len(num_error)) == len(values)):
                return 'Unequal size of parameters'
            else:
                for num in reversed(num_error):
                    values.pop(num)
        missing_register = self.check_missing_register(fields)
        if len(missing_register) > 0:
            reg_read, reg_not_read = self.check_read(fields)
            for register in reg_not_read:
                if not(register in self._register):
                    self._register[register] = 0
            if len(reg_read) > 0:
                self.register_read(field=fields, update=False)
        for num, field in enumerate(fields):
            result = field.set_value(value=values[num], register_value=self._register)
            if not(isinstance(result, str)):
                self._register = result
            else:
                new_error = True
                self._error.append({'important': True, 'name': 'ValueError',
                                    'text': result, 'value': (field, value[num])})
        return new_error

    def get_field_value(self, field, read=False):
        new_error, fields, num_error = self.field_formatting(field=field)
        if self.check_missing_register(fields) or read:
            self.register_read(field=fields, update=read)
        result = {}
        for field in fields:
            result[field] = field.get_value(self._register)
        return new_error, result

    def register_read(self, field, update=True):
        if self._send:
            self.clear()
        new_error, fields, not_used = self.field_formatting(field)
        registers = []
        for field in fields:
            result = self.field_registers(field)
            for register in result:
                if not(register in registers):
                    registers.append(register)
        for register in registers:
            if not (register in self._register) or update:
                self._register[register] = self._function['read'](register)
        return new_error

    def register_write(self, field=None, error_clear=False, clear=True):
        new_error = False
        if self.check_error():
            if error_clear:
                self.clear()
            return True
        if field is None:
            for address in self._register:
                self._function['write'](address, self._register[address])
        else:
            new_error, fields, not_used = self.field_formatting(field)
            registers = []
            for field in fields:
                result = self.field_registers(field)
                for register in result:
                    if not(register in registers):
                        registers.append(register)
            for register in registers:
                if not(register in self._register):
                    if error_clear:
                        self.clear()
                    return True
            for address in reversed(registers):
                self._function['write'](address, self._register[address])
        self._send = True
        if clear:
            self.clear()
        return new_error

    def clear_flags(self, flag, back_value=False):
        if not isinstance(flag, list):
            flags = [flag]
        else:
            flags = flag
        for flag in flags:
            if not(flag in self.flags):
                return True
        if not(REG_IRQ_FLAGS in self._register):
            return True
        register = self._register[REG_IRQ_FLAGS]
        self._register[REG_IRQ_FLAGS] = 0
        for flag in flags:
            self.set_field_value(flag, 1)
        self._function['write'](REG_IRQ_FLAGS, self._register[REG_IRQ_FLAGS])
        if back_value:
            self._register[REG_IRQ_FLAGS] = register
        else:
            self._register[REG_IRQ_FLAGS] = register | ~self._register[REG_IRQ_FLAGS]
        return False
