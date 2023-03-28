from flask import Blueprint, jsonify
from app.models.store_status import StoreStatus

get_top_10 = Blueprint('get_top_10', __name__)

@get_top_10.route('/top10', methods=['GET'])
def fetch_top_10():
    top_10 = StoreStatus.query.limit(10).all()
    result = []
    for row in top_10:
        result.append({
            "store_id": row.store_id,
            "status": row.status,
            "timestamp_utc": str(row.timestamp_utc)
        })
    return jsonify(result)