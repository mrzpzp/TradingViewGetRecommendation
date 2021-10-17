from tradingview_ta import TA_Handler, Interval, Exchange
from datetime import date
import time


#Add your assets to the list

list  = [

{"SYMBOL": "BTCUSD", "SCREENER": "crypto", "EXCHANGE": "BINANCE" , "INTERVAL": Interval.INTERVAL_1_DAY},

{"SYMBOL": "AAPL", "SCREENER": "america", "EXCHANGE": "NASDAQ" , "INTERVAL": Interval.INTERVAL_1_DAY}

]


def main():
    for i in range(len(list)):
        SYMBOL = list[i]["SYMBOL"]
        SCREENER = list[i]["SCREENER"]
        EXCHANGE = list[i]["EXCHANGE"]
        INTERVAL = list[i]["INTERVAL"]

        asset = TA_Handler(
            symbol=SYMBOL,
            screener=SCREENER,
            exchange=EXCHANGE,
            interval=INTERVAL
        )
            
        asset_sum = asset.get_analysis().summary
        osc = asset.get_analysis().oscillators
        today = date.today()
        t = time.localtime()
        
        print("\n" , "RECOMMENDATION FOR" , SYMBOL , ":" , asset_sum["RECOMMENDATION"], "\n")
        print("   DETAILS: " , asset_sum, "\n")
        
            
        with open("result.txt", "a") as f:
            f.write(SYMBOL + "|"  + " RECOMMENDATION > " + asset_sum["RECOMMENDATION"]  + "\n" + " oscillators >> " + str(osc))
            f.write("\n\n" + today.strftime("   DATE ADDED > %d, %b %Y") + "\n" + time.strftime("   TIME ADDED > %H:%M:%S", t) + "\n\n\n")
        
        
        print(today.strftime(" DATE > %d, %b %Y"))
        print(time.strftime(" TIME > %H:%M:%S", t))
        
        print(f"\nAsset {SYMBOL} added to result.txt \n")
        

if __name__ == "__main__":
    
    try:
        main() 
        print(f"\nDONE")
        input()
        
    except Exception as e:
        print(e)