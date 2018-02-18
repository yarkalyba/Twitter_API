import urllib.request
import urllib.parse
import urllib.error
import twurl
import json
import ssl


def make_js(acct):
    """
    function gets a username and returns json with data about user

    param acct: username
    return: json with full data about twitter page of the user
    """

    TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '15'})
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    js = json.loads(data, encoding="UTF-8")

    return js
