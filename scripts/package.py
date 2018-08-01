#!/usr/bin/env python
from __future__ import print_function, division, unicode_literals
import urllib2
import urllib
import json
import pprint
import os
import sys
import json
import monitor
import numpy as np
import requests

def add_resource( id,key, path, r_name, r_format):
       print('Creating new resource...')

       requests.post('http://your-ckan-site/api/action/resource_create',
                  data={"package_id": id, "name": r_name, "format": r_format},
                  headers={"Authorization": key},
                  files=[('upload', file(path))])

       print('Resource created!')
def main(data):

    json_file = ' '
    file_path = ' '

    for d in data:
        if ".json" in d:
            json_file = d
        else:
            file_path = d

    file = os.path.basename(file_path)
    resource_name, format = file.split('.')
    package_name = resource_name.lower()
    package_name = package_name.replace(" ", "-")
    api_key = 'your-api-key'

    # load metadata into list
    with open (json_file) as f:
        json_dict = json.load(f)

    metadata = []

    for key,value in json_dict.items():
        metadata.append({"key": key, "value": value})


    # Put the details of the dataset we're going to create into a dict.
    dataset_dict = {
        'name': package_name,
        'owner_org': 'materials-science-and-technology',
        'extras': metadata
    }

    # Use the json module to dump the dictionary to a string for posting.
    data_string = urllib.quote(json.dumps(dataset_dict))

    # We'll use the package_create function to create a new dataset.
    request = urllib2.Request(
        'http://your-ckan-site/api/action/package_create')

    # Creating a dataset requires an authorization header.
    request.add_header('Authorization', api_key)

    # Make the HTTP request.
    response = urllib2.urlopen(request, data_string)
    assert response.code == 200

    # Use the json module to load CKAN's response into a dictionary.
    response_dict = json.loads(response.read())
    assert response_dict['success'] is True

    print(response_dict)
    # package_create returns the created package as its result.
    created_package = response_dict['result']

    packageID = created_package["id"]

    # Adds resource to the package
    add_resource(packageID, api_key, file_path, file, format)

if __name__ == '__main__':
  main()
