import lmdb
import cv2
import caffe
from caffe.proto import caffe_pb2

env1=lmdb.open('cifar10_train_lmdb')
txn1=env1.begin()
cursor=txn1.cursor()
datum=caffe_pb2.Datum()

env2=lmdb.open('cifar10_pad4_train_lmdb',map_size=50000*1000*10)
txn2=env2.begin(write=True)

count=0
for key,value in cursor:
    datum.ParseFromString(value)
    label=datum.label

    data=caffe.io.datum_to_array(datum)
    img=data.transpose(1,2,0)
    pad=cv2.copyMakeBorder(img,4,4,4,4,cv2.BORDER_REFLECT)

    array=pad.transpose(2,0,1)
    datum1=caffe.io.array_to_datum(array,label)

    str_id='{:08}'.format(count)
    txn2.put(str_id,datum1.SerializeToString())

    count+=1
    if count%1000 ==0:
        print('already handled with {} pictures'.format(count))
        txn2.commit()
        txn2=env2.begin(write=True)

txn2.commit()
env2.close()
env1.close()

