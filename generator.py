from datetime import datetime
import random
import logging
import time

logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)

def generate_trade_event():
    """
    Generuje symulowane zdarzenia tradingowe.

    Funkcja zbiera obecny timestamp, hardcodowanego tickera w tym przypadku "AAPL" oraz wartosc akcji w przedziale 102-250

    Returns:
        dict: Slownik zawierajacy szczegoly tradingowe:
            - timestamp (str)
            - ticker (str)
            - value (int)
    """

    now = datetime.now()
    purchase_date = now.strftime("%Y-%m-%d %H:%M:%S")

    json_file = {"timestamp": purchase_date, "ticker": "AAPL", "price": random.randint(102, 250)}

    return json_file


    

if __name__ == '__main__':
    logging.info("Rozpoczynam generowanie informacji o akcjach...")

    try:
        while True:
            logging.info(f"Obecne wartosci: \n {generate_trade_event()}")

            time.sleep(2)
        
    except KeyboardInterrupt:

        logging.info("Zakonczenie programu")