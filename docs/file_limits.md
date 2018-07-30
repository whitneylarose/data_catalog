### Changing the file upload limit on nginx

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
