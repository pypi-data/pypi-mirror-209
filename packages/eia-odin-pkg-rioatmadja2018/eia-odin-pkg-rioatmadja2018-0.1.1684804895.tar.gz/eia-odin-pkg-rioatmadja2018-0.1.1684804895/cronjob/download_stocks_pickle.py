#!/usr/bin/env python3
from eia.utils.aws_resources import get_file, write_logs, job_status
from eia.utils.credentials import load_credentials
import os
import logging
from botocore.exceptions import ClientError
import time
from datetime import datetime
from typing import List,Dict
import pandas as pd
import subprocess 

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
load_credentials()

def download_stock_objects():
    log_events: List = []
    job_start: str = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    log.debug(f"[ \033[92mOK\033[0m ] Job started at {job_start}")
    log_events.append({'timestamp': int(time.time() * 1000),
                       'message': f"Job Started at {job_start}"
                       })

    PADD_AREA: Dict = {'New York': 'PADD 1',
                       'Massachusetts': 'PADD 1',
                       'Ohio': 'PADD 2',
                       'Minnesota': 'PADD 2',
                       'Texas': 'PADD 3',
                       'Florida': 'PADD 3',
                       'Colorado': 'PADD 4',
                       'California': 'PADD 5',
                       'Washington': 'PADD 5'}

    try:

        log.debug(
            f"[ \033[92mOK\033[0m ] Downloading https://odin.s3.amazonaws.com/pickle_obj/sarimax_padd_area_weekly_gasoline_retail_price.pkl ...")
        log_events.append({'timestamp': int(time.time() * 1000),
                           'message': f"Downloading sarimax_padd_area_weekly_gasoline_retail_price.pkl at {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}"})

        computed_model: Dict = get_file(file_name="pickle_obj/sarimax_padd_area_weekly_gasoline_retail_price.pkl",
                                        bucket_name="gasprice-dataset",
                                        dst_path="/tmp/")

        stocks_df: 'DataFrame' = pd.read_pickle(computed_model.get('file_name'))
        stocks_df.columns = [" ".join(col.split("_")[1:]).title() for col in stocks_df.columns]
        for col in stocks_df.columns:
            file_name: str = f"pickle_obj/sarimax_crude_oil_stocks_{PADD_AREA.get(col).replace(' ', '').lower()}.pkl"
            log.debug(
                f"[ \033[92mOK\033[0m ] Downloading https://odin.s3.amazonaws.com/pickle_obj/{file_name} ...")
            log_events.append({'timestamp': int(time.time() * 1000),
                               'message': f"Downloading {file_name} at {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}"})

            get_file(file_name=file_name,
                     bucket_name="gasprice-dataset",
                     dst_path="/tmp")

        all_files: str = '\n'.join(['/tmp/%s' % (item) for item in os.listdir('/tmp/') if 'pkl' in item])
        job_status(job_title="Download completed",
                   msg=f"Your files are ready:\n{all_files}",
                   topic_arn="arn:aws:sns:us-east-1:193235400604:crude_oil_import")

        log_events.append({'timestamp': int(time.time() * 1000),
                           'message': f"Jobs completed at {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}"})

        for item in os.listdir("/tmp/"):
            if 'pkl' in item:
                log.debug(f"[ \033[92mOK\033[0m ] Changing Permission to -rw-rw-rw for /tmp/{item}")
                subprocess.Popen(f"chmod 666 /tmp/{item}", shell=True)

        write_logs(log_group_name="download_stocks_pickles",
                   log_events=log_events)

        log.debug(f"[ \033[92mOK\033[0m ] Job ends at {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}")

    except ClientError as e:
        job_status(job_title="Download Failed",
                   msg="Unable to retrieve the pickle objects, Please check your IAM credentials !!!",
                   topic_arn="arn:aws:sns:us-east-1:193235400604:download_failure")

        raise ClientError("[ERROR] Caught an exception ") from e
