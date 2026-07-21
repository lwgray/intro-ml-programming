"""Bake the weeks 1-5 datasets into the image so class days start warm.

Everything sklearn/seaborn fetches at runtime lands in the caches pointed to by
SCIKIT_LEARN_DATA / SEABORN_DATA, which are set image-wide, so the notebooks
find them without modification. The UCI files that notebooks read directly by
URL can't be cached transparently; offline copies are kept under /opt/data/uci
as insurance against archive.ics.uci.edu outages on class day.
"""

import os
import time
import urllib.request


def retry(fn, attempts=4):
    for i in range(attempts):
        try:
            return fn()
        except Exception as e:
            if i == attempts - 1:
                raise
            print(f'attempt {i + 1} failed ({e}); retrying...')
            time.sleep(10 * (i + 1))


from sklearn.datasets import fetch_california_housing, fetch_openml

retry(lambda: fetch_california_housing())                                        # week 1
retry(lambda: fetch_openml('boston', version=1, as_frame=True, parser='auto'))   # week 1 day 2
retry(lambda: fetch_openml(data_id=537, as_frame=True))                          # week 1
retry(lambda: fetch_openml(name='adult', version=2, as_frame=True, parser='auto'))  # weeks 3-4

import seaborn as sns

retry(lambda: sns.load_dataset('titanic'))                                       # week 2

UCI_URLS = [
    'https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data',
    'https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data',
    'https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data',
    'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv',
]
os.makedirs('/opt/data/uci', exist_ok=True)
for url in UCI_URLS:
    dest = os.path.join('/opt/data/uci', url.rsplit('/', 1)[1])
    retry(lambda u=url, d=dest: urllib.request.urlretrieve(u, d))

print('part1 prefetch complete')
