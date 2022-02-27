import RedisDB
import re
import os

global baseURL

def get_endpoints():
    # crawling website which will be obtained from the request -- website should be variable
    os.system('~/Desktop/Diplomka/crawlergo-0.4.2/cmd/crawlergo/crawlergo_cmd -c ~/Downloads/chrome-linux/chrome -t 15 https://www.dictionary.com/ > crawling_output.txt')
    # get method and URL, print into txt 
    os.system('grep -w \'GET\|POST\|PUT\|DELETE\' ./crawling_output.txt > all_endpoints.txt')
    os.system('cut -d " " -f 1-2 all_endpoints.txt | uniq -u > working_endpoints.txt')

def get_baseURL():
    endpoints = open ('working_endpoints.txt', 'r')
    baseURL = endpoints.readline().split(' ')[1]
    return baseURL