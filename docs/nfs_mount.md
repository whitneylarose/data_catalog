# Mounting a NFS drive
Whitney Nelson <br>
Oak Ride National Labratory <br>
Advance Data and Workflow <br>
Last Updated: July 11th, 2018<br>

This documentation assumes that the NFS drive endpoint is already created.

Note:  Mounting the NFS drive to an existing directory "hides" the content of the directory. The content can be viewed again by umounting the drive. 


1.  Install the required packages:
```
$ sudo apt install nfs-common
```
* Check the fstab file:
```
$ cat /etc/fstab
```
You should see something like:
```
LABEL=cloudimg-rootfs   /        ext4   defaults        0 0
```

* Edit the file with your entry:
```
$ sudo vim /etc/fstab
```
enter your fstab entry
```
</remote/export> /var/lib/ckan nfs defaults 0 0
```
  where ``</remote/export>`` is your CADES endpoint

  ``/var/lib/ckan`` is the default storage space for CKAN datasets

   and `defaults` is a comma separated list of options. For additional informtaion on options refer [here](https://www.centos.org/docs/5/html/5.1/Deployment_Guide/s1-nfs-client-config-options.html).

* Now, you can mount your drive
```
$ sudo mount /var/lib/ckan
```
* Ensure your drive is mounted correctly
```
$ df
```
* You should see `/var/lib/ckan` mounted to your endpoint.

* Restart your apache server to set up the storage space. 
```
sudo service apache2 restart
```
