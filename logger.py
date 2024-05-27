import logging

logger = logging.getLogger('main')
logger.setLevel(logging.DEBUG)

handler = logging.FileHandler('logs.log', 'a')
handler.setLevel(logging.DEBUG)

handler2 = logging.StreamHandler()
handler2.setLevel(logging.DEBUG)

formater = logging.Formatter('[%(asctime)s][%(levelname)s] %(message)s')
handler.setFormatter(formater)
logger.addHandler(handler)

handler2.setFormatter(formater)
logger.addHandler(handler2)


