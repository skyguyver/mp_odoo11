# mp_odoo11
MalPhi project in Odoo 11 environment

# postgres
docker run -d -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=admin --name postgres -p 5433:5432 --restart=always postgres

# pgadmin4
docker run --name pgadmin4 --link postgres:postgres -p 5050:5050 -d fenglc/pgadmin4
user: pgadmin4@pgadmin.org
password: admin

# docker
docker run -v /dev_path/github/mp_odoo11/trunk:/mnt/extra-addons  -p 8070:8069 --name malphi --link postgres:db odoo

# copy files from container
docker cp malphi:/usr/lib/python3/dist-packages/odoo /dev_path/github/mp_odoo11