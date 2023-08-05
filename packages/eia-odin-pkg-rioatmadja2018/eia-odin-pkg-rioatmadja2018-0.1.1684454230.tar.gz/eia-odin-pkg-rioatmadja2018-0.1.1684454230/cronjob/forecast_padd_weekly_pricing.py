#!/usr/bin/env python3
import boto3
from eia.utils.aws_resources import write_logs, job_status, upload_file
from eia.utils.credentials import load_credentials
from datetime import datetime
import time
import logging
import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.stats.diagnostic import acorr_ljungbox
from collections import defaultdict
import os
import pymysql
from typing import List

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


def forecast_weekly_gasoline_retail_price():
    log_events: List = []

    try:
        sns_topic_arn: str = "arn:aws:sns:us-east-1:193235400604:forecast"
        start_job: str = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        log_events.append({'timestamp': int(time.time() * 1000),
                           'message': f"[ OK ] Job Started at {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}"})

        cred_status: bool = load_credentials()
        log_group_name: str = "forecast_gasoline_weekly_retail_price"

        con: 'MySQL' = pymysql.connect(user=os.environ["MYSQL_USER"],
                                       password=os.environ["MYSQL_PASSWD"],
                                       host=os.environ["MYSQL_HOST"],
                                       db=os.environ["MYSQL_DB"])

        tbl_names: List[str] = list(
            list(pd.read_sql("SHOW TABLES LIKE '%pricing%' ", con=con).to_dict().values())[0].values())
        report: defaultdict = defaultdict(list)

        for tbl in tbl_names:
            log_events.append({'timestamp': int(time.time() * 1000),
                               'message': f"[ OK ] Computing SARIMAX For {tbl} at {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}"})

            padd_df: "DataFrame" = pd.read_sql("SELECT * FROM %s" % (tbl), con=con)
            padd_df['period'] = pd.to_datetime(padd_df['period'])
            log.debug(f"[ \033[92mOK\033[0m ] Computing SARIMAX FOR {tbl}")

            endog: 'Series' = padd_df.set_index("period").sort_index()["2022":]['value']
            model: SARIMAX = SARIMAX(endog=endog,
                                     order=(1, 1, 2),
                                     seasonal_order=(1, 0, 0, 7),
                                     simple_differencing=False).fit()

            ljungbox_test: List[int] = acorr_ljungbox(model.resid, lags=10)['lb_pvalue'].tolist()
            log_events.append({'timestamp': int(time.time() * 1000),
                               'message': f"AIC: {model.aic}: LJungbox: {ljungbox_test}"
                               })

            log.debug(f"[ \033[92mOK\033[0m ] AIC{model.aic} LJungbox:{ljungbox_test}")
            log_events.append({'timestamp': int(time.time() * 1000),
                               'message': f"[ OK ] Finished Computing SARIMAX For {tbl} at {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}"})

            report[tbl].append({'aic': model.aic,
                                'ljungbox': ljungbox_test,
                                'model': model
                                })

        con.close()

        finished_time: str = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        log_events.append({'timestamp': int(time.time() * 1000),
                           'message': f"[ OK ] Job finished at {finished_time}"})

        pkl_file: str = "/tmp/sarimax_padd_area_weekly_gasoline_retail_price.pkl"
        pd.DataFrame(report).to_pickle(pkl_file)
        upload_file(file_name=pkl_file,
                    bucket_name="gasprice-dataset",
                    key_name=os.path.join("pickle_obj/", os.path.basename(pkl_file)))

        log_events.append({'timestamp': int(time.time() * 1000),
                           'message': f"Pickle Object uploaded at https://gasprice-dataset.s3.amazonaws.com/pickle_obj/%s: {os.path.basename(pkl_file)}"
                           })

        write_logs(log_group_name=log_group_name, log_events=log_events)

        message: str = f"Dry Run Job finished at {finished_time}\n"
        for tbl, item in report.items():
            message += "%s %s\n" % (tbl, item)

        message += f"Pickle Object uploaded at https://gasprice-dataset.s3.amazonaws.com/pickle_obj/{os.path.basename(pkl_file)}"

        job_status(job_title="Forecast PADD Area Weekly Gasoline Retail Price",
                   msg=message,
                   topic_arn=sns_topic_arn)

    except ConnectionError as e:

        job_status(job_title="Forecast PADD Area Weekly Gasoline Retail Price",
                   msg=f"Job Failed at {finished_time}.\nCaught an exception {e}",
                   topic_arn=sns_topic_arn)

        raise ConnectionError("[ERROR] Caught an exception ") from e
