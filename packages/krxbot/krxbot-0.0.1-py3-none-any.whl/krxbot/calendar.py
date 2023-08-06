import datetime


def now():
    """Return the current korean date and time.

    :return: datetime.datetime
    """
    tz = datetime.timezone(datetime.timedelta(hours=9))
    dt = datetime.datetime.now(tz=tz)

    return dt


def is_weekend(dt):
    """Return whether it is weekend or not.

    :param dt: datetime.datetime
    :return: bool
    """
    week = dt.weekday()

    if week >= 5:
        return True
    else:
        return False


def is_holiday(dt):
    """NotImplemented

    :param dt: datetime.datetime
    :return: bool
    """
    return False


def is_trading_day(dt):
    """Return whether it is a trading day or not.

    :param dt: datetime.datetime
    :return: bool
    """
    if is_weekend(dt) or is_holiday(dt):
        return False
    else:
        return True
