
#!/usr/bin/env python3 
import os
from sqlalchemy import create_engine
from eia.utils.aws_resources import get_file, list_files, job_status, write_logs
from eia.utils.credentials import load_credentials
import sqlite3
import boto3
from datetime import datetime
import re
from typing import List, Dict
import pandas as pd
from botocore.exceptions import ClientError
import logging
import time

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

try:
    log_events: List = []
    log.debug(f"[ \033[92mOK\033[0m ] Updating Database")
    load_credentials()

    log_events.append({'timestamp': int(time.time() * 1000),
                       'message': f"[ OK ] Job Started at {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}"})

    engine = create_engine(f"mysql+pymysql://admin:{os.environ['MYSQL_PASSWD']}@{os.environ['MYSQL_HOST']}:3306/{os.environ['MYSQL_DB']}")
    s3_resources: List[str] = [ item.get('Key') for item in list_files(bucket_name='gasprice-dataset') if re.findall("dataset/crude_oil/.*.sqlite", item.get('Key')) ]

    message: str = "Updating the following ODIN-Table:\n"
    for sqllite_file in s3_resources:
        resp: Dict = get_file(file_name=sqllite_file, bucket_name='gasprice-dataset', dst_path="/tmp" )
        sqlite_con: 'sqlite3' = sqlite3.connect(resp.get('file_name'))

        for tbl_name in pd.read_sql("SELECT * FROM sqlite_master", con=sqlite_con)['tbl_name'].tolist():
            message += f"- {tbl_name}\n"
            log.debug(f"[ \033[92mOK\033[0m ] Updating {tbl_name} Table")
            log_events.append({'timestamp': int(time.time() * 1000),
                               'message': f"[ OK ] Updating {tbl_name} Table at {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}"})

            curr_df: 'DataFrame' = pd.read_sql("SELECT * FROM %s" % (tbl_name) , con=sqlite_con )
            curr_df.columns = [col.replace("-", "_") for col in curr_df.columns.tolist()]
            curr_df.to_sql(tbl_name, con=engine, if_exists='replace')

    write_logs(log_group_name="odin_db_update",
               log_events=log_events)

    timestamp: str = datetime.utcnow().strftime("%y-%m-%d %H:%M:%S")
    message += f"Finish Updating ODIN-DB at {timestamp}"

    job_status(job_title="Update ODIN-DB",
               msg=message,
               topic_arn="arn:aws:sns:us-east-1:193235400604:crude_oil_import")

except ClientError as e:

    job_status(job_title="Failed to update ODIN DB",
               msg=f"Job Failed at {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}.\nCaught an exception {e}",
               topic_arn="arn:aws:sns:us-east-1:193235400604:download_failure")
