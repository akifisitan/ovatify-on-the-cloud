# Use the official Node image as the base image
FROM node:20

# Set the working directory in the container
WORKDIR /app

COPY . /app

# Install pnpm
RUN npm install -g pnpm

# Install dependencies and build the application
RUN pnpm install && pnpm run build

# Install Apache
RUN apt-get update && \
  apt-get install -y apache2

# Enable Apache mod_rewrite for handling SPA routes
RUN a2enmod rewrite

# Update the Apache configuration to allow .htaccess overrides
RUN sed -i 's/AllowOverride None/AllowOverride All/g' /etc/apache2/apache2.conf

# Copy the built app to the Apache directory
RUN mv build html && rm -rf /var/www/html && mv html /var/www/

# Copy the .htaccess file to the build directory
COPY .htaccess /var/www/html/.htaccess

# Expose port 80
EXPOSE 80

# Start Apache in the foreground
CMD ["apachectl", "-D", "FOREGROUND"]
