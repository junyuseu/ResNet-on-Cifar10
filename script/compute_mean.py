import caffe
import lmdb
import numpy as np
import cv2
from caffe.proto import caffe_pb2
import time
lmdb_env=lmdb.open('residual/baseline/cifar10_pad4_train_lmdb')
lmdb_txn=lmdb_env.begin()
lmdb_cursor=lmdb_txn.cursor()
datum=caffe_pb2.Datum()
#test={}
N=0
mean = np.zeros((1, 3, 40, 40))
beginTime = time.time()
for key,value in lmdb_cursor:
    datum.ParseFromString(value)
    data=caffe.io.datum_to_array(datum)
    image=data.transpose(1,2,0)
    mean[0][0] += image[:, :, 0]
    mean[0][1] += image[:, :, 1]
    mean[0][2] += image[:, :, 2]
    N+=1
    if N % 1000 == 0:
        elapsed = time.time() - beginTime
        print("Processed {} images in {:.2f} seconds. "
              "{:.2f} images/second.".format(N, elapsed,
                                             N / elapsed))
mean[0]/=N
blob = caffe.io.array_to_blobproto(mean)
with open('mean_pad.binaryproto', 'wb') as f:
    f.write(blob.SerializeToString())

lmdb_env.close()
'''
blob = caffe.proto.caffe_pb2.BlobProto()
data = open( 'mean.binaryproto' , 'rb' ).read()
blob.ParseFromString(data)
arr = np.array( caffe.io.blobproto_to_array(blob) )
print arr
'''
