from espmeter.settings.local_settings import *
try:
    from local_settings import *
except ImportError:
    try:
        from production import *
    except ImportError:
        from espmeter.settings.base import *
