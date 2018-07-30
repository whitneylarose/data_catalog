### Metadata Handling
Metadata can be uploaded manually must be formatted in a JSON format and uploaded anytime a new package is created.

There are two options provided to upload metadata:

#### Option 1: Manual Input

This requires you to put in a key value pair for each peice of information you choose to answer. 

#### Option 2: CKAN API

When you create a package, specify the associated JSON metadata and it will insert each key value pair. 

```
python dataset_upload.py <file_path> <metadata_file_path> <api_key> <org_name>

```

### Uploading metadata from outside resources
Some users have data that is already stored in a preexisting data repository. In these cases, we do not want to duplicate the large datasets. Instead, the user has the option to provide the URL to the data and any associated metadata. This will be a direct link that the user can enter when creating a new resource.

#### External Metadata
Datasets can be stored remotely (with a URL) on the CKan server, metadata associated with the datasets needs to be accessible. This will allow a user to maintain the ability to make queries that will return sufficient results on the CKan site. There are two plugins that can be utilized to collect metadata from remote locations called ckan-next-harvest and ckan-json can be utilized to c

The ckan-next-harvest plugin  allows Ckan to make request for metadata from other data repositories and storing in Ckan's central database. It also provides a UI to manage the sources and jobs. Set up can be found via https://github.com/ckan/ckanext-harvest. The ckannext-json plugin utilizes the harverster to generate .json files. Instructions for installation can be found at https://github.com/HHS/ckanext-datajson.
