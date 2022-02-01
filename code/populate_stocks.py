import sqlite3
import config
import alpaca_trade_api as tradeapi
import pandas as pd

connection = sqlite3.connect(config.DB_FILE)
connection.row_factory = sqlite3.Row
cursor = connection.cursor()


api = tradeapi.REST(config.API_KEY, config.SECRET_KEY, base_url=config.API_URL)


assets = api.list_assets()

print(assets)
'''
cursor.execute("""
        SELECT symbol, name FROM stock LIMIT 5""")
rows = cursor.fetchall()
symbols = [row['symbol'] for row in rows]
print(symbols)

'''
'''
cursor.execute("""
            SELECT * FROM stock""")
rows = cursor.fetchone()

'''
'''
# print(rows)
# for row in rows:
#   print(row['symbol'])

'''
'''
for asset in assets:

    try:
        if asset.status == 'active' and asset.tradable and asset.symbol not in symbols:
            print(f"Added a new stock {asset.symbol}{asset.name}")
            cursor.execute("INSERT INTO stock (symbol, name, exchange) VALUES (?, ?, ?)",
                           (asset.symbol, asset.name, asset.exchange))
    except Exception as e:
        print(asset.symbol)
        print(e)

connection.commit()
'''
