from datetime import datetime
import random
import logging
import time
from google.cloud import storage
import json


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

def upload_to_gcs(bucket_name: str, data: dict, destination_blob_name: str):
    """
    Wysyla slownik jako plik json do gcs

    Args:
        bucket_name (str)
        data (dict)
        destination_blob_name (str)
    """
    storage_client = storage.Client.from_service_account_json('gcp-keys.json')
    
    bucket = storage_client.bucket(bucket_name)
    
    blob = bucket.blob(destination_blob_name)
    
    json_data_string = json.dumps(data)
    
    blob.upload_from_string(
          json_data_string
        , content_type = 'application/json'
        , timeout = 60
    )



    

if __name__ == '__main__':
    logging.info("Rozpoczynam generowanie informacji o akcjach i wyslanie do GCS")

    bucket_name = 'trading-bronze-2026'

    try:
        while True:

            event = generate_trade_event()
            clean_time = event["timestamp"].replace("-", "").replace(":", "").replace(" ", "_")
            file_name = f"{event['ticker']}_{clean_time}.json"

            logging.info(f"Generuję dane: {event}")
            
            upload_to_gcs(bucket_name, event, file_name)

            logging.info(f"Pomyślnie wysłano plik {file_name} do GCS.")
        
    except KeyboardInterrupt:

        logging.info("Zakonczenie programu")

        time.sleep(2)
