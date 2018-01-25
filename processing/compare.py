from flask_sqlalchemy import SQLAlchemy

from models import AssignedTask, User
from ludaya.ludaya import db
from datetime import datetime

import nltk
import string
from nltk import tokenize

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
            pass

def compare(task, user):
    category = task['name']
    group = task.keys()[0]
    name = task[group]

    new_task = AssignedTask(name=name, group=group, category=category, user_id=user)
    db.session.add(new_task)
    db.session.commit()



def get_user_tasks(user_id):
    tasks = AssignedTask.get_assignedtask(user_id)
    lst = []
    for task in tasks:
        lst.append(task)
    return lst



