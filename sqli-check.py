import urllib.request, urllib.parse, urllib3, base64
import requests as reqq
from bs4 import BeautifulSoup

url = "https://service-tlive.tangerangkota.go.id/services/daftarumkm/Arsip/getDetailRtRw"
params = {'rt': 'semua'}
# params = params.encode('ascii')
uname = "r35t4p1"
pname = "xlzh5v6sgrpvqs3os86x2s298fb04z6txo9cntx0"
Authz = '%s:%s' % (uname, pname)
b64_Authz = Authz.encode('ascii')
# b64_Authz = base64.b64encode(Authz)
headz = {'Authorization': 'Basic %s' % b64_Authz}

#http = urllib3.PoolManager()
#Authz = urllib3.util.make_headers(basic_auth='r35t4p1:xlzh5v6sgrpvqs3os86x2s298fb04z6txo9cntx0')
#http.request('POST', params, url, headers=Authz)

ambil_data = reqq.post(url, params=params, headers=headz)

#req = urllib.request.Request(url, params, Authz)
#with urllib.request.urlopen(req) as r:
#    print(r.read().decode('utf-8'))

html_file = BeautifulSoup(ambil_data.text, "html.parser")

print(ambil_data.status_code, html_file.prettify(), file=open("output.html", "a"))

#def req_post(self, url, params, methods = ['POST']):
#    sess = requests.session()
#    self.url = sess.post(url)
#    self.params = params
#    self.methods = urllib.request.urlopen(url, params, methods)
#    return sess
