#!/usr/bin/env python3
import pandas as pd
import boto3
from eia.utils.aws_resources import get_file,write_logs
from eia.utils.credentials import load_credentials
import os
from typing import List
from sqlalchemy import create_engine
import logging
import time
from datetime import datetime

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

load_credentials()
log_name: str = "odin_db_update"
log_events: List = []

def get_lives_gasprices():
    try:

        log.debug(f"[ \033[92mOK\033[0m ] Retrieving gasprices from s3 buckets")
        log_events.append({'timestamp': int(time.time() * 1000),
                           'message': f"[ OK ] Job Started at {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}"})

        client: 's3' = boto3.client(service_name='s3',
                                    region_name='us-east-1',
                                    aws_access_key_id=os.environ['ODIN_KEY_ID'],
                                    aws_secret_access_key=os.environ['ODIN_SECRET_KEY'])

        gasprice_reports: 'DataFrame' = pd.DataFrame(
            client.list_objects_v2(Bucket="gasprice-dataset", Prefix="live_gasoline_prices", MaxKeys=10000).get("Contents")).sort_values(
            by="LastModified", ascending=False)

        log.debug(f"[ \033[92mDONE\033[0m ] Listing All CSVs Files")
        dir_path: str = "/mnt/gasprices"
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)

        # ingest data
        for csv in gasprice_reports[gasprice_reports["Key"].apply(lambda row: 'csv' in row)]['Key'].tolist():

            if not os.path.exists(os.path.join(dir_path, csv)):
                get_file(file_name=csv,
                         bucket_name="gasprice-dataset",
                         dst_path=dir_path)

                log.debug(f"[ \033[92mDONE\033[0m ] downloading {csv}")

        log_events.append({'timestamp': int(time.time() * 1000),
                           'message': f"[ DONE ] Downloading All CSVs Files {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}"})

        log_events.append({'timestamp': int(time.time() * 1000),
                           'message': f"[ OK ] Merging All CSVs Files {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}"})

        merged_reports: List = []
        for gasprice_report in os.listdir(dir_path):

            curr_df: 'DataFrame' = pd.read_csv(os.path.join(dir_path, gasprice_report))
            curr_df.drop([col for col in curr_df.columns.tolist() if "Unnamed" in col], inplace=True, axis=1)
            merged_reports.extend(curr_df.to_dict(orient='records'))
            log.debug(f"[ \033[92mDONE\033[0m ] merging {gasprice_report}")

        log_events.append({'timestamp': int(time.time() * 1000),
                           'message': f"[ DONE ] Merging All CSVs Files {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}"})

        report_df: 'DataFrame' = pd.DataFrame(merged_reports).drop_duplicates()
        args: str = "mysql+pymysql://%s:%s@%s:3306/%s" % (
        os.environ['MYSQL_USER'], os.environ['MYSQL_PASSWD'], os.environ['MYSQL_HOST'], os.environ['MYSQL_DB'])
        engine: "MySQL" = create_engine(args)
        report_df.to_sql("live_gasoline_prices", con=engine, if_exists='replace')

        log_events.append({'timestamp': int(time.time() * 1000),
                           'message': f"[ DONE ] Job completed at {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}"})

        write_logs(log_group_name=log_name,
                   log_events=log_events)
        log.debug(f"[ DONE ] Job completed at {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}")

    except ConnectionError as e:

        log_events.append({'timestamp': int(time.time() * 1000),
                           'message': f"[ ERROR ] Merging All CSVs Files {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}.\nCaught an exceptions {e}"})

        write_logs(log_group_name=log_name,
                   log_events=log_events)

        raise ConnectionError(f"[ ERROR ] Caught an exceptions {e}") from e

if __name__ == "__main__":
    get_lives_gasprices()