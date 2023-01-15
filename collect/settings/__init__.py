import os 
from dotenv import load_dotenv

load_dotenv()


from .dev import *
# if os.environ.get('WEBSITE_MODE') == 'prod':
#     from .prod import *
# else:
#     from .dev import *