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

symptom_names = {
    "Symptom_1": "itching",
    "Symptom_2": "skin rash",
    "Symptom_3": "nodal skin eruptions",
    "Symptom_4": "dischromic patches",
    "Symptom_5": "None",
    "Symptom_6": "continuous sneezing",
    "Symptom_7": "shivering",
    "Symptom_8": "chills",
    "Symptom_9": "watering from eyes",
    "Symptom_10": "stomach pain",
    "Symptom_11": "acidity",
    "Symptom_12": "ulcers on tongue",
    "Symptom_13": "vomiting",
    "Symptom_14": "cough",
    "Symptom_15": "chest pain",
    "Symptom_16": "yellowish skin",
    "Symptom_17": "nausea",
    "Symptom_18": "loss of appetite",
    "Symptom_19": "abdominal pain",
    "Symptom_20": "yellowing of eyes",
    "Symptom_21": "burning micturition",
    "Symptom_22": "spotting urination",
    "Symptom_23": "passage of gases",
    "Symptom_24": "internal itching",
    "Symptom_25": "indigestion",
    "Symptom_26": "muscle wasting",
    "Symptom_27": "patches in throat",
    "Symptom_28": "high fever",
    "Symptom_29": "extra marital contacts",
    "Symptom_30": "fatigue",
    "Symptom_31": "weight loss",
    "Symptom_32": "restlessness",
    "Symptom_33": "lethargy",
    "Symptom_34": "irregular sugar level",
    "Symptom_35": "blurred and distorted vision",
    "Symptom_36": "obesity",
    "Symptom_37": "excessive hunger",
    "Symptom_38": "increased appetite",
    "Symptom_39": "polyuria",
    "Symptom_40": "sunken eyes",
    "Symptom_41": "dehydration",
    "Symptom_42": "diarrhoea",
    "Symptom_43": "breathlessness",
    "Symptom_44": "family history",
    "Symptom_45": "mucoid sputum",
    "Symptom_46": "headache",
    "Symptom_47": "dizziness",
    "Symptom_48": "loss of balance",
    "Symptom_49": "lack of concentration",
    "Symptom_50": "stiff neck",
    "Symptom_51": "depression",
    "Symptom_52": "irritability",
    "Symptom_53": "visual disturbances",
    "Symptom_54": "back pain",
    "Symptom_55": "weakness in limbs",
    "Symptom_56": "neck pain",
    "Symptom_57": "weakness of one body side",
    "Symptom_58": "altered sensorium",
    "Symptom_59": "dark urine",
    "Symptom_60": "sweating",
    "Symptom_61": "muscle pain",
    "Symptom_62": "mild fever",
    "Symptom_63": "swelled lymph nodes",
    "Symptom_64": "malaise",
    "Symptom_65": "red spots over body",
    "Symptom_66": "joint pain",
    "Symptom_67": "pain behind the eyes",
    "Symptom_68": "constipation",
    "Symptom_69": "toxic look (typhos)",
    "Symptom_70": "belly pain",
    "Symptom_71": "yellow urine",
    "Symptom_72": "receiving blood transfusion",
    "Symptom_73": "receiving unsterile injections",
    "Symptom_74": "coma",
    "Symptom_75": "stomach bleeding",
    "Symptom_76": "acute liver failure",
    "Symptom_77": "swelling of stomach",
    "Symptom_78": "distention of abdomen",
    "Symptom_79": "history of alcohol consumption",
    "Symptom_80": "fluid overload",
    "Symptom_81": "phlegm",
    "Symptom_82": "blood in sputum",
    "Symptom_83": "throat irritation",
    "Symptom_84": "redness of eyes",
    "Symptom_85": "sinus pressure",
    "Symptom_86": "runny nose",
    "Symptom_87": "congestion",
    "Symptom_88": "loss of smell",
    "Symptom_89": "fast heart rate",
    "Symptom_90": "rusty sputum",
    "Symptom_91": "pain during bowel movements",
    "Symptom_92": "pain in anal region",
    "Symptom_93": "bloody stool",
    "Symptom_94": "irritation in anus",
    "Symptom_95": "cramps",
    "Symptom_96": "bruising",
    "Symptom_97": "swollen legs",
    "Symptom_98": "swollen blood vessels",
    "Symptom_99": "prominent veins on calf",
    "Symptom_100": "weight gain",
    "Symptom_101": "cold hands and feets",
    "Symptom_102": "mood swings",
    "Symptom_103": "puffy face and eyes",
    "Symptom_104": "enlarged thyroid",
    "Symptom_105": "brittle nails",
    "Symptom_106": "swollen extremities",
    "Symptom_107": "abnormal menstruation",
    "Symptom_108": "muscle weakness",
    "Symptom_109": "anxiety",
    "Symptom_110": "slurred speech",
    "Symptom_111": "palpitations",
    "Symptom_112": "drying and tingling lips",
    "Symptom_113": "knee pain",
    "Symptom_114": "hip joint pain",
    "Symptom_115": "swelling joints",
    "Symptom_116": "painful walking",
    "Symptom_117": "movement stiffness",
    "Symptom_118": "spinning movements",
    "Symptom_119": "unsteadiness",
    "Symptom_120": "pus filled pimples",
    "Symptom_121": "blackheads",
    "Symptom_122": "scarring",
    "Symptom_123": "bladder discomfort",
    "Symptom_124": "foul smell of urine",
    "Symptom_125": "continuous feel of urine",
    "Symptom_126": "skin peeling",
    "Symptom_127": "silver like dusting",
    "Symptom_128": "small dents in nails",
    "Symptom_129": "inflammatory nails",
    "Symptom_130": "blister",
    "Symptom_131": "red sore around nose",
    "Symptom_132": "yellow crust ooze"
}


class ChatbotMedicoRural:
    def __init__(self):
        # Inicializar todos los síntomas en 0 en el DataFrame de entrada
        self.evidencia = {symptom: 0 for symptom in symptom_columns}
        self.sintomas_pendientes = symptom_columns.copy()

    def iniciar_evaluacion(self):
        self.preguntar_sintoma()
    
    def preguntar_sintoma(self):
        if not self.sintomas_pendientes:
            self.evaluar_urgencia()
            return
        
        # Preguntar sobre cada síntoma usando nombres descriptivos
        sintoma = self.sintomas_pendientes.pop(0)
        sintoma_descriptivo = symptom_names.get(sintoma, sintoma)
        
        respuesta = messagebox.askquestion("Síntoma", f"¿Tiene el síntoma '{sintoma_descriptivo}'?")
        
        if respuesta == 'yes':
            # Marcar el síntoma como presente
            self.evidencia[sintoma] = 1
        
        self.preguntar_sintoma()
    
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
