CURRENCIES = ["USD", "EUR", "CLP"]

STABLE_COINS = ["DAI", "USDT"]

COINS = [
    "BTC",
    "ETH",
    "LTC",
    "XRP",
    "BCH",
    "TRX",
    "DASH",
    "XLM",
    "EOS",
    "DOT",
]

BALANCE_COINS = [*COINS, *STABLE_COINS, *CURRENCIES]


KRAKEN_MINIMUM = {
    "AAVE": 0.05,
    "ALGO": 15,
    "ANT": 2,
    "REP": 0.3,
    "REPV2": 0.3,
    "BAL": 0.3,
    "BAT": 30,
    "XXBT": 0.0002,
    "XBT": 0.0002,
    "BCH": 0.02,
    "ADA": 25,
    "LINK": 0.5,
    "COMP": 0.05,
    "ATOM": 1,
    "CRV": 10,
    "DAI": 5,
    "DASH": 0.05,
    "EOS": 2.5,
    "XETH": 0.005,
    "ETH": 0.005,
    "ETH2.S": 0.02,
    "XLTC": 0.05,
    "LTC": 0.05,
    "XXRP": 20,
    "XRP": 20,
    "XXLM": 20,
    "XLM": 20,
    "USDT": 5,
    "TRX": 250,
    "DOT": 0.2,
}

MINIMUM_TO_TRADE = {"kraken": KRAKEN_MINIMUM}

CEROS = {
    "USDT": 8,
    "BTC": 8,
    "DAI": 8,
    "ETH": 8,
    "BNB": 8,
    "LTC": 8,
    "BCH": 8,
    "CHA": 8,
    "LUK": 8,
    "DASH": 8,
    "XLM": 7,
    "XRP": 6,
    "TRX": 6,
    "DOT": 8,
    "CLP": 0,
    "EOS": 4,
    "USD": 2,
    "EUR": 2,
    "POL": 4,
}


KRAKEN_RENAME_COINS = {
    "XXBT": "BTC",
    "XBT": "BTC",
    "XETH": "ETH",
    "ETH": "ETH",
    "DASH": "DASH",
    "ZUSD": "USD",
    "USD": "USDT",
    "USDT": "USDT",
    "XXRP": "XRP",
    "XRP": "XRP",
    "XXLM": "XLM",
    "XLM": "XLM",
    "XLTC": "LTC",
    "LTC": "LTC",
    "DAI": "DAI",
    "BCH": "BCH",
    "TRX": "TRX",
    "EOS": "EOS",
    "ZEUR": "EUR",
    "PAXG": "PAX",
    "DOT": "DOT",
    "USDC": "USDC",
}

KRAKEN_RENAME_PAIRS = {
    "XXLMZUSD": "XLM/USD",
    "EOSUSDT": "EOS/USDT",
    "TRXUSD": "TRX/USDT",
    "XRPUSDT": "XRP/USDT",
    "XBTUSDT": "BTC/USDT",
    "ETHUSDT": "ETH/USDT",
    "DASHUSD": "DASH/USD",
    "XLTCUSDT": "LTC/USDT",
    "LTCUSDT": "LTC/USDT",
    "BCHUSDT": "BCH/USDT",
    "USDTZUSD": "USDT/USD",
    "DAIUSDT": "DAI/USDT",
    "XXBTZUSD": "BTC/USD",
    "XETHZUSD": "ETH/USD",
    "PAXGUSD": "PAX/USDT",
    "DOTUSDT": "DOT/USDT",
    "EOSUSD": "EOS/USD",
    "DAIUSD": "DAI/USD",
    "USDTEUR": "USDT/EUR",
    "XXBTZEUR": "BTC/EUR",
    "USDCUSD": "USDC/USD",
    "USDCUSDT": "USDC/USDT",
}

KRAKEN_RENAME_COINS_INV = {v: k for k, v in KRAKEN_RENAME_COINS.items()}

ORIONX_RENAME_COINS = {
    "BTC": "BTC",
    "ETH": "ETH",
    "DASH": "DASH",
    "DAI": "DAI",
    "USDT": "USDT",
    "LTC": "LTC",
    "XRP": "XRP",
    "BCH": "BCH",
    "TRX": "TRX",
    "XLM": "XLM",
    "EOS": "EOS",
}

ORIONX_RENAME_COINS_INV = {v: k for k, v in ORIONX_RENAME_COINS.items()}

LOANS_RENAME_COINS = {
    "BTC": "BTC",
    "ETH": "ETH",
    "DASH": "DASH",
    "DAI": "DAI",
    "USDT": "USDT",
    "LTC": "LTC",
    "XRP": "XRP",
    "BCH": "BCH",
    "TRX": "TRX",
    "XLM": "XLM",
    "EOS": "EOS",
}

LOANS_RENAME_COINS_INV = {v: k for k, v in LOANS_RENAME_COINS.items()}

BINANCE_RENAME_COINS = {"BTC": "BTC"}

BINANCE_RENAME_COINS_INV = {v: k for k, v in BINANCE_RENAME_COINS.items()}

RENAME_COINS = {
    "kraken": KRAKEN_RENAME_COINS,
    "orionX": ORIONX_RENAME_COINS,
    "loans": LOANS_RENAME_COINS,
    "binance": BINANCE_RENAME_COINS,
}

RENAME_COINS_INV = {
    "kraken": KRAKEN_RENAME_COINS_INV,
    "orionX": ORIONX_RENAME_COINS_INV,
    "loans": LOANS_RENAME_COINS_INV,
    "binance": BINANCE_RENAME_COINS_INV,
}

KRAKEN_FEE = 0.0016
