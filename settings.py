import os

HEALTH_INTEVAL_TIME = 60

HOST= "127.0.0.1" 
#os.environ.get("WEHA_APP_HOST")

PORT= "8000"
#os.environ.get("WEHA_APP_PORT")

MANAGER_ADDRESS = os.environ.get("WEHA_API_HOST")

MANAGER_PORT = os.environ.get("WEHA_API_PORT")

DJANGO_SERVER_PATH = ''

SECRET_KEY = 'n(bd1f1c%e8=_xad02x5qtfn%wgwpi492e$8_erx+d)!tpeoim'

APP_NAME = 'sample'

HEALTH_PATH = 'health/report/'

IGNORE_API = True

MF_USERNAME = os.environ.get("WEHA_API_USERNAME")

MF_PASSWORD = os.environ.get("WEHA_API_PASSWORD")

INSTALLED_SERVICES = ('calculator.AddService','calculator.MultService')

NO_THREADING = False
