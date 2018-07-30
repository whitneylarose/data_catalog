### Delete a dataset
A dataset can be deleted by a user with authorized access manually going in and deleted the dataset. It will not appear on the site anymore however it will still be available on CKAN. A system admin has the ability to purge a dataset.

#### Option 1: Utilizing the paster command

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

#### Option 2: Manual deleting then removing the dataset from resources

* Delete the dataset on the CKAN site.
* Login to your CKAN site as a system admin and navigate to http://your-host-site/ckan-admin/trash
.
* Click `Purge` towards the bottom of the page.

* Delete the corresponding directory via command line.  

```
cd /var/lib/ckan/default/resources
sudo rm -r resource_folder
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


