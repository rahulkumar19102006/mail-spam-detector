from django.db import models


class PredictionHistory(models.Model):
    message_text = models.TextField()
    prediction_result = models.CharField(max_length=10) # 'spam' or 'ham'
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.prediction_result} - {self.message_text[:20]}..."
