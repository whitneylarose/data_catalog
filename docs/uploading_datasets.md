# Uploading a CKAN dataset  via API

The CKAN API utilizes http request to upload datasets. This is okay for smaller datasets but slow and inefficient for larger datasets.

Note: A dataset is a single resource.

### Upload new dataset to a preexisting package.

 You can add resources to a package by running the following:

```
python resoure_upload.py <package_id> <file_path> <api_key>
```

Replace <package_id> with the package you would like to add your dataset to. Replace <file_path> with the location that your dataset is stored and replace <api_key> with an Authorization API key.


### Upload a dataset to a new package
Packages hold a list of resources.
```
python dataset_upload.py <file_path> <metadata_file_path> <api_key> <org_name>
```
Replace <file_path> and <metadata_file_path> with the location that your dataset and metadata is stored. Replace <api_key> with an Authorization API key and <org_name> with the name of the organization that the dataset will be assigned to. 
