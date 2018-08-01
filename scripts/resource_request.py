import requests
import sys

class resource_request():

   def create(self, id,key, path, r_name, r_format):
       print('Creating new resource...')

       requests.post('http://your-ckan-site/api/action/resource_create',
                  data={"package_id": id, "name": r_name, "format": r_format},
                  headers={"Authorization": key},
                  files=[('upload', file(path))])

       print('Resource created!')
