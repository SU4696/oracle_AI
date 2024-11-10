import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
import joblib
import os

# Cargar los datos
data = pd.read_csv('/Users/suyeoncho/Downloads/oracle_AI/consolidated_data.csv')

# Seleccionar columnas de síntomas y severidades
symptom_columns = [col for col in data.columns if 'Symptom_' in col and 'severity' not in col]
severity_columns = [col for col in data.columns if 'severity' in col]

# Llenar valores ausentes en severidad con 0 y en síntomas con "None"
data[severity_columns] = data[severity_columns].fillna(0)
data[symptom_columns] = data[symptom_columns].fillna("None")

# Crear la entrada (X) y la salida (y)
X = data[symptom_columns + severity_columns]
y = data['Disease']

# Dividir en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el preprocesador para codificar las columnas de síntomas
preprocessor = ColumnTransformer(
    transformers=[
        ('symptom_encoder', OneHotEncoder(handle_unknown='ignore'), symptom_columns)
    ],
    remainder='passthrough'  # Mantener las columnas de severidad como están
)

# Crear y entrenar el modelo en un pipeline
model = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', MLPClassifier(hidden_layer_sizes=(64, 32), max_iter=300, random_state=42))
])

try:
    print("Iniciando el entrenamiento del modelo...")
    model.fit(X_train, y_train)
    print("Entrenamiento completado.")

    # Intentar guardar el modelo en el directorio actual
    output_path = '/Users/suyeoncho/Downloads/oracle_AI/modelo_entrenado.pkl'
    joblib.dump(model, output_path)

    if os.path.exists(output_path):
        print(f"Modelo guardado exitosamente en {output_path}")
    else:
        print("Error: No se pudo encontrar el archivo guardado.")
except Exception as e:
    print(f"Ocurrió un error durante el entrenamiento o guardado del modelo: {e}")
