# ORNL Data Catalog
Whitey Nelson <br>
Oak Ridge Nation Labratory <br>
Advance Data and Workflow group <br>
Latest Update: July 30, 2018 <br>


Refer to the following links for information on set ups and modifications.

### Infrastructure 
The infrastructure for this data catalog utilizes CADES cloud.

1. [CADES Birthright VM Launch](http://support.cades.ornl.gov/user-documentation/_book/quick-starts/launch-vm-quick-start.html)
    - Networks Tab: choose general_extnetwork1
2. [Accessing your VM](http://support.cades.ornl.gov/user-documentation/_book/openstack/access-vm/access-vm-ssh.html)
3. [SSH shortcut](https://github.com/pycroscopy/cades_birthright/blob/master/ssh_alias.md)
4. [Add Additional Volume](https://github.com/pycroscopy/cades_birthright/blob/master/mount_drive.md)
5. [Mounting a NFS drive](https://github.com/whitneylarose/data_catalog/blob/master/docs/nfs_mount.md)
6. [Running a Server](http://support.cades.ornl.gov/user-documentation/_book/openstack/additional/simple-web-server.html)

### Software 

We utilzed CKAN, an open source data management framework. 

1. [CKAN Overview](https://github.com/whitneylarose/data_catalog/blob/master/docs/ckan_install.md)
2. [CKAN Install](https://github.com/whitneylarose/ckan/blob/master/doc/maintaining/installing/install-from-package.rst)
3. [Organizations](https://github.com/whitneylarose/data_catalog/blob/master/docs/organizations.md)
4. CKAN API
    - [Dataset Uploads](https://github.com/whitneylarose/data_catalog/blob/master/docs/uploading_datasets.md)
    - [Dataset Downloads](https://github.com/whitneylarose/data_catalog/blob/master/docs/downloading_datasets.md)
    - [Metadata](https://github.com/whitneylarose/data_catalog/blob/master/docs/metadata_handling.md)
5. [File Limits](https://github.com/whitneylarose/data_catalog/blob/master/docs/file_limits.md)
6. [Deletions](https://github.com/whitneylarose/data_catalog/blob/master/docs/deletions.md)
### Data Transfer tool 

You will need a firewall exception to utilize Globus. 

1. [Globus File Transfer](https://github.com/whitneylarose/data_catalog/blob/master/docs/globus_setup.md)
