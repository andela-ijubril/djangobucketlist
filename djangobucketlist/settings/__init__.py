import os
if not os.getenv('TRAVIS') and not os.getenv('HEROKU'):
    from django_envie.workroom import convertfiletovars
    convertfiletovars()
    from development import *

if os.getenv('HEROKU') is not None:
    from production import *