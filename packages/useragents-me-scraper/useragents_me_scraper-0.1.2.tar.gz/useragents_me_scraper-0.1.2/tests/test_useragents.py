from useragents_me_scraper import useragents as ua


def test_process_ua():
    test_ua_json = '[{"ua":"Mozilla\/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/111.0.0.0 Safari\/537.36","pct":36.47},{"ua":"Mozilla\/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/112.0.0.0 Safari\/537.36","pct":24.17},{"ua":"Mozilla\/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/109.0.0.0 Safari\/537.36","pct":5.47}]'
    test_processed_ua = ua._process_ua(test_ua_json)
    test_content = test_ua_json
    test_start_date, test_end_date = ua.utils.get_week_timeframe()

    assert(ua.utils.convert_str_to_date(test_processed_ua['start_date']) == test_start_date and
           ua.utils.convert_str_to_date(test_processed_ua['end_date']) == test_end_date and
           test_processed_ua['content'] == test_content)


def test_is_valid_pct_int():
    assert ua._is_valid_pct(50, 0, 100) == True


def test_is_not_valid_pct_int():
    assert ua._is_valid_pct(0, 50, 100) == False


def test_is_valid_pct_float():
    assert ua._is_valid_pct(50.5, 50.0, 50.9) == True


def test_is_not_valid_pct_float():
    assert ua._is_valid_pct(50.0, 60.9, 70.9) == False


def test_contains_valid_substring_empty():
    test_ua = 'Mozilla\/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/111.0.0.0 Safari\/537.36'
    substring_list = []
    assert ua._contains_valid_substring(substring_list, test_ua) == True


def test_contains_valid_substring_true_single():
    test_ua = 'Mozilla\/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/111.0.0.0 Safari\/537.36'
    substring_list = ['AppleWebKit']
    assert ua._contains_valid_substring(substring_list, test_ua) == True


def test_contains_valid_substring_true_multiple():
    test_ua = 'Mozilla\/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/111.0.0.0 Safari\/537.36'
    substring_list = ['10.0', 'Windows', 'Safari', '537.36']
    assert ua._contains_valid_substring(substring_list, test_ua) == True


def test_contains_valid_substring_false():
    test_ua = 'Mozilla\/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/111.0.0.0 Safari\/537.36'
    substring_list = ['5347']
    assert ua._contains_valid_substring(substring_list, test_ua) == False
