### S3 Bucket CORS Policy
```
[
    {
        "AllowedHeaders": [
            "*"
        ],
        "AllowedMethods": [
            "PUT",
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": [
            "ETag"
        ],
        "MaxAgeSeconds": 3000
    }
]
```

# some useful commands
* version check `pip show lib_name`
* install dpndncs from file `pip3 install --no-cache-dir -r requirements.txt` / `pip3 install -r requirements.txt`
* run flask on dedicated prot & host`flask run --host=0.0.0.0 --port=5000`
* docker image build `sudo docker build --tag sharebro-api1 .`
* run `sudo docker run -d -p 5000:5000 sharebro-api1:latest`

### nginx server setup 

run -
```
sudo apt-get update
sudo apt-get install nginx -y
sudo mkdir /var/www/frontend
cd /var/www/frontend
echo "Coming Soon" | sudo tee index.html
cd /etc/nginx/
```
> **sites-available** contains individual configuration files for all of your possible static websites.
> **sites-enabled** contains links to the configuration files that NGINX will actually read and run.
> **create a configuration file in sites-available**, and then **create a symbolic link** (a pointer) to that file in sites-enabled to actually tell NGINX to run it.

run -
```
cd sites-available/
sudo nano frontend
```
Paste -
```
server {
  listen 80 default_server;
  listen [::]:80 default_server;
  root /var/www/frontend;
  index index.html;
  server_name  ;
  location / {
    try_files $uri $uri/ =404;
  }
}
```
run -
```
sudo ln -s /etc/nginx/sites-available/frontend /etc/nginx/sites-enabled/frontend
```
restart nginx -
```
sudo systemctl restart nginx
```

in case -
```
sudo fuser -k 80/tcp
sudo rm /etc/nginx/sites-enabled/default
sudo systemctl restart nginx
```
