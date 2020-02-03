# Defending Against Physically Realizable Attacks on Image Classification

### Tong Wu, Liang Tong, Yevgeniy Vorobeychik
 

[[arXiv]](https://arxiv.org/abs/1909.09552)   **first version**


###ABSTRACT
We study the problem of defending deep neural network approaches for image classification from physically realizable attacks. First, we demonstrate that the two most scalable and effective methods for learning robust models, adversarial training with PGD attacks and randomized smoothing, exhibit very limited effec- tiveness against three of the highest profile physical attacks. Next, we propose a new abstract adversarial model, rectangular occlusion attacks, in which an ad- versary places a small adversarially crafted rectangle in an image, and develop two approaches for efficiently computing the resulting adversarial examples. Fi- nally, we demonstrate that adversarial training using our new attack yields image classification models that exhibit high robustness against the physically realizable attacks we study, offering the first effective generic defense against such attacks.

<img src="Figure/phattack.png" height="210" width="860">

## Prepare for the experiment 
1. Clone this repository: 
```
git clone https://github.com/tongwu2020/phattacks.git
```

2. Install the dependencies:
```
conda create -n phattack
conda activate phattack
# Install following packages:
# See https://pytorch.org/ for the correct command for your system to install correct version of Pytorch 
conda install scipy pandas statsmodels matplotlib seaborn numpy 
conda install -c conda-forge opencv
# May need more packages 
```

3. Download our trained models from:

4. Run specific task:

```
cd glass 
```
or 

```
cd sign
```




Contact [tongwu@wustl.edu]() with any questions. 