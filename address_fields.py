
def value_range(value, min_value=0, max_value=0xFF):
    if value < min_value:
        value = min_value
    elif value > max_value:
        value = max_value
    return value


class Register:
    def __init__(self, address=0, bit_count=8, bit_bias=0, bit_in_reg=8):
        bit_count = value_range(bit_count, 1, bit_in_reg)
        bit_bias = value_range(bit_bias, 0, (bit_in_reg - bit_count))
        mask = 0x00
        for num in range(bit_in_reg):
            if num < bit_count:
                mask = (mask << 1) + 1
            elif num < bit_count+bit_bias:
                mask <<= 1
        self.address = address
        self.bit_count = bit_count
        self.bit_bias = bit_bias
        self.mask = mask


class Field:
    def __init__(self, register, min_value=0, max_value=None, reserved_value=None, mode='r'):
        self.register = None
        self.reg_count = None
        self.min_value = None
        self.max_value = None
        self.reserved_value = None
        self.mode = None
        self.init(register, min_value, max_value, reserved_value, mode)

    def init(self, register, min_value=0, max_value=None, reserved_value=None, mode='r'):
        if reserved_value is None:
            reserved = []
        else:
            if not(isinstance(reserved_value, list)):
                reserved = [reserved_value]
            else:
                reserved = reserved_value
        if not(isinstance(register, list)):
            registers = [register]
        else:
            registers = register
        bit_count = 0
        reg_address = []
        for register in registers:
            if not(isinstance(register, Register)):
                return True
            else:
                bit_count += register.bit_count
                if not(register.address in reg_address):
                    reg_address.append(register.address)
        value = 0
        for num in range(bit_count):
            value = (value << 1) + 1
        min_value = value_range(min_value, 0, value)
        if max_value is None:
            max_value = value
        else:
            max_value = value_range(max_value, min_value, value)
        self.register = registers
        self.reg_count = len(reg_address)
        self.min_value = min_value
        self.max_value = max_value
        self.reserved_value = reserved
        self.mode = mode
        return False

    def get_value(self, register_value):
        if not(isinstance(register_value, dict)):
            return 'Value not correct'
        if len(register_value) < self.reg_count:
            return 'Invalid number of registers'
        for register in self.register:
            if not(register.address in register_value):
                return 'Invalid address of registers (not %s)' % str(register.address)
        value = 0
        for register in reversed(self.register):
            value <<= register.bit_count
            value |= (register_value[register.address] & register.mask) >> register.bit_bias
        return value

    def set_value(self, value, register_value=None):
        if self.mode == 'r':
            return 'Read-only field'
        if (value < self.min_value) or (value > self.max_value) or (value in self.reserved_value):
            return 'Value not correct'
        if not(register_value is None):
            if not(isinstance(register_value, dict)):
                return 'Register value not correct'
            if len(register_value) < self.reg_count:
                return 'Invalid number of registers'
            for register in self.register:
                if not(register.address in register_value):
                    return 'Invalid address of registers (not %s)' % str(register.address)
        else:
            register_value = {}
            for register in self.register:
                register_value[register.address] = 0

        for register in self.register:
            register_value[register.address] &= ~register.mask
            register_value[register.address] |= (value & (register.mask >> register.bit_bias)) << register.bit_bias
            value >>= register.bit_count
        return register_value
