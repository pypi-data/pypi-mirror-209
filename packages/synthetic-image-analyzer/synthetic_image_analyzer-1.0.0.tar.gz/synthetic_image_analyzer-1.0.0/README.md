# privacy analyzer
This repository analyzes the privacy breach risk of synthetic images. To be specific, it performs a metric-based membership inference attack (MIA) without access to the generative model.

For a detailed explaination of privacy attack in generative models, please refer to section 6.3 in [this review](https://arxiv.org/abs/2209.09239). This review paper focuses on non-imaging data, but these methods are also applicable to image data.

## Method description
The membership inference attack assumes that the attacker only have the access to data, while do not have the access to the generative models. The attacker can obtain a set of complete records, i.e., all attributes are publicized, and by observing the synthetic dataset S, the attacker will determining whether a given real data record was part of the synthetic model’ training dataset.

We used a simple metric-based membership inference attack (MIA) in an unsupervised manner. We presume that, the synthetic records must bear similarity with the records that were used to generate them [22]. As is shown in the figure below. If a synthetic data point is close to this real data point than any other real data points, this synthetic dataset caused a privacy breach. In this figure, S1 and S2 caused a privacy breach, and the overall privacy breach risk of this synthetic dataset is 2/5.

![图片](https://user-images.githubusercontent.com/30890745/225038684-39fcb201-7789-47c1-adc0-f64baf2bdc14.png)

Our method is composed of four steps. Let's assume the syntheitc dataset have a size of 512*512:

1. Feature embedding: Each image is embeded as a discrete feature map using [VQ-VAE2](https://arxiv.org/abs/1906.00446). VQ-VAE quantizes the latent features into a discrete latent space, i.e., each pixel in the latent feature maps is a K-way categorical variable, sampling from 0 to K-1.  We used a two-level latent hierarchy with feature maps of size 32*32 (top) and 64*64 (bottom). Only top features were used to compute privacy breach risk in this repository.
```
sh image_compressing.sh
```

2. Distance calculation: The distance between feature maps were computed by the Hamming distance between data points.

3. Privacy breach calculation

**Step2 and 3 is being optimized. It is too slow currently.
