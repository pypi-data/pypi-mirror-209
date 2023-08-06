# eric_chen_forward

To train the model:
```python
from eric_chen_forward.model import Classifier

# alpha parameter used in data augmentation, 0.2 by default
model = Classifier(alpha=0.2)

# option 1
# text files of labels and paragraphs respectively, separated by newlines
# model_type is 'SVM' by default, you can use 'LR' for logistic regression
model.train(labels_file="labels_file_path", paragraphs_file="paragraphs_file_path", model_type='SVM')

# option 2
# csv file must have a 'label' column and 'paragraph' column only, and the column names are hardcoded
model.train(csv_file="csv_file_path", model_type='LR')
```

To use the saved model in code:
```python
with open('model_name.pkl', 'rb') as f:
    model = pickle.load(f)
```

To run the classifier demo:
```python
from eric_chen_forward import url_classifier_demo

API_KEY = [paste api key here]
SEARCH_ENGINE_ID = [paste search engine ID here]
url_classifier_demo.Demo('file path of model.pkl', API_KEY, SEARCH_ENGINE_ID, max_summary_length=100)
```
max_summary_length is set to 100 words by default.

Register an API Key and set up the Programmable Search Engine to be able to use the Google Custom Search API: https://developers.google.com/custom-search/v1/overview

After setting up, the Search engine ID can also be found in the control panel: https://programmablesearchengine.google.com/controlpanel/all