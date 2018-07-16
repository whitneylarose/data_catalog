# Mounting a NFS drive
Whitney Nelson <br>
Oak Ride National Labratory <br>
Advance Data and Workflow <br>
Last Updated: July 11th, 2018<br>

Note: This documentation assumes that the NFS drive endpoint is already created.

1.  Install the required packages:
```
$ sudo apt install nfs-common
```

* Create a folder. This will be where your NFS is mounted
```
$ sudo mkdir -p data
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
</remote/export> /data nfs defaults 0 0
```
  where ``</remote/export>`` is your CADES endpoint

  ``/data`` is where the  directory will be mounted

   and `defaults` is a comma separated list of options. For additional informtaion on options refer [here](https://www.centos.org/docs/5/html/5.1/Deployment_Guide/s1-nfs-client-config-options.html).

* Now, you can mount your drive
```
$ sudo mount /data
```
* Ensure your drive is mounted correctly
```
$ df
```
* You should see `/data` mounted to your endpoint.
