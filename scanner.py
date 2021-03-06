#!/usr/bin/env python3

import sys
import requests
import urllib3
from urllib.parse import urlparse

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
        res = requests.get(url, headers=headers, verify=False, timeout=8)

        # Get the status code and convert to string
        http_status_code = str(res.status_code)

        print(url + " - " + http_status_code)
        result_tuple = (url, http_status_code)

    except Exception as e: 
        print(e)
        result_tuple = (url,"Connection Refused")
        

    return result_tuple

# Bubble sort
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

def make_and_write_results(sorted_list, out_file):
    http_code = 2

    while http_code <= 6:

        # For each url in the sorted list
        for url in sorted_list:

            # Print out header text if it matches the current loop counter 
            if url[1][0] == str(http_code):
                print("--- " + str(http_code) + "00s ---")
                print("--- " + str(http_code) + "00s ---", file=out_file)
                break

            # If it matches the text, print out Error headers
            elif url[1] == 'Connection Refused' and http_code == 6:
                print("--- Errors ---")
                print("--- Errors ---", file=out_file)
                break
            else: 
                continue
        
        # For each url match with the first digit of the http status and the while loop couter
        for url in sorted_list:
            if url[1][0] == '2' and http_code == 2:
                print(url[0],"-", url[1])
                print(url[0],"-", url[1], file=out_file)
                continue
            elif url[1][0] == '3' and http_code == 3:
                print(url[0],"-", url[1])
                print(url[0],"-", url[1], file=out_file)
                continue
            elif url[1][0] == '4' and http_code == 4:
                print(url[0],"-", url[1])
                print(url[0],"-", url[1], file=out_file)
                continue
            elif url[1][0] == '5' and http_code == 5:
                print(url[0],"-", url[1])
                print(url[0],"-", url[1], file=out_file)
                continue
            elif url[1] == 'Connection Refused' and http_code == 6:
                print(url[0],"-", url[1])
                print(url[0],"-", url[1], file=out_file)
                continue

        # Increase the loop counter by one
        http_code += 1
        
    return None

def main():
    # return codes sybolize success (0) or failure (-1/1) 
    try:
        if len(sys.argv) == 2:           
            url_list = read_file(sys.argv[1])
            
            # Gather all the requests into a single list
            unsorted_list = []
            for url in url_list:
                unsorted_list.append(perform_requests(url))

            # Gather all of the domains observed
            list_of_domains = []
            domain = ''
            for url_tuple in unsorted_list:
                urlparse_obj = urlparse(url_tuple[0])
                domain = urlparse_obj.scheme + "://" + urlparse_obj.hostname
                list_of_domains.append(domain)

            # Sort our list for later usage
            sorted_list = sort(unsorted_list)
        
            # Create temporary buffers
            single_domain_buffer = []
            already_printed_domains = []

            # Open file for writing with append option
            out_file = open("output.txt", "a")

            # Iterate over the list of domains and skip the ones already written
            for domain in list_of_domains:
                # If the domain is already in our list, skip it
                if domain in already_printed_domains:
                    continue
                else:
                    # Otherwise, append it to the current seen domain list
                    already_printed_domains.append(domain)
                    for url_tuple in sorted_list:
                        # If the current domain matches a url in the current tuple
                        if domain in url_tuple[0]:
                            # Append it to the list for a single domain
                            single_domain_buffer.append(url_tuple)
                        else:
                            # Otherwise keep searching for a match
                            continue
                
                # Write headers and call the write results function  
                print('\n')
                print('\n', file=out_file)
                print("======== " + str(domain) + " ========")
                print("======== " + str(domain) + " ========", file=out_file)
                make_and_write_results(single_domain_buffer, out_file)

                # Overwrite the single domain list 
                single_domain_buffer = []
            
            # Close file
            out_file.close()
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