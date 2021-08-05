from machine import UART

# uart1 = UART(1, baudrate=9600, tx=33, rx=32)
uart2 = UART(2, baudrate=9600)  # hardware-16,17
uart2.write('hello')  # 5
# >>> 5
uart2.read(5)
# >>> b'hello'
