import urllib.request
import regex as re
import json

tld_url = 'https://data.iana.org/TLD/tlds-alpha-by-domain.txt'

tld_data = urllib.request.urlopen(tld_url)
file = open("tld.json", "w")
tld_lst = []

for line in tld_data:
    tld_string = line.decode('utf-8')[:-1]
    if re.match('^[^\s-]{2,}$', tld_string):
        tld_lst.append(tld_string)
json.dump(tld_lst, file)
file.close()
