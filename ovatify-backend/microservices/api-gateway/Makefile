copy:
	sudo cp nginx.conf /etc/nginx/nginx.conf
	sudo cp location_proxy_shared.conf /etc/nginx/conf.d/location_proxy_shared.conf
	sudo cp service_config/auth_service_routes.conf /etc/nginx/conf.d/auth_service.conf
	sudo cp service_config/recommendation_service_routes.conf /etc/nginx/conf.d/recommendation_service.conf
	sudo cp service_config/user_service_routes.conf /etc/nginx/conf.d/user_service.conf
	sudo nginx -t
	sudo systemctl reload nginx

update:
	sudo cp proxy.conf /etc/nginx/sites-available/proxy.conf
	sudo cp nginx.conf /etc/nginx/nginx.conf
	sudo nginx -t
	sudo systemctl reload nginx

reload:
	sudo systemctl reload nginx

check:
	sudo nginx -t

view-error-logs:
	sudo tail -f /var/log/nginx/error.log

view-access-logs:
	sudo tail -f /var/log/nginx/access.log