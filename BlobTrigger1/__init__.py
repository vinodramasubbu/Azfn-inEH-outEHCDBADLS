import logging

import azure.functions as func


def main(myblob: func.InputStream,myblobout: func.Out[func.InputStream]):
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes")
    #outputDocument.set(func.Document.from_dict({"id": id, "activity": name}))
    myblobout.set(myblob.read())