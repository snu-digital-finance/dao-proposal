from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

vectorizer = TfidfVectorizer(
    ngram_range=(1, 2), min_df=0.05, max_df=0.90)


def cosine(texts):
    tfidf_matrix = vectorizer.fit_transform(texts)
    cos_mat = cosine_similarity(tfidf_matrix, tfidf_matrix)
    return np.where(cos_mat > 1, 1, cos_mat), tfidf_matrix


def filter_similar(cos_mat, threshold=0.75):
    selected_rows = []
    visited = set()

    for i in range(len(cos_mat)):
        if i not in visited:
            selected_rows.append(i)
            for j in range(i + 1, len(cos_mat)):
                if cos_mat[i][j] >= threshold:
                    visited.add(j)

    return np.unique(np.array(selected_rows))
