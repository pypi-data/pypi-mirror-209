import pandas as pd
import sqlite3
from eric_chen_forward import util
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import LogisticRegression
import pickle

class Classifier:

    def __init__(self, alpha=0.2) -> None:
        self.eda_util = util.EDA(alpha=alpha)
        self.categories = []

    def train(self, labels_file=None, paragraphs_file=None, csv_file=None, model_type='SVM'):
        if csv_file:
            df = pd.read_csv(csv_file)
            labels = df['label'].to_list()
            paragraphs = df['paragraph'].to_list()
        else:
            with open(labels_file) as f:
                labels = f.read().splitlines()
            with open(paragraphs_file) as f:
                paragraphs = f.read().splitlines()

        eda_paragraphs = self.eda_util.run_data_augmentation(paragraphs)

        paragraphs.extend(eda_paragraphs)
        labels.extend(labels)
        assert(len(paragraphs) == len(labels))

        self.categories = list(set(labels))

        eda_df = pd.DataFrame()
        eda_df['label'] = labels
        eda_df['paragraph'] = paragraphs
        eda_df['cleaned_text'] = eda_df['paragraph'].apply(lambda x: util.clean_document(x))
        eda_df['num_years'] = eda_df['paragraph'].apply(lambda x: util.num_years(x))

        X = eda_df[['cleaned_text', 'num_years']]
        y = eda_df['label']
        column_transformer = ColumnTransformer([
            ('tfidf', TfidfVectorizer(), 'cleaned_text')
        ])
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=0, stratify=y)

        if model_type == 'SVM':
            sgd = Pipeline([('preprocess', column_transformer),
                ('clf', SGDClassifier(loss='hinge', penalty='l2', alpha=1e-3, random_state=0, tol=None))])
            sgd.fit(X_train, y_train)
            y_pred = sgd.predict(X_test)
            print('SVM with SGD')
            print(f'accuracy: {accuracy_score(y_pred, y_test)}')
            print(classification_report(y_test, y_pred))
            print('-' * 55)

            with open('svm_model.pkl', 'wb') as f:
                pickle.dump(sgd, f)
            
            print(f'Saving SVM model at svm_model.pkl')

            report = classification_report(y_test, y_pred, output_dict=True)
            return report


        elif model_type == 'LR':
            log_reg = Pipeline([('preprocess', column_transformer),
                ('clf', LogisticRegression(C=1e5))])

            log_reg.fit(X_train, y_train)
            y_pred = log_reg.predict(X_test)
            print('Logistic Regression')
            print(f'accuracy: {accuracy_score(y_pred, y_test)}')
            print(classification_report(y_test, y_pred))
            print('-' * 55)

            with open('lr_model.pkl', 'wb') as f:
                pickle.dump(log_reg, f)
            
            print(f'Saving LR model at lr_model.pkl')

            report = classification_report(y_test, y_pred, output_dict=True)
            return report

    def get_categories(self):
        return self.categories
