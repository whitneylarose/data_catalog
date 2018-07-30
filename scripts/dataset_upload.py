#!/usr/bin/env python
# Creates a package and uploads the dataset to the package
from __future__ import print_function, division, unicode_literals
import urllib2
import urllib
import json
import os
import sys
import json
from resource_request import resource_request

# grab dataset information
# package name must be lower cased with no spaces
file_path =  sys.argv[1]
file = os.path.basename(file_path)
resource_name, format = file.split('.')
package_name = resource_name.lower()
package_name = package_name.replace(" ", "-")
#api_key = '9c2012f1-4e25-4693-aff1-9d1c0058ef39'

# check if there is metadata
metadata = []
if (sys.argv[2]):

    json_file = sys.argv[2]
    # load metadata into list
    with open (json_file) as f:
        json_dict = json.load(f)

    for key,value in json_dict.items():
        metadata.append({"key": key, "value": value})
        
api_key = sys.argv[3]
org_name = sys.argv[4]

# Put the details of the dataset we're going to create into a dict.
dataset_dict = {
    'name': package_name,
    'owner_org': org_name,
    'extras': metadata
}

# Use the json module to dump the dictionary to a string for posting.
data_string = urllib.quote(json.dumps(dataset_dict))

# We'll use the package_create function to create a new dataset.
request = urllib2.Request(
    'http://128.219.187.22/api/action/package_create')

# Creating a dataset requires an authorization header.
request.add_header('Authorization', api_key)

# Make the HTTP request.
response = urllib2.urlopen(request, data_string)
assert response.code == 200

# Use the json module to load CKAN's response into a dictionary.
response_dict = json.loads(response.read())
assert response_dict['success'] is True

# package_create returns the created package as its result.
created_package = response_dict['result']

packageID = created_package["id"]

# Adds resource/dataset  to the package
resource = resource_request()
resource.create(packageID, api_key, file_path, file, format)

