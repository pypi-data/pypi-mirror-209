import json
import requests
from useragents_me_scraper import utils
from bs4 import BeautifulSoup

FILENAME = 'ua_cache.json'
URL = "https://www.useragents.me/"


def _save_ua_cache(ua_processed_json):
    """ Saves the UA data into a json file.

    Parameters
    ----------
    ua_processed_json : dict 
      Processed ua containing start_date, end_date, and content (list of uas, pcts).
    """
    with open(FILENAME, 'w') as outfile:
        json.dump(ua_processed_json, outfile)


def _is_existing_ua_cache():
    """ Returns true or false depending on whether a ua_cache.json exists in the local space or not.

    Returns
    -------
    boolean
      True if the ua_cache.json exists. False if the ua_cache.json does not exist.
    """
    existing_flag = False

    try:
        f = open('ua_cache.json')
        f.close()
    except:
        existing_flag = False

    return existing_flag


def _is_outdated_ua_cache():
    """ Returns true or false depending on whether the date today is past beyond the end_date in ua_cache.json.

    Returns
    -------
    boolean
      True if the ua_cache is outdated. False if the ua_cache is not outdated.
    """
    outdated_flag = True

    with open(FILENAME, 'r') as f:
        ua_data = json.load(f)
        outdated_flag = utils.is_outdated(ua_data['end_date'])

    return outdated_flag


def _scrape_ua_me():
    """ Returns true or false depending on whether the date today is past the end date argument or not.

    Returns
    -------
    list
      List of the raw scraped ua-pct dictionary key-value pairs scraped from useragents.me.
    """
    r = requests.get(URL)

    content = BeautifulSoup(r.content, 'html5lib')

    common_div = content.find(id="most-common-desktop-useragents-json-csv")
    common_user_agents = common_div.div.textarea.string
    ua_raw_json = json.loads(common_user_agents)

    return ua_raw_json


def _process_ua(ua_raw_json):
    """ Processes ua_raw_json by adding start_date, end_date, and nesting raw ua data inside the list content key.

    Parameters
    ----------
    ua_raw_json : 
      List of the raw scraped ua-pct dictionary key-value pairs scraped from useragents.me.

    Returns
    -------
    dict
        A dictionary with start_date, end_date, and content with ua-pct key-value pairs. 
    """
    start_date = utils.date.today()
    end_date = start_date + utils.timedelta(days=7)

    ua_processed_json = {
        "start_date": str(start_date),
        "end_date": str(end_date),
        "content": ua_raw_json
    }

    return ua_processed_json


def _is_valid_pct(pct, min_pct, max_pct):
    """ Returns true or false on whether the pct is within the min_pct and max_pct valid range.

    Parameters
    ----------
    pct : float
      The pct of a given useragent.
    min_pct: float
      Min range for the pct.
    max_pct: float
      Max range for the pct.

    Returns
    -------
    boolean
      True if pct is within the range. False if pct is outside the range.
    """
    return pct >= min_pct and pct <= max_pct


def _contains_valid_substring(substring_list, ua_string):
    """ Returns true or false depending on whether no substring_list was specified or any keyword inside substring_list is found within the ua_string.

    Parameters
    ----------
    substring_list : list
      A list containing all keywords to be searched.
    ua_string : string
      A useragent string to be searched with keywords for.

    Returns
    -------
    boolean
      True if no substring_list specified or a keyword matched within ua_string. False no keyword matched the ua_string.
    """
    return len(substring_list) == 0 or any(keyword in ua_string for keyword in substring_list)


def get_uas(head=None, min_pct=0.0, max_pct=100.0, substring_list=[], cache=True):
    """ Returns true or false depending on whether the date today is past the end date argument or not.

    Parameters
    ----------
    head : int
      The date that the date today is going to be compared to
    min_pct: float
      Min range for the pct.
    max_pct: float
      Max range for the pct.
    substring_list : list
      A list containing all keywords to be searched and matched on useragents.
    cache : boolean
      A flag for either caching the scraped to a ua_cache.json file that has a weeklong lifetime, or directly scraping the site. 

    Returns
    -------
    list
      The list of useragents filtered according to the specifications passed.
    """
    retrieved_uas = []

    # If cache does not exist or is outdated
    if not _is_existing_ua_cache() or _is_outdated_ua_cache():
        # Process/Format
        ua_raw_json = _scrape_ua_me()
        ua_processed_json = _process_ua(ua_raw_json)
        # Save
        if cache:
            _save_ua_cache(ua_processed_json)
        else:
            ua_data = ua_processed_json

    # Loading the data
    if cache:
        with open('ua_cache.json', 'r') as f:
            ua_data = json.load(f)

    for ua in ua_data['content']:
        # Filter according to pct and substring
        if _is_valid_pct(ua['pct'], min_pct, max_pct) and _contains_valid_substring(substring_list, ua['ua']):
            retrieved_uas.append(ua['ua'])
        # Filter according to head
        if head != None and len(retrieved_uas) == head:
            break

    return retrieved_uas
