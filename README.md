### Citation
	@article{He2015,
	    author = {Kaiming He and Xiangyu Zhang and Shaoqing Ren and Jian Sun},
	    title = {Deep Residual Learning for Image Recognition},
	    journal = {arXiv preprint arXiv:1512.03385},
	    year = {2015}
    	}

## Introduction

  Reimplementation ResNet on cifar10

## Structure

  The network structure is here:
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
![ResNet-20](https://github.com/fish145/ResNet-on-Cifar10/blob/master/ResNet-20/test.PNG)
![PlainNet-20](https://github.com/fish145/ResNet-on-Cifar10/blob/master/PlainNet-20/test.PNG)
  
##Blog address
 <br/>[zhihu](https://zhuanlan.zhihu.com/p/22071346)
 <br/>[csdn](http://blog.csdn.net/yj3254/article/details/52244402)

