import requests
import urllib
param={'q': '東京都目黒区駒場３丁目８−１'}
ep="https://msearch.gsi.go.jp/address-search/AddressSearch"
Response =requests.get(ep,params=param)
print(Response.json())