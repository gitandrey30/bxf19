# Manual 
* use git clone comand
* create venv
* pip install requirements
* create db from psql(settings in rep)
---
* if all OK you can run server and try it
---
## to use guvicorn+nginx need use special configs:  
create .service to gunicorn:
```
[Unit]
Description=Gunicorn instance to serve fast4
After=network.target

[Service]
User=name
Group=www-data
WorkingDirectory=/home/name/projects/fast4
Environment="PATH=/home/name/projects/fast4/venv/bin"
ExecStart=/home/name/projects/fast4/venv/bin/gunicorn --workers 3 --bind unix:fast4.sock -m 007 >

[Install]
WantedBy=multi-user.target
```
after create config file to nginx:
```
server {
    listen 80;
    server_name localhost;

    location / {
    include proxy_params;
    proxy_pass http://unix:/home/name/projects/fast4/fast4.sock;
    }

}
```

result of working this settings you can see in media folder in rep)
project deployed on localhost with gunicorn+nginx

