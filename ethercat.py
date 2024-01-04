import time
import spidev

COMM_SPI_READ = 0x03
DUMMY_BYTE = 0xFF
ID_REV_MSB = 0x00
ID_REV_LSB = 0x50

bus = 0
device = 0  # chip enable 0, Etherberry is connected to CE0

spi = spidev.SpiDev()


def init_spi():
    spi.open(bus, device)
    spi.max_speed_hz = 3900000  # 3.9 MHz bcm2835_spi_setClockDivider(16); calculates to 15 Mhz
    spi.mode = 0  # bcm2835_spi_setDataMode(BCM2835_SPI_MODE0);
    spi.lsbfirst = False  # bcm2835_spi_setBitOrder(BCM2835_SPI_BIT_ORDER_MSBFIRST);
    spi.no_cs = True  # bcm2835_spi_chipSelect(BCM2835_SPI_CS_NONE);
    spi.cshigh = False  # bcm2835_spi_setChipSelectPolarity(BCM2835_SPI_CS0, LOW);
    spi.bits_per_word = 8
    return


def etc_read_reg(address_msb, address_lsb):
    send_buffer = [COMM_SPI_READ, address_msb, address_lsb, DUMMY_BYTE, DUMMY_BYTE, DUMMY_BYTE, DUMMY_BYTE]
    receive_buffer = spi.xfer2(send_buffer)
    return receive_buffer


def find_device_id():
    dev_id = etc_read_reg(ID_REV_MSB, ID_REV_LSB)
    return dev_id
