from base import *
try:
    from local_settings import *
except ImportError:
    try:
        from production import *
    except ImportError:
        from base import *
