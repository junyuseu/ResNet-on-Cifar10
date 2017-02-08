### Citation
	@article{He2015,
	    author = {Kaiming He and Xiangyu Zhang and Shaoqing Ren and Jian Sun},
	    title = {Deep Residual Learning for Image Recognition},
	    journal = {arXiv preprint arXiv:1512.03385},
	    year = {2015}
    	}

## Introduction

  Reimplementation ResNet on cifar10
  <br/>You can get cifar10_train(test)_lmdb by script/convert_cifar10_lmdb.py and cifar10_pad4_train(test)_lmdb by script/pad_cifar10.py
  and mean_pad.binaryproto by script/compute_mean.py

## Structure

  The network structure is here(we only list the network of 20 depth):
  	<br/>[ResNet_20](http://ethereon.github.io/netscope/#/gist/544993a5985bb87e11443dc1dbcb4881)
  	<br/>[PlainNet_20](http://ethereon.github.io/netscope/#/gist/18200c298ed00d846cfd511babe70a9b)
	
## Usage

  for training
  ```
  caffe train -solver=solver.prototxt -gpu 0
  ```

  for testing 
  ```
  caffe test -model=res20_cifar_train_test.prototxt -weights=ResNet_20.caffemodel -iterations=100 -gpu 0
  ```
  
  
## Result
#Result with data augmentation:
![ResNet(DA)](https://github.com/fish145/ResNet-on-Cifar10/blob/master/data_augmentation/accuracy.png)
#Compare result(without data augmentation):
<br/>![compare](https://github.com/fish145/ResNet-on-Cifar10/blob/master/without_data_augmentation/compare.png)
  
##Blog address
 <br/>[zhihu](https://zhuanlan.zhihu.com/p/22071346)
 <br/>[csdn](http://blog.csdn.net/yj3254/article/details/52244402)

