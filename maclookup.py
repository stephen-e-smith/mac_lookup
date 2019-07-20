#!/usr/bin/python

'''
MAC to vendor lookup script
'''

import argparse
import re
import requests
import sys


def lookup_mac(address, key):
    """ Returns a Vendor name given a MAC address """
    vendor = 'INVALID'
    url = 'https://api.macaddress.io/v1?output=json&search=' + address
    headers = {'X-Authentication-Token': key}

    try:
        vendor_payload = requests.post(url, headers=headers)
        vendor = vendor_payload.json()['vendorDetails']['companyName']
    except requests.exceptions.ConnectionError:
        print('Unable to connect to {}'.format(url))
    except requests.exceptions.HTTPError as e:
        print('Invalid HTTP response code {}'.format(e))
    except requests.exceptions.Timeout:
        print('Timeout connecting to {}'.format(url))

    return vendor

parser = argparse.ArgumentParser(description="A MAC address to vendor lookup script.")
mandatory = parser.add_argument_group("Mandatory Arguments")
mandatory.add_argument("-m", "--mac", help="The MAC address to lookup.", type=str)
mandatory.add_argument("-k", "--key", help="macaddress.io API key.", type=str)

args = parser.parse_args()

if not isinstance(args.key, str):
    print('KEY is required.')
    sys.exit(1)
if isinstance(args.mac, str):
    """ Shamelessly stolen from stackoverflow """
    if re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", args.mac.lower()):
        vendor = lookup_mac(args.mac.lower(), args.key)
        print(vendor)
    else:
        print("MAC must be a 12 digit hexidecimal string using only a colon or hyphen as a separator.")
        sys.exit(1)
