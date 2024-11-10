import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
import joblib

# Cargar los datos
data = pd.read_csv('/Users/suyeoncho/Downloads/oracle_AI/consolidated_data.csv')

# Preprocesar datos: seleccionar columnas de síntomas y severidades
symptom_columns = [col for col in data.columns if 'Symptom_' in col and 'severity' not in col]
severity_columns = [col for col in data.columns if 'severity' in col]

# Llenar valores ausentes con 0 para severidad
data[severity_columns] = data[severity_columns].fillna(0)

# Crear la entrada (X) con síntomas y severidad, y la salida (y) con 'Disease'
X = data[symptom_columns + severity_columns]
y = data['Disease']

# Dividir en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el preprocesador para codificar las columnas de síntomas
preprocessor = ColumnTransformer(
    transformers=[
        ('symptom_encoder', OneHotEncoder(), symptom_columns)
    ],
    remainder='passthrough'  # Mantiene las columnas de severidad como están
)

# Crear y entrenar el modelo en un pipeline
model = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', MLPClassifier(hidden_layer_sizes=(64, 32), max_iter=300, random_state=42))
])

# Entrenar el modelo
model.fit(X_train, y_train)

# Guardar el modelo entrenado
joblib.dump(model, '/Users/suyeoncho/Downloads/oracle_AI/modelo_entrenado.pkl')
print("Modelo entrenado y guardado exitosamente.")
