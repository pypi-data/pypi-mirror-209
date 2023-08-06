import logol
from logol import get_print_debug, get_logger

logol.BASE_PATH = '.'
print(logol.BASE_PATH)
print, debug = get_print_debug(__file__)
print('Olá mundo!')
debug('Olá arquivo!')

log = get_logger('test', 'test.log', 1)
log.debug('Debung')
log.info('Information')
log.warning('Warning')
try:
    1/0
except ZeroDivisionError:
    log.exception('Exception')
log.error('Error')
log.critical('Critical')

log2 = get_logger('test', 'test.log', force=True)
log2.info('Log reconfigurado')

log3 = get_logger('test', 'test.log')