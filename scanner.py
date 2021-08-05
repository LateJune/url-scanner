#!/usr/bin/env python3

import sys
import re
import requests
import urllib3

def read_file(file):
    list_of_urls = []

    urls_file = open(file, "r")
    for url in urls_file.readlines():
        list_of_urls.append(url.rstrip('\n'))
        #print(list_of_urls)
    urls_file.close()
    return list_of_urls
        

def perform_requests(url):

    headers = {
        "UserAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Safari/7534.48.3",
        "Accept": "text/html"
        }
    

    try:
        # Write the response to a variable
        print(url)
        res = requests.get(url, headers=headers, verify=False)

        # Get the status code and convert to string
        http_status_code = str(res.status_code)
    
        if re.match("2[0-9]{2}",http_status_code):
            print(res)
        elif re.match("3[0-9]{2}",http_status_code):
            print(res)
        elif re.match("4[0-9]{2}",http_status_code):
            print(res)
        elif re.match("5[0-9]{2}",http_status_code):
            print(res)
        else: 
            print("Did not match on any status codes, something probably did not work")

    except Exception as e: 
        print(e)

    
    print('')

    return None



def main():
    # return codes sybolize success (0) or failure (1) 

    try:
        if len(sys.argv) == 2:
            url_list = read_file(sys.argv[1])
            #print(url_list[0])
            
            for url in url_list:
                perform_requests(url)   

            return 0

        else:
            print("Too many arguments... heres the input as a list")
            print(sys.argv)
            return 0

    except Exception as e :
        print(e)
        print("Usage: python3 file.py urls.txt")
        print("Usage: python3 file.py domain uris.txt")

        return 1


    

if __name__ == "__main__":
    urllib3.disable_warnings()
    main()

