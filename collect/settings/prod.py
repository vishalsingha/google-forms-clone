from .base import *
from dotenv import load_dotenv

load_dotenv()

# CSRF_COOKIE_SECURE = False
# SECURE_SSL_REDIRECT  = False 
# SECURE_HSTS_SECONDS = 31536000
SECRET_KEY = 'dmvklfmv;mv;fnvdflvnklnvkdfmvvm;lvmvldfv,dfl;vdf'
# DEBUG = False if int(os.environ.get('DEBUG')) ==0 else True
DEBUG = True
ALLOWED_HOSTS = ['*']



# conf for OTP
# EMAIL_HOST = 'smtp.zoho.in'
# EMAIL_HOST_USER = 'authenticate@prepscope.com'
# EMAIL_HOST_PASSWORD = 'T0tp5525@5m1ilfor0tp'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_USE_SSL = False



# # conf for newslatter
# EMAIL_HOST_NWS = 'smtp.zoho.in'
# EMAIL_HOST_USER_NWS = 'newsletter@prepscope.com'
# EMAIL_HOST_PASSWORD_NWS = 'n5wsl5tt5r@5525for5m1il'
# EMAIL_PORT = 587