import json
from .tasks import handle_enrollment


def bulk_process(raw_data, chunk_size=500):
    """
    Function to process the raw data and create Enrollment records in bulk.
    Chunks the data to improve scalability and reduce task overhead.
    """
    for i in range(0, len(raw_data), chunk_size):
        chunk = raw_data[i : i + chunk_size]
        handle_enrollment.delay(items=json.dumps(chunk))
    return 1