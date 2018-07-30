import json
import sys
import urllib2
import requests
import urllib

#reads in CSV file and authorizaion
organizations_file =  sys.argv[1]
api_key = sys.argv[2]
organizations_list = []

with open(organizations_file, 'r') as f:
    organizations_list.append(str(f.read()))

# Put the details of the organization we're going to create into a dict.
# Note: organizations must be lower case without any spaces
for org in organizations_list:
    url_name = org.replace(" ", "-")
    name = url_name.lower()
    print(name)
    organization_dict = {
        'name': name,
        'display_name': org
    }

    # Use the json module to dump the dictionary to a string for posting.
    data_string = urllib.quote(json.dumps(organization_dict))

    # We'll use the organization_create function to create a new organization.
    request = urllib2.Request(
        'http://128.219.187.22/api/action/organization_create')

    # Creating a organization requires an authorization header.
    request.add_header('Authorization', api_key)

    # Make the HTTP request.
    response = urllib2.urlopen(request, data_string)
    assert response.code == 200

    # Use the json module to load CKAN's response into a dictionary.
    response_dict = json.loads(response.read())
    assert response_dict['success'] is True

    # organization_create returns the created organization as its result.
    created_org = response_dict['result']

    print(created_org)
