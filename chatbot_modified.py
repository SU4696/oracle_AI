import pandas as pd
import joblib
import tkinter as tk
from tkinter import messagebox

# Cargar el modelo entrenado y el archivo de datos consolidado
model = joblib.load('/Users/suyeoncho/Downloads/oracle_AI/modelo_entrenado.pkl')
data = pd.read_csv('/Users/suyeoncho/Downloads/oracle_AI/consolidated_data.csv')

# Crear diccionarios para descripciones y precauciones
description_dict = dict(zip(data['Disease'], data['Description']))
precaution_dict = data.set_index('Disease')[['Precaution_1', 'Precaution_2', 'Precaution_3', 'Precaution_4']].T.to_dict('list')

# Obtener columnas de síntomas y severidades
symptom_columns = [col for col in data.columns if 'Symptom_' in col and 'severity' not in col]

class ChatbotMedicoRural:
    def __init__(self):
        # Inicializar todos los síntomas en 0 en el DataFrame de entrada
        self.evidencia = {symptom: 0 for symptom in symptom_columns}
        # Inicializar lista de síntomas pendientes
        self.sintomas_pendientes = symptom_columns.copy()

    def iniciar_evaluacion(self):
        self.preguntar_sintoma()
    
    def preguntar_sintoma(self):
        if not self.sintomas_pendientes:
            self.evaluar_urgencia()
            return
        
        # Preguntar sobre cada síntoma
        sintoma = self.sintomas_pendientes.pop(0)
        respuesta = messagebox.askquestion("Síntoma", f"¿Tiene el síntoma '{sintoma}'?")
        
        if respuesta == 'yes':
            # Marcar el síntoma como presente
            for column in self.evidencia.keys():
                if sintoma in column:
                    self.evidencia[column] = 1
        
        self.preguntar_sintoma()  # Continuar preguntando
    
    def evaluar_urgencia(self):
        # Crear el DataFrame con la estructura requerida por el modelo
        evidencia_df = pd.DataFrame([self.evidencia])
        
        # Realizar la predicción
        prediction = model.predict(evidencia_df)
        resultado = prediction[0]
        
        # Obtener descripción y precauciones para la enfermedad diagnosticada
        descripcion = description_dict.get(resultado, "No hay descripción disponible.")
        precauciones = precaution_dict.get(resultado, ["No hay recomendaciones disponibles."])
        precauciones_texto = "\n".join(precauciones)
        
        # Mostrar el diagnóstico, descripción y precauciones
        messagebox.showinfo("Diagnóstico", f"El diagnóstico probable es: {resultado}\n\nDescripción:\n{descripcion}\n\nPrecauciones:\n{precauciones_texto}")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal
    chatbot = ChatbotMedicoRural()
    chatbot.iniciar_evaluacion()
