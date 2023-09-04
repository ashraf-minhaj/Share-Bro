FROM nginx

# ENV IP= curl ipinfo.io/ip
# RUN curl ipinfo.io/ip
# ENV PORT=80

# Remove default nginx configuration
RUN rm -rf /usr/share/nginx/html/*

# Copy your HTML files into the container
COPY index.html /usr/share/nginx/html
COPY app.js /usr/share/nginx/html

# EXPOSE 80
CMD [ "nginx", "-g", "daemon off;" ]