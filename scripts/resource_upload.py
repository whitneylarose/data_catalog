import requests
import sys

package_id = sys.argv[1]
file_path = sys.argv[2]
api_key = sys.argv[3]

requests.post('http://your-ckan-site/api/action/resource_create',
              data={"package_id":package_id},
              headers={"Authorization": api_key},
              files=[('upload', file(file_path))])
