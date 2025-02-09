#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import urllib2

reload(sys)
sys.setdefaultencoding('utf-8') 

def get_redirect_url(url):  
  opener = urllib2.build_opener()  
  request = urllib2.Request(url)  
  request.get_method = lambda: 'HEAD'  
  response = opener.open(request) 
  return response.geturl()
  
def get_content_type(url):  
  opener = urllib2.build_opener()  
  request = urllib2.Request(url)  
  request.get_method = lambda: 'HEAD'  
  response = opener.open(request) 
  response.info()  
  return dict(response.headers).get('content-type', 'error')

def download_page(url, proxy = None, data = None, headers = {}):
  # set http proxy
  if proxy:
    handler = urllib2.ProxyHandler({'http': 'http://%s/' % proxy})
    opener = urllib2.build_opener(handler)
  else:
    # null_proxy_handler = urllib2.ProxyHandler({})
    # opener = urllib2.build_opener(*null_proxy_handler)
    opener = urllib2.build_opener()

  request = urllib2.Request(url, data)
  # request.get_method = lambda: 'PUT' # or 'DELETE'

  # set headers
  for key, value in headers.items():
    request.add_header(key, value)

  response = opener.open(request, timeout=100)
  # in python source code, urlopen call opener.open
  # redirected_url = response.geturl()
  page_buf = response.read()
  return page_buf

def main():
  url = "http://www.baidu.com"
  header = {'user-agent': 'mozilla/5.0 (x11; linux i686) applewebkit/537.36 (khtml, like gecko) chrome/42.0.2311.135 safari/537.36'}

  buf = download_page(url, None, None, header)
  # print buf

if __name__ == '__main__':
  main()
