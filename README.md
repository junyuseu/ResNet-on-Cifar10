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
  The data augmentation means 4 pixels are padded on each side for every images during training. You can make datasets prepared by using the scripts.

## Structure

  The network structure is here(we only list the network of 20 depth):
  	<br/>[ResNet_20](http://ethereon.github.io/netscope/#/gist/544993a5985bb87e11443dc1dbcb4881)
  	<br/>[PlainNet_20](http://ethereon.github.io/netscope/#/gist/18200c298ed00d846cfd511babe70a9b)
	
## Usage
  First, you should make sure that your caffe is correctly installed. You can follow this blog's instructions if you use windows.(https://zhuanlan.zhihu.com/p/22129880)

  for training
  ```
  caffe train -solver=solver.prototxt -gpu 0
  ```

  for testing 
  ```
  caffe test -model=res20_cifar_train_test.prototxt -weights=ResNet_20.caffemodel -iterations=100 -gpu 0
  ```
  
  
## Result
### Result with data augmentation:
		model|Repeated|Reference
		:---:|:---:|:---:
		20 lyaers|91.94%|91.25%
		32 layers|92.70%|92.49%
		44 layers|93.01%|92.83%
		56 layers|93.19%|93.03%
		110 layers|93.56%|93.39%
**notice**:'Repeated' means reimplementation results and 'Reference' means result in the paper.**We got even better results than the original paper**

### Compare result(without data augmentation):
		model|PlainNet|ResNet
		:---:|:---:|:---:
		20 lyaers|90.10%|91.74%
		32 layers|86.96%|92.23%
		44 layers|84.45%|92.67%
		56 layers|85.26%|93.09%
		110 layers|X|93.27%

## Blog address
 <br/>[zhihu](https://zhuanlan.zhihu.com/p/22071346)

