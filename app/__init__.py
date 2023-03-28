from flask import Flask
from celery import Celery
from flask_sqlalchemy import SQLAlchemy

import logging

logger = logging.getLogger(__name__)
db = SQLAlchemy()

from .models.report import Report
from .models.store_status import StoreStatus
from .models.store_timezone import StoreTimezone
from .models.working_hours import WorkingHours

celery = Celery(__name__) # ), broker=app.config["CELERY_BROKER_URL"])

from app import tasks

def create_app(Config):
    app = Flask(__name__)

    app.config.from_object(Config)
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    
    log_foramt = "%(asctime)s [%(levelname)s] %(message)s"
    logging.basicConfig(filename = 'app.log', level=logging.DEBUG, format=log_foramt)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    celery.conf.update(app.config)

    from app.routes.trigger_report import trigger_report
    from app.routes.get_report import get_report
    from app.routes.fetch_top_10 import get_top_10

    app.register_blueprint(trigger_report)
    app.register_blueprint(get_report)
    app.register_blueprint(get_top_10)

    return app