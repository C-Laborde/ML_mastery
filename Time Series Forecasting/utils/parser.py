from datetime import datetime


def parser(x):
    return datetime.strptime('200'+x, '%Y-%m')
