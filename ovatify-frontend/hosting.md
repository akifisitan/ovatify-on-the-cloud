# Hosting

## Requirements

- [node](https://nodejs.org/en)
- [pnpm](https://pnpm.io/)

Create `build` folder with site assets

```bash
pnpm install
pnpm run build
```

## Hosting on a VM via Apache Web Server

1. Run

```bash
sudo vim /etc/apache2/apache2.conf
```

2. Locate the following

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

3. Restart the service

```bash
sudo systemctl restart apache2
```

4. Copy the `.htaccess` file into the `build` folder

5. Copy all the contents of the `build` folder into `/var/www/html`

Here's one way to do it

```bash
mv build html
sudo rm -rf /var/www/html
sudo mv html /var/www/
```

6. Now you can access the site via http://localhost/ and non-existent routes such as http://localhost/notfound should render the proper 404. If you're seeing the default apache 404 page when accessing such routes, there is an issue with the setup.
