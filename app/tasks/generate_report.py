from app import celery, db
from app.models import Report
from app.models import StoreStatus

from datetime import datetime

import pandas as pd

@celery.task(name="generate_report_task", bind=True, max_retries=3, default_retry_logic=10)
def generate_report_task(report_id):
    report = Report.query.get(report_id)
    header = ['store_id', 'uptime_last_hour', 'uptime_last_day', 'update_last_week', 'downtime_last_hour', 'downtime_last_day', 'downtime_last_week']
    file_path = f'./../../out/{report_id}.csv'
    report.start_time = datetime.utcnow()
    report.status = 'STARTED'
    db.session.commit()

    # generate the report
    all_unique_stores = StoreStatus.query.with_entities(StoreStatus).distinct().all()
    store_ids = set([tokens[0] for tokens in all_unique_stores])

    report_data = []

    for store_id in store_ids:
        # generate output for each store
        # TODO: To be implmented
        output = []
        # after generation of output for each data
        report_data.append([store_id].extend(output))
    pd.DataFrame(report_data).to_csv(file_path, header=header)

    report.status = 'COMPLETED'
    report.end_time = datetime.utcnow()
    report.file_path = file_path
    db.session.commit()
