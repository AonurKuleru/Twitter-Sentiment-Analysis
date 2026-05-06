import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score


file_path = r'C:\Proje\training.1600000.processed.noemoticon.csv'
df = pd.read_csv(file_path, encoding='latin-1', names=["target", "ids", "date", "flag", "user", "text"])

df = df[['target', 'text']]
df['target'] = df['target'].replace(4, 1)


df = pd.concat([df[df['target']==1].sample(50000), df[df['target']==0].sample(50000)])


def clean(text):
    text = text.lower()
    text = re.sub(r'@[A-Za-z0-9_]+|https?://[A-Za-z0-9./]+|[^a-z\s]', '', text)
    return text.strip()

print("Metinler temizleniyor ve model eğitiliyor...")
df['text'] = df['text'].apply(clean)


X_train, X_test, y_train, y_test = train_test_split(df['text'], df['target'], test_size=0.2, random_state=42)


vectorizer = TfidfVectorizer(max_features=5000, stop_words='english')
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

model = LogisticRegression(max_iter=1000)
model.fit(X_train_tfidf, y_train)


y_pred = model.predict(X_test_tfidf)
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(7, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False,
            xticklabels=['Negatif', 'Pozitif'], 
            yticklabels=['Negatif', 'Pozitif'],
            annot_kws={"size": 15, "weight": "bold"})

plt.title(f'Duygu Analizi Başarı Oranı: %{accuracy_score(y_test, y_pred)*100:.1f}', pad=20)
plt.xlabel('Modelin Tahmini')
plt.ylabel('Gerçek Durum')
plt.show()
