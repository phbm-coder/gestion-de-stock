from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
from django.db.models import Sum
from django.utils import timezone
from datetime import timedelta
from apps.stock.models import StockMovement


class DemandPredictor:
    def __init__(self, product_id):
        self.product_id = product_id
        self.model = LinearRegression()
        self.scaler = StandardScaler()

    def get_historical_data(self, days=90):
        """Récupère les données historiques des 90 derniers jours"""
        start_date = timezone.now() - timedelta(days=days)
        movements = StockMovement.objects.filter(
            product_id=self.product_id,
            movement_type='OUT',
            created_at__gte=start_date
        ).extra(select={'day': 'DATE(created_at)'}).values('day').annotate(total=Sum('quantity'))
        return movements

    def train(self):
        """Entraîne le modèle de prédiction"""
        data = list(self.get_historical_data())
        if len(data) < 7:
            return False

        X = np.array(range(len(data))).reshape(-1, 1)
        y = np.array([d['total'] for d in data])

        X_scaled = self.scaler.fit_transform(X)
        self.model.fit(X_scaled, y)
        return True

    def predict_next_days(self, days=30):
        """Prédit la demande pour les 30 prochains jours"""
        if not self.train():
            return None

        historical_count = len(list(self.get_historical_data()))
        X_future = np.array(range(historical_count, historical_count + days)).reshape(-1, 1)
        X_future_scaled = self.scaler.transform(X_future)
        predictions = self.model.predict(X_future_scaled)

        return [max(0, int(pred)) for pred in predictions]
