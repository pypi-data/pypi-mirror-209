import datetime as dt

import numpy as np
from sklearn import tree, ensemble
from . import xpd, xnp, xplt

MIN_TIME = dt.datetime.min.time()


def x_monkey_patch(aggressive=False):
    xpd.monkey_patch(aggressive=aggressive)
    xnp.monkey_patch()
    xplt.monkey_patch()


def split_X_y(df, target):
    df = df.copy()
    y = df[target]
    del df[target]
    return df, y


def date_to_datetime(d):
    return dt.datetime.combine(d, MIN_TIME)


def x_convert_rf_classifier_to_reg(clf):
    """
    Warning: this function KILLS clf (can't use it after)
    """
    assert len(clf.classes_) == 2, 'only supported for binary situation'

    X = np.zeros((1, clf.n_features_in_))
    y = np.zeros(1)
    reg = ensemble.RandomForestRegressor(n_estimators=clf.n_estimators)
    reg.fit(X, y)
    reg.estimators_ = clf.estimators_.copy()
    estimators2 = []
    for est in reg.estimators_:
        def pred_prob(xx, **kwargs):
            return est.predict_proba(xx)[:, 1]
        est.predict = pred_prob
        tr = tree.DecisionTreeRegressor()
        tr.fit(X, y)

        tr.tree_ = est.tree_
        vals = tr.tree_.value
        for i0 in range(vals.shape[0]):
            for i1 in range(vals.shape[1]):
                sum_val = vals[i0, i1].sum()
                for i2 in range(vals.shape[2]):
                    vals[i0, i1, i2] = vals[i0, i1, 1] / sum_val

        estimators2.append(tr)
    reg.estimators_ = estimators2
    return reg
