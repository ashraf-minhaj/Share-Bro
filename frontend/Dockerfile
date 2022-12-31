FROM ubuntu

# ENV IP= curl ipinfo.io/ip
# RUN curl ipinfo.io/ip
# ENV PORT=80

RUN apt-get update

RUN apt-get install nginx -y

# ; apt-get install curl -y

# COPY index.html /var/www/frontend/
COPY index.html /var/www/html/

# RUN cd /etc/nginx/sites-available/

# echo "Coming Soon" | sudo tee /etc/nginx/sites-available/frontend
# RUN IP=$(curl ipinfo.io/ip); echo "server { listen 80 default_server; listen [::]:80 default_server; root /var/www/frontend; index index.html; server_name  ${IP}; location / { try_files $uri $uri/ =404; } }" | tee /etc/nginx/sites-available/frontend

# RUN ln -s /etc/nginx/sites-available/frontend /etc/nginx/sites-enabled/frontend

# RUN rm /etc/nginx/sites-enabled/default

EXPOSE 80
CMD [ "nginx", "-g", "daemon off;" ]

# systemctl restart nginx
# sudo docker build --tag sharebro-frontend .