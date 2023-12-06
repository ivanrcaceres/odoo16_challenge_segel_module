# odoo16_challenge_segel_module
Odoo 16 mas un modulo personalizado llamado challenge_segel_module

una vez dentro del servidor ejecutamos este comando en l aterminal
sudo wget https://raw.githubusercontent.com/Yenthe666/InstallScript/16.0/odoo_install.sh

damos permiso de ejecucion
sudo chmod +x odoo_install.sh

ejecutamos el instalador
sudo ./odoo_install.sh

debemos estar atento para aceptar algunas preguntas que nos hace el servidor

una vez instalado el odoo con usus dependencia
hay que crear una carpeta donde vamos a descargar el modulo personalizado

mkdir el_modulo_personalizado

cd el_modulo_personalizado

git clone https://github.com/ivanrcaceres/odoo16_challenge_segel_module.git

cd el_modulo_personalizado/odoo16_challenge_segel_module/

cp -r challenge_segel_module /odoo/custom/addons/

sudo service odoo-server stop

sudo service odoo-server start
