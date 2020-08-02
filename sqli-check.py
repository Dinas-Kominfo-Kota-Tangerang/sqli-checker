# Coded by NAuliajati - Dinas Kominfo Kota Tangerang
import urllib.request, urllib.parse, urllib3, base64
import requests as reqq
from bs4 import BeautifulSoup

url = "https://redacted.com/services/..;/Arsip/..;/x" # change
params = {'rt': 'semua'}
uname = "uname" # change
pname = "passwd" # change
Authz = '%s:%s' % (uname, pname)
b64_Authz = Authz.encode('ascii') # encode binary to bytes
headz = {'Authorization': 'Basic %s' % b64_Authz}

ambil_data = reqq.post(url, params=params, headers=headz)

html_file = BeautifulSoup(ambil_data.text, "html.parser")

print(ambil_data.status_code, html_file.prettify(), file=open("output.html", "f"))
