import pandas as pd

from app import logger, create_app
from app import db
from app.models.store_status import StoreStatus
from app.models.working_hours import WorkingHours
from app.models.store_timezone import StoreTimezone

app = create_app()
with app.app_context():

    db.create_all()

    # read all three files and insert them into DB for later processing
    logger.info("[Store Status] going to load the given data for testing...")
    store_status = pd.read_csv(r"data\store status.csv")
    logger.info("[Store Status] successfully loaded in memory")

    count = 0
    for row in store_status.itertuples():
        count += 1
        status = StoreStatus(row.store_id, row.status, row.timestamp_utc)
        db.session.add(status)
        if count % 1000000 == 0:
            logger.info(f'Total rows inserted so far: {count}')
    logger.info('[Store Status] Commiting changes into the DB')
    db.session.commit()
    logger.info('[Store Status] Commit complete')


    working_hours = pd.read_csv(r"data\Menu hours.csv")
    logger.info("[Working Hours] read successfully")

    count = 0
    for row in working_hours.itertuples():
        count += 1
        hours = WorkingHours(row.store_id, row.day, row.start_time_local, row.end_time_local)
        db.session.add(hours)
        if count % 1000 == 0:
            logger.info(f'Total rows inserted so far: {count}')
    logger.info('[Working Hours] Commiting changes into the DB')
    db.session.commit()
    logger.info('[Working Hours] Commit complete')


    timezones = pd.read_csv(r"data\bq-results-20230125-202210-1674678181880.csv")
    logger.info("[Timezones] read successfully")

    count = 0
    for row in timezones.itertuples():
        count += 1
        tz = StoreTimezone(row.store_id, row.timezone_str)
        db.session.add(tz)
        if count % 1000 == 0:
            logger.info(f'Total rows inserted so far: {count}')
    logger.info('[Timezones] Commiting changes into the DB')
    db.session.commit()
    logger.info('[Timezones] Commit complete')
    