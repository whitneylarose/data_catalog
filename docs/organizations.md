# Organizations 

Organizations consist of members who control the creating, updating, viewing, and deleting datasets. 

## Creating organizations

**It is recommended that organizations are created manually via the Ckan site.** 

A system admin has the option to manually create organizations or utilize the CKAN API. By default, you will become an admin to the organization you create and have full access to edit/add/delete datasets or members.


CKAN API: 
An example of creating organizations can be downloaded [here](https://github.com/whitneylarose/data_catalog/blob/master/scripts/org_create.py). In this example, you would run the following:
```
python ors_create.py <org_file.csv>
```

However, this has limitations. The name of an organization can only be alphameric lowercase without spaces. For example, "My Organization Example" would show up on the catalog site as "my-organization-example". CKAN does not provide another way to name organizations. Therefore, the only way to properly format the name of an organization is by manual user input on the catalog's site.

 ## Deleting organizations  

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
