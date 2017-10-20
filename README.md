# mp_odoo11
MalPhi project in Odoo 11 environment

# docker
docker run -v /dev_path/odoo/mp_odoo11/trunk:/mnt/extra-addons  -p 8071:8069 --name malphi11 --link mp_db:db odoo