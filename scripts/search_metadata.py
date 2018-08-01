# Searches and downloads by key word (or metadata)
import requests
import sys
import json 
import urllib
import urllib2
import wget

key_word = sys.argv[1]
api_key = sys.argv[2]

# We'll use the package_serach function to query for a key word.
request = urllib2.Request(
    'http://128.219.187.22/api/action/package_search?q='+ key_word)

# Creating a dataset requires an authorization header.
request.add_header('Authorization', api_key)

# Make the HTTP request.
response = urllib2.urlopen(request)
assert response.code == 200

# Use the json module to load CKAN's response into a dictionary.
response_dict = json.loads(response.read())
assert response_dict['success'] is True

# Grab the response.
packages = response_dict['result']

# Get dataset results
resources_list = packages['results']

# Download each dataset
for resources in resources_list:
    resource = resources['resources']
    for r  in resource:
       dataset_url = r['url']
       wget.download(dataset_url)
