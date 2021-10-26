from datetime import datetime, timedelta

def today():
    return datetime.today()

def antes_ayer():
    antes_ayer = datetime.today() - timedelta(days=2)   # Fecha lim inferior
    d1 = antes_ayer.strftime("%d.%m.%Y")
    return d1

def ayer():
    ayer = datetime.today() - timedelta(days=1) # Fecha lim superior
    d2 = ayer.strftime("%d.%m.%Y")
    return d2