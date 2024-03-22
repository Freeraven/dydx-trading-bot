from dydx3.constants import API_HOST_MAINNET, API_HOST_SEPOLIA

# dostep do zmiennych evniroment
from decouple import config

# !!! SELECR MODE
# DEVELOPMENT / PRODUCTION
MODE = "DEVELOPMENT"

# Clode all open positions and orders
ABORTY_ALL_POSITIONS = False

# Find Cointegrated Pairs
FIND_COINTEGRATED = True

# Place Trades
PLACE_TRADES = True

# Resulution
RESOLUTION = "1HOUR"

# Stats Window
WINDOW = 21

# Thresholds - Opening (Trade)
MAX_HALF_LIFE = 24
ZSCORE_THRESH = 1.5
USD_PER_TRADE = 50

# dla Testnest mamy okolo 2000$, w prawdziwej sieci  trzeba dac ile mamy gotowki w portfelu
USD_MIN_COLLATERAL = 1880

# Thresholds - Closing
CLOSE_AT_ZSCORE_CROSS = True

# adres publiczny portfela
ETHEREUM_ADDRESS = "0x8217B2DE4eB2C4F754cfda62Dc27fB93eA9BE736"

# uwaga uzycie z modulu decouple funkcji config, modul wie jak uzyc danych z pliku .env

# KEYS - Production
# Must be on be on Mainnet od DYDX
STARK_PRIVATE_KEY_MAINNET = config("STARK_PRIVATE_KEY_MAINNET")
DYDX_API_KEY_MAINNET = config("DYDX_API_KEY_MAINNET")
DYDX_API_SECRET_MAINNET = config("DYDX_API_SECRET_MAINNET")
DYDX_API_PASSPHRASE_MAINNET = config("DYDX_API_PASSPHRASE_MAINNET")

# KEYS - Development
# Must be on be on TestNet od DYDX
STARK_PRIVATE_KEY_TESTNET = config("STARK_PRIVATE_KEY_TESTNET")
DYDX_API_KEY_TESTNET = config("DYDX_API_KEY_TESTNET")
DYDX_API_SECRET_TESTNET = config("DYDX_API_SECRET_TESTNET")
DYDX_API_PASSPHRASE_TESTNET = config("DYDX_API_PASSPHRASE_TESTNET")

# KEYS - Export
STARK_PRIVATE_KEY = STARK_PRIVATE_KEY_MAINNET if MODE == "PRODUCTION" else STARK_PRIVATE_KEY_TESTNET
DYDX_API_KEY = DYDX_API_KEY_MAINNET if MODE == "PRODUCTION" else DYDX_API_KEY_TESTNET
DYDX_API_SECRET = DYDX_API_SECRET_MAINNET if MODE == "PRODUCTION" else DYDX_API_SECRET_TESTNET
DYDX_API_PASSPHRASE = DYDX_API_PASSPHRASE_MAINNET if MODE == "PRODUCTION" else DYDX_API_PASSPHRASE_TESTNET

print(STARK_PRIVATE_KEY)
print(DYDX_API_KEY)
print(DYDX_API_SECRET)
print(DYDX_API_PASSPHRASE)

# HOST -Export
HOST = API_HOST_MAINNET if MODE == "PRODUCTION" else API_HOST_SEPOLIA

# HTTP PROVIDER
HTTP_PROVIDER_MAINNET = "https://eth-mainnet.g.alchemy.com/v2/IQaJWpT1Bx7zdoDfwRYIGhiAsXRrddoI"
HTTP_PROVIDER_TESTNET = "https://eth-sepolia.g.alchemy.com/v2/bqh7WfHCKJpnLsvdjcjOwskxt_wRwdv5"

HTTP_PROVIDER = HTTP_PROVIDER_MAINNET if MODE == "PRODUCTION" else HTTP_PROVIDER_TESTNET

