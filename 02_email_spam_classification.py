# Email classification: Normal (ham) vs Spam using Naive Bayes, KNN and SVM.
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import make_pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report, accuracy_score

# Optional CSV: columns must be "text" and "label" (ham/spam).
try:
    df=pd.read_csv("emails.csv")
    X=df["text"].astype(str); y=df["label"].astype(str).str.lower()
except FileNotFoundError:
    X=pd.Series([
      "Congratulations you won a free prize click now","Meeting moved to 3 pm tomorrow",
      "Claim your cash reward now","Please review the attached project report",
      "You have won lottery send bank details","Can we discuss the assignment today",
      "Urgent claim your free gift","The lecture starts at ten"
    ]*20)
    y=pd.Series(["spam","ham","spam","ham","spam","ham","spam","ham"]*20)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.25,random_state=42,stratify=y)
models={"Naive Bayes":make_pipeline(TfidfVectorizer(),MultinomialNB()),
        "K-Nearest Neighbors":make_pipeline(TfidfVectorizer(),KNeighborsClassifier(n_neighbors=3)),
        "Support Vector Machine":make_pipeline(TfidfVectorizer(),LinearSVC())}
for name,model in models.items():
    model.fit(X_train,y_train); pred=model.predict(X_test)
    print(f"\n{name} accuracy: {accuracy_score(y_test,pred):.3f}")
    print(classification_report(y_test,pred,zero_division=0))
