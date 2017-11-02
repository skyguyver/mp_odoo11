# mp_odoo11
MalPhi project in Odoo 11 environment

# postgres
docker run -d -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=admin --name postgres -p 5433:5432 --restart=always postgres

# pgadmin4
docker run --name pgadmin4 --link postgres:postgres -p 5050:5050 -d fenglc/pgadmin4
docker run --name pgadmin4 -p 5050:5050 -d fenglc/pgadmin4
user: pgadmin4@pgadmin.org
password: admin

# docker home
docker run -v /dev_path/github/mp_odoo11/trunk:/mnt/extra-addons -p 8070:8069 --name malphi --link postgres:db odoo
docker run -p 8071:8069 --name odoo11 --link postgres:db odoo

# docker office
docker run -v /dev_path/odoo/mp_odoo11/trunk:/mnt/extra-addons  -p 8070:8069 --name malphi --link postgres:db odoo
docker run -v /dev_path/odoo/mp_odoo11/trunk:/mnt/extra-addons -v /dev_path/odoo/11:/var/lib/odoo -p 8070:8069 --name malphi --link postgres:db odoo
/usr/lib/python3/dist-packages/odoo/addons/base/ir

# copy files from container
docker cp malphi:/usr/lib/python3/dist-packages/odoo /dev_path/github/mp_odoo11
docker cp /lynard.ebglobal/development/odoo/11/addons/base/ir/ir_sequence.py malphi:/usr/lib/python3/dist-packages/odoo/addons/base/ir/