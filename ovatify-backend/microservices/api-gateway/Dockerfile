# Use the official Nginx image as a base
FROM nginx:latest

# Remove the default Nginx configuration
RUN rm /etc/nginx/conf.d/default.conf

# Copy config file
COPY nginx.conf /etc/nginx/nginx.conf

# Copy shared proxy settings
COPY location_proxy_shared.conf /etc/nginx/conf.d/location_proxy_shared.conf

# Copy microservice related
COPY service_config/auth_service_routes.conf /etc/nginx/conf.d/auth_service.conf
COPY service_config/recommendation_service_routes.conf /etc/nginx/conf.d/recommendation_service.conf
COPY service_config/user_service_routes.conf /etc/nginx/conf.d/user_service.conf

# Expose port 80
EXPOSE 80
