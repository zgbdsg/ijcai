__author__ = 'zhouguobing'
import sys
import os
import datetime
import math
from dateutil.parser import parse
import cPickle as cp

path = os.path.abspath('../data/train_1w.csv')
trainData = open(path, 'r')
path  = os.path.abspath('../data/test_1w.csv')
testData = open(path,'r')

trainFeatureFile = open(os.path.abspath('../data/trainingFeatureTorch.csv'), 'w')
testFeatureFile = open(os.path.abspath('../data/testFeatureTorch.csv'), 'w')

num = 1

for line in trainData:
    # feature = []
    if num == 1:
        num += 1
        continue
    user_id, age_range, gender, merchant_id, label, activity_log = line.strip().split(',')

    acts = activity_log.split('#')
    label = int(label) + 1

    for act in acts:
        # print len(act.strip().split(':'))
        if len(act.strip().split(':')) != 5:
            print act,num
            continue
        item_id,category_id,brand_id,time_stamp,action_type = act.strip().split(':')
        feature = []
        feature.append(str(label))
        feature.append("\"%s\""%(item_id))
        feature.append("\"%s\""%(category_id))
        feature.append("\"%s\""%(brand_id))
        feature.append("\"%s\""%(time_stamp))
        feature.append("\"%s\"\n"%(action_type))
        # feature.append("\"%s,%s\""%(start,end))

        trainFeatureFile.write(",".join(feature))

    num += 1

trainFeatureFile.flush()
trainFeatureFile.close()


num = 1
for line in testData:
    # feature = []
    if num == 1:
        num += 1
        continue
    user_id, age_range, gender, merchant_id, label, activity_log = line.strip().split(',')

    acts = activity_log.split('#')
    label = 1

    for act in acts:
        # print len(act.strip().split(':'))
        if len(act.strip().split(':')) != 5:
            print act,num
            continue
        item_id,category_id,brand_id,time_stamp,action_type = act.strip().split(':')
        feature = []
        feature.append(str(label))
        feature.append("\"%s\""%(item_id))
        feature.append("\"%s\""%(category_id))
        feature.append("\"%s\""%(brand_id))
        feature.append("\"%s\""%(time_stamp))
        feature.append("\"%s\"\n"%(action_type))
        # feature.append("\"%s,%s\""%(start,end))

        testFeatureFile.write(",".join(feature))

    num += 1

testFeatureFile.flush()
testFeatureFile.close()

trainData.close()
