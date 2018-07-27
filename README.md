# ORNL Data Catalog
Whitey Nelson <br>
Oak Ridge Nation Labratory <br>
Advance Data and Workflow group <br>
Latest Update: July 27, 2018 <br>

### Introduction

The infrastructure for this data catalog utilizes CADES cloud. Refer to the following links for information on set ups and modifications.

1. [CADES Birthright VM Launch](http://support.cades.ornl.gov/user-documentation/_book/quick-starts/launch-vm-quick-start.html)
  - Networks Tab: choose general_extnetwork1
2. [Accessing your VM](http://support.cades.ornl.gov/user-documentation/_book/openstack/access-vm/access-vm-ssh.html)
3. [SSH shortcut](https://github.com/pycroscopy/cades_birthright/blob/master/ssh_alias.md)
4. [Add Additional Volume](https://github.com/pycroscopy/cades_birthright/blob/master/mount_drive.md)
5. [Mounting a NFS drive](https://github.com/whitneylarose/data_catalog/blob/master/docs/nfs_mount.md)
6. [Globus File Transfer](https://github.com/whitneylarose/data_catalog/blob/master/docs/globus_setup.md)
7. [Running a Server](http://support.cades.ornl.gov/user-documentation/_book/openstack/additional/simple-web-server.html)
8. [Firewall Exception](http://support.cades.ornl.gov/user-documentation/_book/openstack/additional/request-firewall.html)


### CKAN
CKAN is a mature open source  public data repository utilized for this project. It is internationally active in the development community and provides a flexible schema for customization.  CKAN is a python based content management system in contrast to DKAN which is Drupal based and is normally utilized for a PHP ecosystem for existing content management systems. Several other government institutions are utilizing Ckan to publish research data including [data.gov](https://data.gov).

### Installation

This CKAN installation requires Ubuntu 16.04 64-bit. Directions for this CKAN set up can be found [here](https://github.com/whitneylarose/ckan/blob/master/doc/maintaining/installing/install-from-package.rst).

You can find addtional reference documentation on the [CKan doc's site](http://docs.ckan.org/en/2.8/).

### CKAN Key terminology

* **Organization:** An organization owns each dataset. Organizations consist of members who are allowed to edit/add/delete datasets according to their privileges. Refer to [Organizations and Authorizations](http://docs.ckan.org/en/2.8/maintaining/authorization.html) to learn more.

* **Resource** A resource is a single dataset. A resource can not be added independently. It will always be held within a package.

* **Package:** A package is a collection of resources(datasets). Packages can are owned by a single organization.

* **Fileupload:** The file upload button is enabled to allow user to manually upload files. The storage location for the file is /var/lib/ckan/default. This is configured in the CKAN config file (/etc/ckan/default/production.ini )

* **Filestore:** The filestore API allows users to upload new resources via curl command or a file script. The python script to upload files can be found inside /filestore. For more information on curl commands, refer to http://docs.ckan.org/en/2.8/maintaining/filestore.html#filestore-api.

* **Datastore:** The datastore allows a user to upload data that can then be queryable. This is only compatible with tabular data (Excel and CSV files).

* **Datapusher:** The datapusher works alongside the datastore to automatically add data to the datastore.

Note: The datastore and datapusher are implemented but NOT enabled in this installment of CKAN.  

### Creating organizations
An user has the option to manually create organizations on the catalog site. By default, the user will become an admin to the organizations datasets with full access to edit/add/delete entires.

**It is recommended that organizations are create manually via the Ckan site.** Creating organizations with the CKan API is possible but has limitations which are described below:

 An example of creating organizations is found in orgs_create.py. It requires a  CSV file in the argument of the command. The user would run the following to create multiple organizations:
```
python ors_create.py test_orgs.CSV
```
 However, this options has limitations. The name of an organization can only be alphameric lowercase without spaces. For example, "Test Organization Example" would show up on the catalog site as "test-organization-example". CKAN does not provide another way to name organizations via http request. Therefore, the only way to properly format the name of an organization is by manual user input on the catalog's site.

 ### Deleting organizations  

 Organizations can not be delete and/or purged via the website.
 They must be deleted in database.

 You can access the database with the following:
 ```
 sudo -u postgres psql ckan_default
 ```

 Organizations are stored in the "group" table. Contents of the table can be viewed:
 ```
 SELECT * FROM "group";
 ```

### Packages and resources

You can add new datasets manually or via the API.

Resources can only be added to existing packages. You can run the following to upload to the filestore:
```
python filestore/resource_upload.py <package_id> <file_path>
```

There is a script provided that creates a new package, uploads a new resource, and metadata.

```
python filestore/packageCreate.py <file_path> <metadata_file_path>
```


### Metadata Handling
Metadata can be uploaded manually must be formatted in a JSON format and uploaded anytime a new package is created.

There are two options provided to upload metadata:

Option 1: Manual Input

This requires you to put in a key value pair for each peice of information you choose to answer. 

Option 2: CKAN API

When you create a package, specify the associated JSON metadata and it will insert each key value pair. 

```
python filestore/packageCreate.py <file_path> <metadata_file_path>
```

### Uploading metadata from outside resources
Some users have data that is already stored in a preexisting data repository. In these cases, we do not want to duplicate the large datasets. Instead, the user has the option to provide the URL to the data and any associated metadata. This will be a direct link that the user can enter when creating a new resource.

#### External Metadata
Datasets can be stored remotely (with a URL) on the CKan server, metadata associated with the datasets needs to be accessible. This will allow a user to maintain the ability to make queries that will return sufficient results on the CKan site. There are two plugins that can be utilized to collect metadata from remote locations called ckan-next-harvest and ckan-json can be utilized to c

The ckan-next-harvest plugin  allows Ckan to make request for metadata from other data repositories and storing in Ckan's central database. It also provides a UI to manage the sources and jobs. Set up can be found via https://github.com/ckan/ckanext-harvest. The ckannext-json plugin utilizes the harverster to generate .json files. Instructions for installation can be found at https://github.com/HHS/ckanext-datajson.


### To change the file upload limit

You can change the size of a file upload through the ckan nginx conf file. To do so edit the following:

```
sudo vim /etc/nginx/sites-available/ckan
```
Change the the following line, replacing 10000M with a your desired maximum size in megabytes.
```
server{
client_max_body_size 10000M;
}
```
Ensure to use "M" NOT "MB".

Restart nginx:
```
sudo service nginx restart
```

### Deleting the entire database
Note: Only proceed if you want to delete all contents including organizations, resources, packages, users, and sys admins.

Access the virtual environment:
```
. /usr/lib/ckan/default/bin/activate
cd /usr/lib/ckan/default/src/ckan
```

Delete the contents:
```
sudo /usr/lib/ckan/default/bin/paster db clean -c /etc/ckan/default/production.ini
```

Restart the database and apache:  
```
paster db init -c /etc/ckan/default/production.ini
sudo service apache2 restart
```


### Delete a dataset
A dataset can be deleted by a user with authorized access manually going in and deleted the dataset. It will not appear on the site anymore however it will still be available on CKAN. A system admin has the ability to purge a dataset.

Option 1: Utilizing the paster command

* Enter the virtual enviornment
```
. /usr/lib/ckan/default/bin/activate
cd /usr/lib/ckan/default/src/ckan
```
* Delete the dataset replacing "dataset" with the dataset's name
```
paster dataset delete h5_dataset -c /etc/ckan/default/production.ini
```

* Purge the dataset replacing "dataset" with the dataset's name
```
 paster dataset purge dataset_name -c /etc/ckan/default/production.ini
 ```

Option 2: Manual deleting then removing the dataset from resources

* Delete the dataset on the CKAN site.
* Login to your CKAN site as a system admin and navigate to http://your-host-site/ckan-admin/trash
.
* Click `Purge` towards the bottom of the page.

* Delete the corresponding directory via command line.  

```
cd /var/lib/ckan/default/resources
sudo rm -r resource_folder
```

