# ORNL Data Catalog
Whitey Nelson <br>
Suhas Somath <br>
Oak Ridge Nation Labratory <br>
Advance Data and Workflow group <br>
Latest Update: August 10th, 2018 <br>


Refer to the following links for information on set ups and modifications.

### Infrastructure 
The infrastructure for this data catalog utilizes CADES cloud.

1. [CADES Birthright VM Launch](http://support.cades.ornl.gov/user-documentation/_book/quick-starts/launch-vm-quick-start.html)
    - Networks Tab: choose general_extnetwork1
2. [Accessing your VM](http://support.cades.ornl.gov/user-documentation/_book/openstack/access-vm/access-vm-ssh.html)
3. [SSH shortcut](https://github.com/pycroscopy/cades_birthright/blob/master/ssh_alias.md)
4. [Add Additional Volume](https://github.com/pycroscopy/cades_birthright/blob/master/mount_drive.md)
5. [Running a Web Server](http://support.cades.ornl.gov/user-documentation/_book/openstack/additional/simple-web-server.html)
6. [Adding Security Certificates](http://support.cades.ornl.gov/user-documentation/_book/openstack/additional/lets-encrypt.html)
7. [S3 Protocols](http://support.cades.ornl.gov/user-documentation/_book/data-transfer-storage/scality-guide.html)
### Software 

We utilzed CKAN, an open source data management framework. 

1. [CKAN Overview](https://github.com/whitneylarose/data_catalog/blob/master/docs/ckan_install.md)
2. [CKAN Install from Package](https://github.com/whitneylarose/ckan/blob/master/doc/maintaining/installing/install-from-package.rst)
    - Note: If you are using a operating system other than Ubuntu 16.04, you should install from [Source](http://docs.ckan.org/en/2.8/maintaining/installing/install-from-source.html). 
3. [Storage Space (Mounting a NFS Drive)](https://github.com/whitneylarose/data_catalog/blob/master/docs/nfs_mount.md)
4. [Organizations](https://github.com/whitneylarose/data_catalog/blob/master/docs/organizations.md)
5. CKAN API
    - [Dataset Uploads](https://github.com/whitneylarose/data_catalog/blob/master/docs/uploading_datasets.md)
    - [Dataset Downloads](https://github.com/whitneylarose/data_catalog/blob/master/docs/downloading_datasets.md)
    - [Metadata](https://github.com/whitneylarose/data_catalog/blob/master/docs/metadata_handling.md)
6. [File Limits](https://github.com/whitneylarose/data_catalog/blob/master/docs/file_limits.md)
7. [Deletions](https://github.com/whitneylarose/data_catalog/blob/master/docs/deletions.md)
### Data Transfer tool 

You will need a firewall exception for port 2223 and an internet connection via ethernet to utilize Globus. Contact Cyber and the Solution Center for these requests. This may take up to 3 - 4 weeks.

1. [Globus Set Up](https://github.com/whitneylarose/data_catalog/blob/master/docs/globus_setup.md)


### User Guides
1. [Data Catalog User Guide](https://github.com/whitneylarose/data_catalog/blob/master/docs/user_guide.md)
2. [Globus File Transfers](https://github.com/whitneylarose/data_catalog/blob/master/docs/globus_transfers.md)
