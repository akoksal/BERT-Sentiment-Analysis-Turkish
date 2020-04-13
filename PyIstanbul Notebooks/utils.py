import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-notebook')
import matplotlib.patches as mpatches

from sklearn.decomposition import PCA
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report

#Modified from https://web.stanford.edu/class/cs224n/materials/Gensim%20word%20vector%20visualization.html
def display_pca_scatterplot(X, y, sample=100):
    indices = np.random.choice(list(range(len(X))), sample)
    X_sample = np.array(X)[indices]
    y_sample = np.array(y)[indices]

    twodim = PCA().fit_transform(X_sample)[:,:2]
    
    plt.figure(figsize=(6,6))
    for idx, el in enumerate(X_sample):
        if y_sample[idx]==2:
            color = 'g'
        elif y_sample[idx]==1:
            color = 'k'
        else:
            color = 'r'
        plt.scatter(el[0], el[1], edgecolors='k', c=color)

    red_patch = mpatches.Patch(color='red', label='Negatif')
    green_patch = mpatches.Patch(color='green', label='Pozitif')
    black_patch = mpatches.Patch(color='black', label='Nötr')
    plt.legend(handles=[green_patch, black_patch, red_patch])



#Modified from https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_digits.html
def grid_search(tuned_parameters, model, X_train, y_train, X_test, y_test, score='f1_macro', cv=2):
    print("# Tuning hyper-parameters for %s" % score)
    print()

    clf = GridSearchCV(model, tuned_parameters, scoring=score, n_jobs=-1, verbose=5, cv=cv)
    clf.fit(X_train, y_train)

    print("Best parameters set found on development set:")
    print(clf.best_params_)
    print("Grid scores on development set:")
    means = clf.cv_results_['mean_test_score']
    stds = clf.cv_results_['std_test_score']
    for mean, std, params in zip(means, stds, clf.cv_results_['params']):
        print("%0.3f (+/-%0.03f) for %r"
            % (mean, std * 2, params))

    print("\nDetailed classification report:")
    print("The model is trained on the full development set.")
    print("The scores are computed on the full evaluation set.")
    y_true, y_pred = y_test, clf.predict(X_test)
    print(classification_report(y_true, y_pred))

    return clf
