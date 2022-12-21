import re
from datetime import datetime


def email_validator(email):
    if re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
        return True
    else:
        return False


def date_validator(fecha):
  try:
    datetime.strptime(fecha,'%d/%m/%Y')
    return True
  except:
    return False


def name_validator(name):
  if re.match(r'^[a-zA-Z\s]+$',name) and len(name)>=3:
    return True
  else:
    return False
  