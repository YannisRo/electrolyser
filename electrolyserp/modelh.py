import logging
logging.basicConfig(level=logging.DEBUG)
import time

def runf():
    start = time.time()

    logging.info("...start calculation")
    #do something
    #print("something")
    end = time.time()
    elapsed = end - start
    print(elapsed)


runf()

