import logging
logging.basicConfig(filename='test3.log',level=logging.INFO,format='%(levelname)s %(asctime)s %(name)s %(message)s')

def devide(a,b):
    logging.info('the number entered by user id %s and %s', a,b)
    try:
        logging.info("we are into function")
        div = a/b
        logging.info("we have completed a division operation")
        logging.info('the result of code is %s',div)
        return div
    except Exception as e:
        logging.exception(e)


((devide(3,9)))