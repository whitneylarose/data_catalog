# User's Guide

Users have the ability to sign up for an account which will give them access to the CKAN API.
The default access for a user is read only privileges, meaning users may only search, view, and download datasets.


## Signing up for a account: 
1. Navigate to the site http://ckan-site.
2. Click `Register` in the top right corner.
3. Fill out all the required information then click `Create Account`.

## Search for datasets and download

This python scripts allows user download all datasets that match a search criteria. 

1. Download the following [script](https://github.com/whitneylarose/data_catalog/blob/master/scripts/search_metadata.py).

2. Edit search_metatdata.py. 
```
sudo vim search_metadata.py
```
3. Replace 'your-ckan-site' with the site's name on line 13  and line 40.

4. Install the following required imports:
```
pip install --upgrade pip
pip install wget
apt-get install python-requests
```

5. Locate your API key by navigating to http://ckan-site/user/your-user-name.
Your API will be located near the bottom of the page.

6. In your command prompt, run the following:
```
python metadata_search.py <key_word> <api_key>
```
Replace `<key_word>` with the word you'd like to search for and `<api_key>`
with your API key.


## Elevating Privileges
A user may have their privileges elevated by an organization admin. Refer to the following to understand
the different privileges:

Role  | Privileges |
------| -----------|
Admin | Can add/edit and delete datasets, as well as manage organization members.|
Editor| Can add and edit datasets, but not manage organization members.|
Member| Can view the organization's private datasets, but not add new datasets.|

To Elevate a user's priveldges: 

1. Click on your Organization.

2. Click the `Members` tabs.

3. Click `Add Member`. 

4. Type in the username or email address and select the desired user.

5. Assign the Role from drop down list.

6. Click `Add member` and the user will appear under members list.


## Add a dataset to a package

Note: Must have editor or admin priveleges.

1. Download the following [script](https://github.com/whitneylarose/data_catalog/blob/master/scripts/resource_upload.py).

2. Edit resource_upload.py: 
```
sudo vim resource_upload.py
```
3. Replace 'your-ckan-site' with the site's name on line 8.

4. Run the following: 
```
python resource_upload.py <package_id> <file_path> <api_key>
```
replace `<package_id>` with a ID of a package you have privileges to edit,
`<file_path>` with the location of your file and `<api_key>` with a your API key.

## Create a new package and upload a dataset
Must have editor or admin priveleges

1. Download the following: 
- [Package Creation](https://github.com/whitneylarose/data_catalog/blob/master/scripts/dataset_upload.py)
- [Resource Upload](https://github.com/whitneylarose/data_catalog/blob/master/scripts/resource_request.py)

2. Edit dataset_upload.py: 
```
sudo vim dataset_upload.py
```
3. Replace 'your-ckan-site' with the site's name on line 48.

4. Edit resource_request.py:

```
sudo vim resource_request.py
```
5. Replace 'your-ckan-site' with the site's name on line 9.

6. Run the following: 
```
python dataset_upload.py <api_key> <org_name> <file_path> <metadata_file_path>
```
Note: `<metadata_file_path>` is optional.
