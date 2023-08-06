#!/usr/bin/env python3
from eia.utils.aws_resources import upload_file, job_status, write_logs
from eia.utils.credentials import load_credentials
from eia.utils.constants import INVERSE_STATES
import subprocess
import os
import time
import logging
from datetime import datetime
import json
import random
from typing import Dict, List
import pandas as pd
from sqlalchemy import create_engine

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

load_credentials()

def get_live_gasoline_pricess():

    log_name: str = "live_gasprice"
    log_events: List = []
    random.seed(123)
    wait_time: List = list(range(15,30))

    try:

        log_events.append({'timestamp': int(time.time() * 1000),
                           'message': f"[ OK ] Job Started at {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}"})

        for state in list(INVERSE_STATES.keys()):

            script: str = "/usr/bin/gasbuddy"
            output_file: str = "/tmp/%s_pricing.txt" % (state.lower())

            log.debug(f"[ \033[92mOK\033[0m ] Downloading output to {output_file}" )
            subprocess.Popen("%s %s > %s" % (os.path.join("/tmp/scripts",script), state, output_file ), shell=True)
            time.sleep(random.choice(wait_time))

            upload_file(file_name=output_file,
                        bucket_name="gasprice-dataset",
                        key_name=f"dataset/live_gasprice/{os.path.basename(output_file)}")

            log_events.append({'timestamp': int(time.time() * 1000),
                               'message': f"[ OK ] Uploading {INVERSE_STATES.get(state)} Gasoline Prices as {output_file} to s3 bucket at {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}"})
            subprocess.Popen("chmod 666 /tmp/*_pricing.txt", shell=True)

        for item in os.listdir("/tmp"):
            state: str = INVERSE_STATES.get(item.split("_")[0].upper())
            if "pricing.txt" in item:
                output_file = os.path.join("/tmp/", item)
                log.debug(f"[ \033[92mOK\033[0m ] Processing {output_file}")
                gasprice_hist: List = []
                streamed_data: Dict = open(output_file, "rb").read().decode('utf-8')

                if "Error 503 Backend fetch failed" in streamed_data:
                    log.debug(f"[ \033[91mERROR\033[0m ] Processing {output_file}")
                    log_events.append({'timestamp': int(time.time() * 1000),
                                       'message': f"[ ERROR ] {state} {output_file} at {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}.\n{streamed_data}"})
                    continue

                streamed_data = json.loads(streamed_data)

                for item in streamed_data.get('data').get('locationByArea').get('stations').get('results'):

                    current_data: Dict = {'gas_station': item.get('name'),
                                          'country': item.get('address').get('country'),
                                          'city': item.get('address').get('locality'),
                                          'address': item.get('address').get('line1', "N/A"),
                                          'zip_code': item.get('address').get('postalCode'),
                                          'state': item.get('address').get('region'),
                                          'regular_gas': 'regular_gas' in item.get('fuels'),
                                          'midgrade_gas': 'midgrade_gas' in item.get('fuels'),
                                          'premium_gas': 'premium_gas' in item.get('fuels'),
                                          'price_unit': item.get('priceUnit'),
                                          'star_rating': item.get('star_rating', "N/A"),
                                          'latitude': item.get('latitude'),
                                          'longitude': item.get('longitude')
                                          }

                    # at the same gas-station but different time and prices 2022-08-14T19:08:31.443Z
                    for price in item.get('prices'):

                        curr_gasstation: List = []
                        if price.get('cash'):
                            current_data = {**current_data,
                                            **{"timestamp": price.get('cash').get('posted_time', "N/A"),
                                               "price": price.get('cash').get('price', "N/A")
                                               }}

                            curr_gasstation.append(current_data)

                        if price.get('credit'):
                            current_data = {**current_data,
                                            **{"timestamp": price.get('credit').get('posted_time', "N/A"),
                                               "price": price.get('credit').get('price', "N/A")
                                               }}

                            curr_gasstation.append(current_data)

                    # reviews associated with the current gas-station at specific loc (lon,lat):
                    gasprice_hist.extend([{**item,
                                           **{'review': review.get('review'), 'review_date': review.get('reviewDate'),
                                              'sentiment_score': review.get('sentimentScore')}} for review in
                                          item.get('reviews').get('results') for item in curr_gasstation])

                historical_prices: 'DataFrame' = pd.DataFrame(gasprice_hist)
                current_report: str = "/tmp/%s_gasoline_prices_%s.csv" % (state ,datetime.utcnow().isoformat())
                historical_prices.to_csv(current_report)

                args: str = "mysql+pymysql://%s:%s@%s:3306/%s" % (
                    os.environ['MYSQL_USER'], os.environ['MYSQL_PASSWD'], os.environ['MYSQL_HOST'],
                    os.environ['MYSQL_DB'])

                engine: "MySQL" = create_engine(args)
                historical_prices.to_sql("live_gasoline_prices", con=engine, if_exists='append')

                upload_file(file_name=current_report,
                            bucket_name='gasprice-dataset',
                            key_name=os.path.join("live_gasoline_prices/", os.path.basename(current_report)))

                log_events.append({'timestamp': int(time.time() * 1000),
                                   'message': f"[ OK ] Uploading {current_report} to s3 bucket {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}"})

        log.debug(f"[ \033[92mOK\033[0m ] Job Completed ...")
        log_events.append({'timestamp': int(time.time() * 1000),
                           'message': f"[ OK ] Job Completed at {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}"})

        write_logs(log_group_name=log_name,
                   log_events=log_events)

        subprocess.Popen("rm /tmp/*.csv", shell=True)


    except ConnectionError as e:

        log_events.append({'timestamp': int(time.time() * 1000),
                           'message': f"[ OK ] Job Failed at {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}.\nCaught an exception {e}"})

        write_logs(log_group_name=log_name,
                   log_events=log_events)

        job_status(job_title="Failed to update ODIN DB",
                   msg=f"Job Failed at {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}.\nCaught an exception {e}",
                   topic_arn="arn:aws:sns:us-east-1:193235400604:download_failure")

        raise ConnectionError("Unable to retrieve data from https://gasbuddy.com. Please check your connections !!!") from e

if __name__ == "__main__":
    get_live_gasoline_pricess()
