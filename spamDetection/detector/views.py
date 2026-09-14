from django.shortcuts import render, redirect
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from .forms import MessageForm
from .models import PredictionHistory

# Global variables so views can share the active ML components
model = None
vectorizer = None

def train_ml_model():
    """Loads base data, appends SQLite overrides, and trains the model."""
    global model, vectorizer
    
    # 1. Load Base Dataset
    base_data = pd.read_csv('C:/Users/rahul/Downloads/spam (2).csv', encoding='latin1')
    # Standardize columns to match our database names
    df_base = pd.DataFrame({
        'v1': base_data['v1'].str.lower(),
        'v2': base_data['v2']
    })
    
    # 2. Extract corrections from SQLite database
    all_logs = PredictionHistory.objects.all()
    user_inputs = []
    for log in all_logs:
        user_inputs.append({
            'v1': log.prediction_result.lower(),
            'v2': log.message_text
        })
        
    if user_inputs:
        df_logs = pd.DataFrame(user_inputs)
        # Combine the original dataset with corrected user entries
        final_df = pd.concat([df_base, df_logs], ignore_index=True)
    else:
        final_df = df_base

    # 3. Vectorize and Fit Model
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(final_df['v2'])
    y = final_df['v1']
    
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = MultinomialNB()
    model.fit(x_train, y_train)
    print("🤖 Model successfully trained with combined data context!")

# Run initial training on startup setup
train_ml_model()


def predict_spam(message):
    message_vector = vectorizer.transform([message])
    prediction = model.predict(message_vector)
    # Extract prediction element safely
    return prediction[0] if hasattr(prediction, '__len__') else prediction


def home(request):
    result = None
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['text']
            result = predict_spam(message)
            
            # Save history to SQLite database
            PredictionHistory.objects.create(
                message_text=message,
                prediction_result=result
            )
    else:
        form = MessageForm()
        
    history = PredictionHistory.objects.all().order_by('-created_at')[:10]
    return render(request, 'home.html', {'form': form, 'result': result, 'history': history})


def clear_history(request):
    if request.method == 'POST':
        PredictionHistory.objects.all().delete()
    return redirect('home')


# NEW: Toggle prediction classification choice if model gets it wrong
def toggle_status(request, log_id):
    if request.method == 'POST':
        log = PredictionHistory.objects.get(id=log_id)
        # Flip the status
        log.prediction_result = 'ham' if log.prediction_result == 'spam' else 'spam'
        log.save()
    return redirect('home')


# NEW: View route to manually trigger retraining via dashboard UI
def retrain_model(request):
    if request.method == 'POST':
        train_ml_model()
    return redirect('home')
