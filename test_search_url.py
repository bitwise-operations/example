import search_url
import pytest

def test_check_status_url_for_page_google():
    a = search_url.SeachUrl()
    list_url = a.all_url_page('https://www.google.com/')
    result_url = a.status_page(list_url)
    statuses = [i for i in result_url.values()]
    assert False == (not 200 in b)
