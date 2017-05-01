from collections import namedtuple, defaultdict
import pickle
import random
import sys

print("Load paper data")
# with open("paperData.pkl", "r") as inFile1:
# 	paperData = pickle.load(inFile1)
features = pickle.load(open('authorFeatures.pkl', 'rb'))

def g(s):
    sum = 0
    for index in range(len(s)):
        sum += pow(10, len(s) - 1 -index) * int(s[index])
    return sum

def getTrainingData():
    X_train = []
    Y_train = []
    X_test = []
    # Get Train Set
    count = 0
    with open(sys.argv[1], 'r') as f:
        line = f.readline()
        while line != '':
            author = line.split('\t')[1]
            authorCitis = g(line.split('\t')[2].strip())
            if author in features:
                X_train.append(features[author])
                Y_train.append(authorCitis)
                count += 1
            else:
                pass
            line = f.readline()
    print("Extracted %d train set"%count)
    # Get Test Set
    count = 0
    with open(sys.argv[2], 'r') as f:
        line = f.readline()
        while line != '':
            count += 1
            author = line.split('\t')[1].strip('\n')
            if author in features:
                X_test.append(features[author])
            else:
                X_test.append([0,0,0,0,0,0])
            line = f.readline()
    print("Extracted %d test set"%count)
    # pickle everything
    with open(sys.argv[3], 'wb') as f1:
        pickle.dump(X_train, f1)
    with open(sys.argv[4], 'wb') as f2:
        pickle.dump(X_test, f2)
    with open(sys.argv[5], 'wb') as f3:
        pickle.dump(Y_train, f3)

getTrainingData()
