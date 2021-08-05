#!/usr/bin/env python3

import sys
import requests
import urllib3

def read_file(file):
    raw_file_contents = []
    list_of_urls = []

    urls_file = open(file, "r")
    for url in urls_file.readlines():        
        raw_file_contents.append(url.rstrip('\n')) 
    urls_file.close()

    for url in raw_file_contents:
        if url != '':
            list_of_urls.append(url)
        else:
            continue
        
    # print(list_of_urls)
    return list_of_urls
        
def perform_requests(url):
    try:
        headers = {
        "UserAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Safari/7534.48.3",
        "Accept": "text/html"
        }
        # Write the response to a variable
        res = requests.get(url, headers=headers, verify=False)

        # Get the status code and convert to string
        http_status_code = str(res.status_code)

        print(url + " - " + http_status_code)
        result_tuple = (url, http_status_code)

    except Exception as e: 
        print(e)

    return result_tuple

# Simple bubble sort
def sort(bubble_sort_list):
    list_len = len(bubble_sort_list)

    for i in range(list_len - 1):
        flag = False
        for j in range(list_len - 1):
            if bubble_sort_list[j][1] > bubble_sort_list[j + 1][1]:
                place_holder = bubble_sort_list[j]
                bubble_sort_list[j] = bubble_sort_list[j + 1]
                bubble_sort_list[j+ 1] = place_holder
                flag = True

        if flag == False:
            break
    
    return bubble_sort_list

def make_and_write_results(sorted_list):

    out_file = open("output.txt", "w")
    http_code = 2

    while http_code < 6:
        print("--- " + str(http_code) + "00s ---")
        print("--- " + str(http_code) + "00s ---", file=out_file)

        for url in sorted_list:
            if url[1][0] == '2' and http_code == 2:
                print(url[0], url[1])
                print(url[0], url[1], file=out_file)
            elif url[1][0] == '3' and http_code == 3:
                print(url[0], url[1])
                print(url[0], url[1], file=out_file)
            elif url[1][0] == '4' and http_code == 4:
                print(url[0], url[1])
                print(url[0], url[1], file=out_file)
            elif url[1][0] == '5' and http_code == 5:
                print(url[0], url[1])
                print(url[0], url[1], file=out_file)
        
        print('')
        print('', file=out_file)
        http_code += 1

    out_file.close()
        
    return None

def main():
    # return codes sybolize success (0) or failure (-1/1) 
    try:
        if len(sys.argv) == 2:
            url_list = read_file(sys.argv[1])
            
            unsorted_list = []
            for url in url_list:
                unsorted_list.append(perform_requests(url))

            print('\n') # include some space between console output
            make_and_write_results(sort(unsorted_list))

            return 0

        else:
            print("Usage: python3 scanner.py urls.txt\n")
            print("Too many or not enough arguments, here is your input as a list:")
            print(sys.argv)
            return 1

    except Exception as e :
        print(e)
        print("Usage: python3 scanner.py urls.txt")
        return -1

if __name__ == "__main__":
    urllib3.disable_warnings()
    main()