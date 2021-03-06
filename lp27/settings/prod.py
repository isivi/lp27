from .base import *

DEBUG = False

ALLOWED_HOSTS += [
    'goodjobs.isivi.pl',
    'goodjobs.pl'
]

FUNCTIONS['ANALYTICS_TRACKING_SCRIPT'] = True
FUNCTIONS['HOTJAR_TRACKING_SCRIPT'] = True


# Compressor

# css and js compressing active
COMPRESS_ENABLED = True
COMPRESS_PRECOMPILERS += PROD_LESS_PRECOMPILER

# NOTE:
# If any css/js production only issues should take place, this is the first place to check.
COMPRESS_CSS_FILTERS = PROD_COMPRESS_CSS_FILTERS
COMPRESS_JS_FILTERS = PROD_COMPRESS_JS_FILTERS
