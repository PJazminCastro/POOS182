from tkinter import messagebox
import sqlite3
import bcrypt

class ControladorBD:
    #CONSTRUCTOR
    

    #CONEXION EN BASE DE DATOS
    def conexionBD(self):
        #intenta correr el codigo, si no se manda al except
        try: 
            conexion = sqlite3.connect('C:/Users/mimoc/OneDrive/UNIVERSIDAD/5 QUINTO CUATRIMESTRE/Fundamentos de programación orientada a objetos/segundo parcial/GitHub/POOS182/TkinterSQLite_P3/RegistroUsuarios.db')#dentro va la ruta de la conexión de la base de datos
            print('Conectado a la BD')
            return conexion
        except sqlite3.OperationalError:
            print('No se puede conectar')

    #METODO INSERTAR USUARIOS
    def guardarUsuario(self, nom, cor, con):
        #1. Llamar conexión (manda a llamar nuestro metodo dentro de la clase)
        conx = self.conexionBD()
        #2. Validar vacios
        if(nom == '' or cor == '' or con == ''):
            messagebox.showwarning('¡Aguas!', 'Formulario incompleto.')
            conx.close()
        #3. Realizar insert a la BD
        else:
            #4. Preparamos las variables necesarias
            cursor = conx.cursor() #se crea un objeto, va a permitir ejecutar las acciones a la BD
            conH = self.encriptarContra(con)
            datos = (nom, cor, conH) #es una lista
            sqlInsert = 'insert into tbregistrados(nombre, correo, contra) values (?,?,?)' #variable propia, insertar en BD, ? = se dejan pendiente los parametros
            #5. Ejecutamos el Insert
            cursor.execute(sqlInsert, datos) #primero el metodo, despues los datos
            
            conx.commit()
            conx.close() #cierra la conexión
            messagebox.showinfo('Exito', 'Usuario guardado')

    #ENCRIPTAR CONTRASEÑA
    def encriptarContra(self, con):
        #1. Preparar contraseña
        conPlana = con
        conPlana = conPlana.encode() #pasa la cadena de caracteres a bit
        salt = bcrypt.gensalt() 
        #2. Encriptamos
        conHa = bcrypt.hashpw(conPlana, salt) #va a contener el pw encriptado
        print(conHa)
        #3. Regresamos la contraseña encriptada
        return conHa

    def consultarUsuario(self, id):
        #1. Realizar conexion a BD
        conx = self.conexionBD()
        #2. Verficar que el ID no sea nulo
        if(id == ''):
            messagebox.showwarning('Cuidado', 'Escribe un ID')
            conx.close
        else:
            #3. Proceder la consulta
            try:
                #4. Preparamos lo necesario (cursor y sqlslect)
                cursor = conx.cursor()
                sqlSelect = 'select * from tbregistrados where id = '+id

                #5. Ejecutar y cerramos conexión
                cursor.execute(sqlSelect)
                RSusuario = cursor.fetchall() #toma lo que este en el cursor para pasarlo a una variable
                conx.close()
                return RSusuario
            except sqlite3.OperationalError:
                print('Error de consulta')

    def consultarUsuarios(self):
        conx = self.conexionBD()
        sqlite3 = 'select * from tbregistrados;'
        cursor = conx.cursor()
        cursor.execute(sqlite3)

        registro = cursor.fetchall()
        for r in registro:
            print (r)