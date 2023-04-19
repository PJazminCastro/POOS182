from tkinter import messagebox
import sqlite3

class ConstructorBD:
    def conexionBD(self):
        try: 
            conexion = sqlite3.connect("C:/Users/mimoc/OneDrive/UNIVERSIDAD/5 QUINTO CUATRIMESTRE/Fundamentos de programación orientada a objetos/segundo parcial/GitHub/POOS182/EXAMEN_3°Parcial/BDExportaciones.db")
            print('Conectado a BD')
            return conexion
        except sqlite3.OperationalError:
            print('No se logro conectar con BD')

    def InsertarRegistro(self, transp, aduana):
        conx = self.conexionBD
        if(transp == '' or aduana == ''):
            messagebox.showwarning('Advertencia', 'Formulario incompleto')
            conx.close()
        else:
            cursor = conx.cursor()
            datos = (transp, aduana)
            sqlInsert = 'insert into TBPedimentos(Transporte, Aduana) values (?,?)'
            cursor.execute(sqlInsert, datos)
            conx.commit()
            conx.close()
            messagebox.showinfo('Registro', 'El registro se ha guardado exitosamente.')

            #aereo, maritimo, terrestre