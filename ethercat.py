import time
import spidev

bus = 0
device = 0  # chip enable 0, Etherberry is connected to CE0

spi = spidev.SpiDev()
spi.open(bus, device)

spi.max_speed_hz = 3000000  # 3 MHz bcm2835_spi_setClockDivider(16); calculates to 15 Mhz
spi.mode = 0                # bcm2835_spi_setDataMode(BCM2835_SPI_MODE0);
spi.lsbfirst = False        # bcm2835_spi_setBitOrder(BCM2835_SPI_BIT_ORDER_MSBFIRST);
spi.no_cs = True            # bcm2835_spi_chipSelect(BCM2835_SPI_CS_NONE);
spi.cshigh = False          # bcm2835_spi_setChipSelectPolarity(BCM2835_SPI_CS0, LOW);
spi.bits_per_word = 8
