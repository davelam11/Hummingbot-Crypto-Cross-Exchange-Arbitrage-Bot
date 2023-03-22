from hummingbot.market.binance.binance_market import BinanceMarket
from hummingbot.market.bybit.bybit_market import BybitMarket
from hummingbot.market.gateio.gateio_market import GateioMarket
from hummingbot.market.bitfinex.bitfinex_market import BitfinexMarket
from hummingbot.market.huobi.huobi_market import HuobiGlobalMarket
from hummingbot.market.kucoin.kucoin_market import KucoinMarket

# Initialize the markets
binance = BinanceMarket()
bybit = BybitMarket()
gateio = GateioMarket()
bitfinex = BitfinexMarket()
huobi = HuobiGlobalMarket()
kucoin = KucoinMarket()

# List of markets to be used in the strategy
markets = [binance, bybit, gateio, bitfinex, huobi, kucoin]

# Add the exchange credentials
binance_key = "your_binance_api_key"
binance_secret = "your_binance_secret_key"
bybit_key = "your_bybit_api_key"
bybit_secret = "your_bybit_secret_key"
gateio_key = "your_gateio_api_key"
gateio_secret = "your_gateio_secret_key"
bitfinex_key = "your_bitfinex_api_key"
bitfinex_secret = "your_bitfinex_secret_key"
huobi_key = "your_huobi_api_key"
huobi_secret = "your_huobi_secret_key"
kucoin_key = "your_kucoin_api_key"
kucoin_secret = "your_kucoin_secret_key"

# Configure API keys in hummingbot
config_file = open("hummingbot_config.yml", 'w')
config_file.write("""
binance:
  api_key: """ + binance_key + """
  secret_key: """ + binance_secret + """
bybit:
  api_key: """ + bybit_key + """
  secret_key: """ + bybit_secret + """
gateio:
  api_key: """ + gateio_key + """
  secret_key: """ + gateio_secret + """
bitfinex:
  api_key: """ + bitfinex_key + """
  secret_key: """ + bitfinex_secret + """
huobi:
  api_key: """ + huobi_key + """
  secret_key: """ + huobi_secret + """
kucoin:
  api_key: """ + kucoin_key + """
  secret_key: """ + kucoin_secret + """
""")
config_file.close()

# Start the hummingbot client
app = Application(strategy_file_path="./hummingbot_strategy.py", config_path="hummingbot_config.yml")
app.start()