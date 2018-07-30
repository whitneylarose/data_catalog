## CKAN
CKAN is a mature open source  public data repository utilized for this project. It is internationally active in the development community and provides a flexible schema for customization.  CKAN is a python based content management system in contrast to DKAN which is Drupal based and is normally utilized for a PHP ecosystem for existing content management systems. Several other government institutions are utilizing Ckan to publish research data including [data.gov](https://data.gov).

## Installation

Directions for this CKAN set up can be found [here](https://github.com/whitneylarose/ckan/blob/master/doc/maintaining/installing/install-from-package.rst).
Note: This CKAN installation requires Ubuntu 16.04 64-bit. 

## CKAN Key terminology

* **Organization:** An organization owns each dataset. Organizations consist of members who are allowed to edit/add/delete datasets according to their privileges. Refer to [Organizations and Authorizations](http://docs.ckan.org/en/2.8/maintaining/authorization.html) to learn more.

* **Resource** A resource is a single dataset. A resource can not be added independently. It will always be held within a package.

* **Package:** A package is a collection of resources(datasets). Packages can are owned by a single organization.

* **Fileupload:** The file upload button is enabled to allow user to manually upload files. The storage location for the file is /var/lib/ckan/default. This is configured in the CKAN config file (/etc/ckan/default/production.ini )

* **Filestore:** The filestore API allows users to upload new resources via curl command or a file script. The python script to upload files can be found inside /filestore. For more information on curl commands, refer to http://docs.ckan.org/en/2.8/maintaining/filestore.html#filestore-api.

* **Datastore:** The datastore allows a user to upload data that can then be queryable. This is only compatible with tabular data (Excel and CSV files).

* **Datapusher:** The datapusher works alongside the datastore to automatically add data to the datastore.

<br>
Note: The datastore and datapusher are implemented but NOT enabled in this installment of CKAN.

### Additional Resources

You can find addtional reference documentation on the [CKan doc's site](http://docs.ckan.org/en/2.8/).
