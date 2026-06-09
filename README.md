# Backend - Gestion de Stocks (Python/Django)

## 🐍 API Avancée avec Django & Machine Learning

Backend Python avec microservices, prédictions ML et analytics avancées.

## 🚀 Installation

```bash
git clone https://github.com/phbm-coder/gestion-de-stock.git
cd gestion-de-stock
git checkout dev/backend-python

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

## 📁 Structure

```
apps/
├── stock/
│   ├── models.py
│   ├── views.py
│   └── serializers.py
├── analytics/
│   ├── ml_predictor.py
│   └── reports.py
config/
├── settings.py
├── urls.py
└── wsgi.py
```

## 🎯 Fonctionnalités

- ✅ API RESTful complète
- ✅ Machine Learning pour prédictions
- ✅ Celery pour tâches asynchrones
- ✅ Cache Redis
- ✅ Analytics avancées
- ✅ Rapports détaillés

## 🛠️ Technologies

- Python 3.10+
- Django 4.2
- Django REST Framework
- Scikit-learn
- Pandas
- Celery
- Redis
- PostgreSQL

## 📦 Commandes

```bash
# Migrations
python manage.py makemigrations
python manage.py migrate

# Tests
python manage.py test

# Serveur
python manage.py runserver

# Celery worker
celery -A config worker -l info
```
