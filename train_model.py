from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_wine
import joblib

# Загрузка данных
wine = load_wine()
X, y = wine.data, wine.target

# Обучение модели
model = RandomForestClassifier()
model.fit(X, y)

# Сохранение модели
joblib.dump(model, 'wine_model.joblib')