from flask_sqlalchemy import SQLAlchemy

from models import AssignedTask, User
from ludaya.ludaya import db
from datetime import datetime

import nltk
import string
from nltk import tokenize

from electronics import ELECTRONICS

# Get default English stopwords and extend with punctuation
stopwords = nltk.corpus.stopwords.words('english')
stopwords.extend(string.punctuation)
stopwords.append('')

def is_ci_token_stopword_set_match(a, b, threshold=0.5):
    """Check if a and b are matches."""
    tokens_a = [token.lower().strip(string.punctuation) for token in tokenize.wordpunct_tokenize(a) \
                    if token.lower().strip(string.punctuation) not in stopwords]
    tokens_b = [token.lower().strip(string.punctuation) for token in tokenize.wordpunct_tokenize(b) \
                    if token.lower().strip(string.punctuation) not in stopwords]

    # Calculate Jaccard similarity
    ratio = len(set(tokens_a).intersection(tokens_b)) / float(len(set(tokens_a).union(tokens_b)))
    return ratio


def compare_all_user_tasks():

    tasks = AssignedTask.query.all()

    for task in tasks:
        if task.status == 'submitted':
            for items in ELECTRONICS:
                if task.group == items['name']:
                    for item in items['tasklist']:
                        if item['taskname'] == task.name:
                            ratio = is_ci_token_stopword_set_match(task.name, item['taskanswer'])
                            if ratio < 0.5:
                                tasks.status == "incorect answer"
                            if ratio > 0.4 and ratio < 0.7:
                                tasks.status == "completed"
                            if ratio > 0.6 and ratio < 0.9:
                                tasks.status == "completed"
                            if ratio > 0.8:
                                tasks.status == "completed"
    tasks.save()
