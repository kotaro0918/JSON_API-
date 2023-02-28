import requests
import urllib
address = '東京都目黒区駒場３丁目８−１'
res = requests.get('https://geocode.csis.u-tokyo.ac.jp/cgi-bin/simple_geocode.cgi?addr='+urllib.parse.quote(address))
print(res.text)