# Use the official Nginx image as a base
FROM nginx:latest

# Remove the default Nginx configuration
RUN rm /etc/nginx/conf.d/default.conf

# Copy the custom Nginx configuration files
COPY nginx.conf /etc/nginx/nginx.conf

# Copy proxy settings
COPY proxy_settings.conf /etc/nginx/conf.d/proxy_settings.conf

# Copy microservice related
COPY service_config/auth_service_routes.conf /etc/nginx/conf.d/auth_service.conf
COPY service_config/recommendation_service_routes.conf /etc/nginx/conf.d/recommendation_service.conf
COPY service_config/user_service_routes.conf /etc/nginx/conf.d/user_service.conf

# Expose port 80
EXPOSE 80

