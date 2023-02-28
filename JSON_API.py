import requests
import urllib
address = '東京都目黒区駒場３丁目８−１'
Response =requests.get('https://msearch.gsi.go.jp/address-search/AddressSearch?q='+urllib.parse.quote(address))
print(Response.json())