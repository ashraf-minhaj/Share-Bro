FROM ubuntu

# ENV IP= curl ipinfo.io/ip
# RUN curl ipinfo.io/ip
# ENV PORT=80

RUN apt-get update

RUN apt-get install nginx -y

COPY . /var/www/frontend/

# RUN cd /etc/nginx/sites-available/

# echo "Coming Soon" | sudo tee /etc/nginx/sites-available/frontend
RUN IP=$(curl ipinfo.io/ip); echo "server { listen 80 default_server; listen [::]:80 default_server; root /var/www/frontend; index index.html; server_name  ${IP}; location / { try_files $uri $uri/ =404; } }" | sudo tee /etc/nginx/sites-available/frontend

RUN sudo ln -s /etc/nginx/sites-available/frontend /etc/nginx/sites-enabled/frontend

RUN sudo rm /etc/nginx/sites-enabled/default \
    sudo systemctl restart nginx