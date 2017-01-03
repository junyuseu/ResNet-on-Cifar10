import os

import numpy as np
import sklearn
import sklearn.linear_model

import lmdb
import caffe

cifar_python_directory = os.path.abspath("cifar-10-batches-py")

print("Converting...")
cifar_caffe_directory=os.path.abspath("cifar10_train_lmdb")
if not os.path.exists(cifar_caffe_directory):
    def unpickle(file):
        import cPickle
        fo=open(file,'rb')
        dict=cPickle.load(fo)
        fo.close()
        return dict

    def shuffle_data(data,labels):
        data,_,labels,_=sklearn.cross_validation.train_test_split(
            data,labels,test_size=0.0,random_state=42
        )
        return data,labels

    def load_data(train_batches):
        data=[]
        labels=[]
        for batch in train_batches:
            d=unpickle(
                os.path.join(cifar_python_directory,batch)
            )
            data.append(d['data'])
            labels.append(np.array(d['labels']))
        data=np.concatenate(data)
        labels=np.concatenate(labels)
        length=len(labels)

        data,labels=shuffle_data(data,labels)
        return data.reshape(length,3,32,32),labels


    X,y=load_data(
        ['data_batch_{}'.format(i) for i in range(1,6)]
    )
    Xt,yt=load_data(['test_batch'])


    env=lmdb.open(cifar_caffe_directory,map_size=50000*1000*5)
    txn=env.begin(write=True)
    count=0
    for i in range(X.shape[0]):
        datum=caffe.io.array_to_datum(X[i],y[i])
        str_id='{:08}'.format(count)
        txn.put(str_id,datum.SerializeToString())

        count+=1
        if count%1000==0:
            print('already handled with {} pictures'.format(count))
            txn.commit()
            txn=env.begin(write=True)

    txn.commit()
    env.close()

    env=lmdb.open('cifar10_test_lmdb',map_size=10000*1000*5)
    txn=env.begin(write=True)
    count=0
    for i in range(Xt.shape[0]):
        datum=caffe.io.array_to_datum(Xt[i],yt[i])
        str_id='{:08}'.format(count)
        txn.put(str_id,datum.SerializeToString())

        count+=1
        if count%1000==0:
            print('already handled with {} pictures'.format(count))
            txn.commit()
            txn=env.begin(write=True)

    txn.commit()
    env.close()

else:
    print("Conversion was already done. Did not convert twice.")