import ta

from ta.momentum import RSIIndicator, StochRSIIndicator

class TechnicalAnalysis():

    def __init__(self):
        pass
    

    #this function calculates the rsi of a certain timeframe, the input is the dataframe and lenght desired
    def rsi(self, df_close):

        rsi = RSIIndicator(df_close, window = 14).rsi()
        
        return rsi

    def stoch_rsi(self, df_close):

        stoch_rsi = StochRSIIndicator(df_close, window = 14).stochrsi

        return stoch_rsi