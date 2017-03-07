# ResNets experiments on cifar10 with caffe

## Citation
	@article{He2015,
	    author = {Kaiming He and Xiangyu Zhang and Shaoqing Ren and Jian Sun},
	    title = {Deep Residual Learning for Image Recognition},
	    journal = {arXiv preprint arXiv:1512.03385},
	    year = {2015}
    	}

## Introduction

  This repository reimplements resnet experiments on cifar10 with caffe according to the paper "Deep Residual Learning for Image Recognition" (http://arxiv.org/abs/1512.03385).
  The data augmentation means 4 pixels are padded on each side for every images during training.You can get cifar10_train(test)_lmdb by script/convert_cifar10_lmdb.py,cifar10_pad4_train(test)_lmdb by script/pad_cifar10.py and mean_pad.binaryproto by script/compute_mean.py.

## Structure

  The network structure is here(we only list the network of 20 depth):
  	<br/>[ResNet_20](http://ethereon.github.io/netscope/#/gist/544993a5985bb87e11443dc1dbcb4881)
  	<br/>[PlainNet_20](http://ethereon.github.io/netscope/#/gist/18200c298ed00d846cfd511babe70a9b)
	
## Usage
  First, you should make sure that your caffe is correctly installed.You can follow this blog's instructions if you use windows.(https://zhuanlan.zhihu.com/p/22129880)

  for training
  ```
  caffe train -solver=solver.prototxt -gpu 0
  ```

  for testing 
  ```
  caffe test -model=res20_cifar_train_test.prototxt -weights=ResNet_20.caffemodel -iterations=100 -gpu 0
  ```
  
  
## Result
###Result with data augmentation:
![ResNet(DA)](https://github.com/fish145/ResNet-on-Cifar10/blob/master/data_augmentation/accuracy.png)
	model|Repeated|Reference
	:---:|:---:|:---:
	20lyaers|91.94%|91.25%
	32layers|92.70%|92.49%%
	44layers|93.01%|92.83%
	56layers|93.19%|93.03%
	110layers|93.56%|93.39%
**notice**:We got even better results than the original paper
###Compare result(without data augmentation):
<br/>![compare](https://github.com/fish145/ResNet-on-Cifar10/blob/master/without_data_augmentation/compare.png)
	model|PlainNet|ResNet
	:---:|:---:|:---:
	20lyaers|90.10%|91.74%
	32layers|86.96%|92.23%%
	44layers|84.45%|92.67%
	56layers|85.26%|93.09%
	110layers||93.27%
##Blog address
 <br/>[zhihu](https://zhuanlan.zhihu.com/p/22071346)

