docker push netenggr/carpool:firstcommit


docker-compose -f docker-compose.prod.yml down -v
docker-compose -f docker-compose.prod.yml up -d --build
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput


pgadmin4
https://towardsdatascience.com/how-to-run-postgresql-and-pgadmin-using-docker-3a6a8ae918b5

https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-pgadmin-4-in-server-mode-on-ubuntu-22-04


docker run -it --rm --entrypoint=bash my_image_name

entrypoint.sh όταν δεν τρέχει( not found) αλλαγή στο vscode από CRLF σε LF κάτω δεξιά

Error starting userland proxy: listen tcp4 0.0.0.0:80: bind: address already in use
κάνει conflict το nginx του ubuntu. το κάνω kill
sudo service nginx stop και αλλάζω το default.conf το listening port από 80 σε 81 μήπως και ξαναξεκινήσει σε κανένα restart