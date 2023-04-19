from tkinter import messagebox
import sqlite3

class ConstructorBD:
    def conexionBD(self):
        try: 
            conexion = sqlite3.connect("C:/Users/mimoc/OneDrive/UNIVERSIDAD/5 QUINTO CUATRIMESTRE/Fundamentos de programación orientada a objetos/segundo parcial/GitHub/POOS182/EXAMEN_3Parcial/BDExportaciones.db")
            print('Conectado a BD')
            return conexion
        except sqlite3.OperationalError:
            print('No se logro conectar con BD')

    def InsertarRegistro(self, trans, aduana):
        conx = self.conexionBD()
        if(trans == '' or aduana == ''):
            messagebox.showwarning('Advertencia', 'Formulario incompleto')
            conx.close()
        else:
            Cursor = conx.cursor()
            datos = (trans, aduana)
            sqlInsert = 'insert into TBPedimentos(Tranporte, Aduana) values (?,?)'
            Cursor.execute(sqlInsert, datos)
            conx.commit()
            conx.close()
            messagebox.showinfo('Registro', 'El registro se ha guardado exitosamente.')

            #aereo, maritimo, terrestre
    def eliminarRegistros(self, id):
        conx = self.conexionBD()
        if(id == ''):
            messagebox.showwarning('Advertencia', 'Escribe un ID')
            conx.close
        else:
            conx = self.conexionBD()
            cursor = conx.cursor() 
            sqlDelete = 'delete from TBPedimentos where  IDExpo = "'+id+'"' 
            cursor.execute(sqlDelete) 
            conx.commit()
            conx.close() 
            messagebox.showinfo('Exito', 'El registro fue eliminado exitosamente')