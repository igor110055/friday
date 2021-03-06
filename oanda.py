import requests
import pandas as pd
import config
import utils


class OandaAPI():

    def __init__(self):
        self.session = requests.Session()    

    def fetch_instruments(self):
        url = f"{config.OANDA_URL}/accounts/{config.ACCOUNT_ID}/instruments"
        response = self.session.get(url, params=None, headers=config.SECURE_HEADER)
        return response.status_code, response.json()

    def get_instruments_df(self):
        code, data = self.fetch_instruments()
        if code == 200:
            df = pd.DataFrame.from_dict(data['instruments'])
            return df[['name', 'type', 'displayName', 'pipLocation', 'marginRate']]
        else:
            return None
    
    def save_instruments(self):
        df = self.get_instruments_df()
        if df is not None:
            df.to_pickle(utils.get_instruments_data_filename())

    def fetch_candles(self, pair_name, count, granularity):
        url = f"{config.OANDA_URL}/instruments/{pair_name}/candles"

        params = dict(
            count = count,
            granularity = granularity,
            price = "MBA"
        )

        response = self.session.get(url, params=params, headers=config.SECURE_HEADER)

        return response.status_code, response.json()


# if __name__ == "__main__":
#     api = OandaAPI()

#     historical_data = api.fetch_candles('EUR_USD', 5, 'H4')

#     #candles = historical_data[1]['candles']

#     #instrument = historical_data[1]['instrument']
#     print(historical_data[1])
    
#     #this for loops loops through all of the candle in the historical data
#     for data_point in historical_data[1]['candles']:

#         #the data of the candlestick
#         #date = data_point['time']

#         #the bid of the candlestick
#         #bid = data_point['bid']

#         print(data_point)
#     #api.save_instruments()