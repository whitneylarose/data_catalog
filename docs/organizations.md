## Organizations 

Organizations consist of members who control the creating, updating, viewing, and deleting datasets. 

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
