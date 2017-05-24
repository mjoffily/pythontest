
import urllib2
import time
import hmac
import hashlib

apikey = '86753166601e4ad8aa6f4a529fea33a1'
apisecret = '21bb839bd46e417eb76c72dbe0fb3459'
baseuri = 'https://bittrex.com/api/v1.1/'
nounce = str(time.clock())
#uri= baseuri + '/public/getticker?market=BTC-XLM'
#uri= baseuri + 'account/getbalances?apikey=' + apikey + '&nonce=' + nounce
uri= baseuri + 'account/getdepositaddress?apikey=' + apikey + '&nonce=' + nounce + '&currency=btc'

sign = hmac.new(apisecret, uri, hashlib.sha512).hexdigest()
headers = {"Content-type": "application/json","Accept": "text/plain", "apisign" : sign}
print headers
req = urllib2.Request(uri)
req.add_header('apisign', sign)
r = urllib2.urlopen(req)
print r.read()

