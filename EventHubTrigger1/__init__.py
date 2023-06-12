from typing import List
import logging
import uuid
import json

import azure.functions as func

def main(events: List[func.EventHubEvent], eventsout: func.Out[str],cosmosout: func.Out[func.Document],adlsout: func.Out[str]):

     for event in events:
        logging.info('Python EventHub trigger processed an event: %s',            
        event.get_body().decode('utf-8'))

        # Output to EventHub
        eventsout.set(event.get_body().decode('utf-8'));

        # Output to CosmosDB
        data = {}
        data['id'] = str(uuid.uuid1())
        data['event'] = str(event.get_body().decode('utf-8'))
        cosmosout.set(func.Document.from_dict(data));

        # Output to ADLS
        adlsout.set(str(json.loads(event.get_body().decode('utf-8'))));
