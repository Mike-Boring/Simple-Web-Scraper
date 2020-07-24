#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Simple Web Scraper.

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

__author__ = "Mike Boring"

"""
Application to scrape a single web page, extracting any URLs, email addresses,
and phone numbers it contains.
...

Suggested milestones for incremental development:
 DONE- Setup parser for command line parsing
 DONE- Save specified webpage html to a text file
 DONE- Search for email, phone and url addresses in file using findall or RE
 DONE- Save to dictionary of lists with keys of url, phone, email
 DONE- Print to console a separated list of each
"""

import re
import sys
import urllib.request
import argparse
import os


def create_parser():
    """Creates an argument parser object."""
    parser = argparse.ArgumentParser()
    parser.add_argument('selected_url', help='url to extract data from')
    return parser


def find_data(selected_url):
    """
    Search thru specified url for urls, phone
    numbers and email addresses and print to console.
    """
    found_data = {}
    if os.path.isfile('url_to_search.txt'):
        os.remove('url_to_search.txt')
    urllib.request.urlretrieve(selected_url, 'url_to_search.txt')
    with open('url_to_search.txt') as f:
        text = f.read()
        final_url_list = []
        url_format = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        email_format = r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)'
        phone_format = r'(\([1-9][0-9][0-9]\)[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]|[1-9][0-9][0-9]-[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9])'
        found_data['url'] = re.findall(url_format, text)
        for url in found_data['url']:
            split_url = url.split("'")
            final_url_list.append(split_url[0])
        found_data['url'] = final_url_list
        found_data['email'] = re.findall(email_format, text)
        found_data['phone'] = re.findall(phone_format, text)
    print('URLS:\n')
    if found_data['url']:
        for url in set(found_data['url']):
            print(url)
    else:
        print('NONE')
    print('\nEmails:\n')
    if found_data['email']:
        for email in set(found_data['email']):
            print(email)
    else:
        print('NONE')
    print('\nPhone Numbers:\n')
    if found_data['phone']:
        for phone in set(found_data['phone']):
            print(phone)
    else:
        print('NONE')


def main(args):
    """Parses args."""
    parser = create_parser()
    if not args:
        parser.print_usage()
        sys.exit(1)
    parsed_args = parser.parse_args(args)
    selected_url = parsed_args.selected_url
    find_data(selected_url)


if __name__ == '__main__':
    main(sys.argv[1:])
