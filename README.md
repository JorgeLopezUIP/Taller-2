# Taller-2 
Para instalar y configurar MariaDB en el entorno de desarrollo, primero descarga el instalador desde la página oficial de MariaDB. 
Durante la instalación, elige la opción de instalar el servidor y cliente, configura una contraseña segura para el usuario root 
y finaliza el proceso. Una vez instalado, abre el terminal o consola y verifica que el servicio esté activo con el comando systemctl 
status mariadb (en Linux) o comprobando el servicio en el panel de servicios (en Windows). Finalmente, accede al cliente ejecutando 
mariadb -u root -p, ingresa tu contraseña, y desde allí podrás crear bases de datos, usuarios y permisos. Para usarlo desde Python, 
asegúrate de instalar el conector con pip install mariadb o usar SQLAlchemy con pip install sqlalchemy mariadb-connector-python
