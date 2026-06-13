import json
from .tasks import handle_enrollment


def bulk_process(raw_data):
    """
    Function to process the raw data and create Enrollment records in bulk.
    """
    for item in raw_data:
        handle_enrollment.delay(item=json.dumps(item))
    return 1