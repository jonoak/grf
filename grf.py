'''
# get_run_file ( grf )

# grf.py

'''

def get(url):
  import requests as rq
  the_file = rq.get(url).text
  name = url.split("file=")[1].split("&")[0]
  with open(name,'w') as wi:
    wi.write(the_file)

def run(url):
  import requests as rq
  the_file = rq.get(url).text
  exec(the_file)

import sys
import os
os.system('pip install requests')
the_request = sys.argv[1]
the_url = sys.argv[2]
if the_request == 'get':
  get(the_url)
elif the_request == 'run':
  run(the_url)
else:
  print("what?")