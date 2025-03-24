"""Para instalar y configurar MariaDB en el entorno de desarrollo, primero descarga el instalador desde la página oficial de MariaDB. 
Durante la instalación, elige la opción de instalar el servidor y cliente, configura una contraseña segura para el usuario root 
y finaliza el proceso. Una vez instalado, abre el terminal o consola y verifica que el servicio esté activo con el comando systemctl 
status mariadb (en Linux) o comprobando el servicio en el panel de servicios (en Windows). Finalmente, accede al cliente ejecutando 
mariadb -u root -p, ingresa tu contraseña, y desde allí podrás crear bases de datos, usuarios y permisos. Para usarlo desde Python, 
asegúrate de instalar el conector con pip install mariadb o usar SQLAlchemy con pip install sqlalchemy mariadb-connector-python"""

import mariadb 
import sys 
import sqlalchemy 
import sqlalchemy.exc
from sqlalchemy.ext.declarative import declarative_base 
import sqlite3
import sqlalchemy.orm

try:
    engine = sqlalchemy.create_engine("mariadb+mariadbconnector://root:Jorlis@127.0.0.1:3306/Libreria")
except sqlalchemy.exc.SQLAlchemyError as a: 
    print("Error al intentar crear la base de datos") 
    sys.exit(1) 

Base = declarative_base() 

class Libro(Base): 
    __tablename__ = "libros" 
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True) 
    titulo = sqlalchemy.Column(sqlalchemy.String(length=100))
    genero = sqlalchemy.Column(sqlalchemy.String(length=100))
    autor = sqlalchemy.Column(sqlalchemy.String(length=100))
    estado = sqlalchemy.Column(sqlalchemy.String(length=100)) 
    active = sqlalchemy.Column(sqlalchemy.Boolean, default=True) 

Base.metadata.create_all(engine)
Session = sqlalchemy.orm.sessionmaker() 
Session.configure(bind=engine) 
Session = Session()

def agregar_libro(): 
    try:
        titulo = input("Titulo del libro: ")  
        genero = input("Genero del libro: ")  
        autor = input("Nombre del autor: ")  
        estado = input("Estado del libro: ")

        nuevo_libro = Libro(titulo=titulo, genero=genero, autor=autor, estado=estado) 

        Session.add(nuevo_libro)
        Session.commit() 

        print("Libro agregado exitosamente.") 
    except Exception as c: 
        Session.rollback() 
        print("Error al agregar libro")     

def actualizar_libro(): 
    try:
        titulo_buscar = input("Ingrese el título del libro que quiere modificar: ")
        libro = Session.query(Libro).filter(Libro.titulo==titulo_buscar).first()
    
        if libro is None:
            print("El libro no existe")
            return
    
        print("1.Actualizar titulo")       
        print("2.Actualizar autor")       
        print("3.Actualizar genero")       
        print("4.Actualizar estado\n")       
        w = int(input("Elija una opcion: ")) 

        if w == 1: 
            busqueda = input("Escriba el nuevo titulo del libro: ") 
            libro.titulo = busqueda 
        elif w == 2: 
            busqueda = input("Escriba el nuevo autor del libro: ") 
            libro.autor = busqueda 
        elif w == 3: 
            busqueda = input("Escriba el nuevo genero del libro: ") 
            libro.genero = busqueda 
        elif w == 4: 
            busqueda = input("Escriba el nuevo estado del libro: ") 
            libro.estado = busqueda 
            
        Session.commit() 
    except Exception as c: 
        Session.rollback() 
        print("Error al actualizar el libro")        

def eliminar_libro(): 
    try:
        titulo_buscar = input("Ingrese el titulo del libro que desea eliminar de la base de datos: ")   
        Session.query(Libro).filter(Libro.titulo == titulo_buscar).delete()  
        Session.commit() 

        print("Libro eliminado")
    except Exception as c: 
        Session.rollback() 
        print("Error al eliminar el libro")
     
def ver_libros(): 
    try:  
        listado = Session.query(Libro).all() 

        for i in listado: 
            print(f"titulo: {i.titulo}\ngenero: {i.genero}\nautor: {i.autor}\nestado: {i.estado}\n") 
    except Exception as c: 
        Session.rollback() 
        print("Error al mostar libros")

def buscar_libro(): 
    try:
        print("1.Buscar por titulo")       
        print("2.Buscar por autor")       
        print("3.Buscar por genero\n")       
        w = int(input("Elija una opcion: ")) 

        if w == 1: 
            busqueda = input("Escriba el titulo del libro: ") 
            libro = Session.query(Libro).filter(Libro.titulo==busqueda).all()
        elif w == 2: 
            busqueda = input("Escriba el autor del libro: ") 
            libro = Session.query(Libro).filter(Libro.autor==busqueda).all()
        elif w == 3: 
            busqueda = input("Escriba el genero del libro: ") 
            libro = Session.query(Libro).filter(Libro.genero==busqueda).all()

        for i in libro: 
            print(f"\ntitulo: {i.titulo}\ngenero: {i.genero}\nautor: {i.autor}\nestado: {i.estado}\n")     
    except Exception as c: 
        Session.rollback() 
        print("Error al buscar libro") 
  
while True: 
    print("1.Ingresar libro")
    print("2.Actualizar informacion del libro")
    print("3.Eliminar libro")
    print("4.Ver libros")  
    print("5.Buscar libros")
    print("6.Salir") 
    e = int(input("Elija una opcion: ")) 

    if e == 1: 
        agregar_libro() 
    
    elif e == 2:
        actualizar_libro() 

    elif e == 3: 
        eliminar_libro()     

    elif e == 4: 
        ver_libros()               

    elif e == 5:
        buscar_libro() 

    elif e == 6:                   
      break 

    else: 
        print("Opcion no valida")



Session.commit() 

Session.close()
 
            
