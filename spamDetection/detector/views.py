from django.shortcuts import render

# Create your views here.
import pandas as pd
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
from .forms import MessageForm

dataset = pd.read_csv('C:/Users/rahul/Downloads/spam (2).csv', encoding='latin1')

from numpy import vectorize
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(dataset['v2'])
y = dataset['v1']

x_train, x_test, y_train, y_test = train_test_split(X,dataset['v1'], test_size=0.2, random_state=42)

model = MultinomialNB()
model.fit(x_train, y_train)

def predict_spam(message):
    message_vector = vectorizer.transform([message])
    prediction = model.predict(message_vector)
    return prediction[0]
 
def Home(request):
    result = None
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['text']
            result = predict_spam(message)
    else:
        form = MessageForm()
        
    return render(request,'home.html',{'form': form,'result': result})
