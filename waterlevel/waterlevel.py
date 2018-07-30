import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

mcp = Adafruit_MCP3008.MCP3008(clk=11, cs=8, miso=9, mosi=10)

print(mcp.read_adc(0))
