#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 10:46:56 2018

@author: fzqa
"""

from sklearn.datasets import fetch_20newsgroups 
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

#20 categories
categories = [ 'alt.atheism','comp.graphics','comp.os.ms-windows.misc',
'comp.sys.ibm.pc.hardware', 'comp.sys.mac.hardware','comp.windows.x',
'misc.forsale','rec.autos','rec.motorcycles','rec.sport.baseball',
'rec.sport.hockey', 'sci.crypt','sci.electronics',
'sci.med','sci.space','soc.religion.christian',
'talk.politics.misc','talk.politics.guns','talk.politics.mideast',
'talk.religion.misc',
];
              
def bayes(categories,a):
    #get train data
    train_d = fetch_20newsgroups(subset = 'train',categories = categories);
    #get test data
    test_d = fetch_20newsgroups(subset = 'test',categories = categories);
    print(train_d.target_names)
    
    #extract the feature vectors  10000features
    vectorizer = HashingVectorizer(stop_words = 'english',non_negative = True,
                                n_features = 10000)
    
    fea_train = vectorizer.fit_transform(train_d.data)
    fea_test = vectorizer.fit_transform(test_d.data);
    print("the size of train is ",repr(fea_train.shape))
    print("the size of train is ",repr(fea_test.shape))
    print( 'The average feature sparsity is {0:.3f}%'.format(fea_train.nnz/float(fea_train.shape[0]*fea_train.shape[1])*100));
    
    #Naive Bayes classifier for multinomial models  多项式
    clf = MultinomialNB(alpha = a) 
    # 训练集合上进行训练， 估计参数
    clf.fit(fea_train,train_d.target);
    # 对测试集合进行预测 保存预测结果
    pred = clf.predict(fea_test);
    get_result(test_d.target,pred,a);

#模型评估
def get_result(actual,pred,alpha):
    m_precision = metrics.precision_score(actual,pred,average="weighted");
    print("alpha=",alpha,"precision=",m_precision)
    
def main():
    bayes(categories,0.15)

if __name__ == "__main__":
    main()