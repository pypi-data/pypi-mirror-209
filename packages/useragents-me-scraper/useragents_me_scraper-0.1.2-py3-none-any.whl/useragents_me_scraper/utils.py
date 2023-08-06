from datetime import datetime, date, timedelta


def convert_str_to_date(str_date):
    """ Converts a string to a _Date object and returns it

    Returns
    -------
    _Date 
      Formatted date to YYYY-MM-DD format
    """
    return datetime.strptime(str_date, '%Y-%m-%d').date()


def get_week_timeframe():
    """ Returns two _Date values - start_date (today) and end_date (date 7 days after start_date)

    Returns
    -------
    _Date 
      The date today.
    _Date
      The date excatly 7 days after today.
    """
    start_date = date.today()
    end_date = start_date + timedelta(days=7)
    return start_date, end_date


def is_outdated(end_date):
    """ Returns true or false depending on whether the date today is past the end date argument or not.

    Parameters
    ----------
    end_date : str
      The date that the date today is going to be compared to

    Returns
    -------
    boolean
      True if the date is outdated. False if the date is not outdated.
    """

    end_date = convert_str_to_date(end_date)
    return date.today() > end_date
