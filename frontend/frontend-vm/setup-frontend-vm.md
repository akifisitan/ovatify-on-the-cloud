# Frontend VM Setup Instructions

These steps assume a fresh installation of Ubuntu 22.04

1. Install node

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
```

```bash
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
```

```bash
nvm install 20
```

2. Install pnpm

```bash
npm i -g pnpm
```

3. Clone the files

```bash
git clone https://github.com/akifisitan/ovatify-on-the-cloud-public-files.git && cd ovatify-on-the-cloud-public-files/frontend-hosting/
```

4. Clone the example .env file, creating an .env file

```bash
cp .env.example .env
```

5. Update the base url if necessary

```bash
vim .env
```

6. Install dependencies and build the app

```bash
pnpm install && pnpm run build
```

7. Install apache

```bash
sudo apt update && sudo apt install apache2 -y
```

Steps 8, 9, 10 and 11 are for a minor nuance that allows nonexisting routes such as /does/not/exist to be handled by Svelte instead of showing the default apache 404 page. If this is not required, skip to step 12.

8. Allow rewrites

```bash
sudo a2enmod rewrite
```

9. Edit /etc/apache2/apache2.conf

```bash
sudo vim /etc/apache2/apache2.conf
```

Locate the following

```txt
<Directory /var/www/>
	Options Indexes FollowSymLinks
	AllowOverride None
	Require all granted
</Directory>
```

and change it to

```txt
<Directory /var/www/>
	Options Indexes FollowSymLinks
	AllowOverride All
	Require all granted
</Directory>
```

10. Restart the apache service

```bash
sudo systemctl restart apache2
```

11. Copy the .htaccess file

```bash
cp .htaccess build/.htaccess
```

12. Copy all the contents of the `build` folder into `/var/www/html`

```bash
mv build html && sudo rm -rf /var/www/html && sudo mv html /var/www/
```

13. Curl localhost to see if everything is working properly

```bash
curl localhost
```

Important: If any changes need to be made to the source files, steps 6 and 12 must be repeated
