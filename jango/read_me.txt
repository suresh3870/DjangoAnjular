----Step to install Project on EC2---

sudo apt-get update
sudo apt-get install python3-pip python3-dev nginx git
sudo pip3 install virtualenv
git clone https://github.com/suresh3870/DjangoAnjular.git
cd DjangoAnjular
virtualenv venv
source venv/bin/activate
cd jango
pip install -r requirements.txt
pip install django bcrypt django-extensions
pip install gunicorn
cd jango

#change the IP4 and add from as per your EC2
for me it was- ALLOWED_HOSTS = ['3.16.167.247']
python manage.py collectstatic
#gunicorn --bind 0.0.0.0:8000 jango.wsgi:application

#sudo vim /etc/systemd/system/gunicorn.service

	[Unit]
	Description=gunicorn daemon
	After=network.target
	[Service]
	User=ubuntu
	Group=www-data
	WorkingDirectory=/home/ubuntu/DjangoAnjular/jango
	ExecStart=/home/ubuntu/DjangoAnjular/venv/bin/gunicorn --workers 3 --bind unix:/home/ubuntu/DjangoAnjular/jango/jango/jango.sock jango.wsgi:application
	[Install]
	WantedBy=multi-user.target

#sudo systemctl daemon-reload
#sudo systemctl start gunicorn
#sudo systemctl enable gunicorn

#sudo vim /etc/nginx/sites-available/jango
	server {
	listen 80;
	server_name 3.16.167.247;
	location = /favicon.ico { access_log off; log_not_found off; }
	location /static/ {
		root /home/ubuntu/DjangoAnjular/jango;
	}
	location / {
		include proxy_params;
		proxy_pass http://unix:/home/ubuntu/DjangoAnjular/jango/jango/jango.sock;
	}
	}
sudo ln -s /etc/nginx/sites-available/jango /etc/nginx/sites-enabled
sudo nginx -t
sudo rm /etc/nginx/sites-enabled/default
sudo service nginx restart