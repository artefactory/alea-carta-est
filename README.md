#
<div align="center">

<h1>Better Capturing Interactions between Products in Retail: <br/>Revisited Negative Sampling for <br/> Basket Choice Modeling</h1>

Jules Désir<sup>1</sup>, Vincent Auriau<sup>1, 2</sup>, Martin Možina<sup>3</sup> and Emmanuel Malherbe<sup>1</sup>

<sup>1</sup> <sub> [Artefact Research Center](https://www.artefact.com/technologies/artefact-research-center/), </sub> <sup>2</sup> <sub>[*MICS*](https://arcade.pages.centralesupelec.fr/) - CentraleSupélec,</sub> <sup>3</sup> <sub> [Fortenova Grupa](https://fortenova.hr/en/home/groups-strength/) </sub>


In [ECML-PKDD 2025](https://ecmlpkdd.org/2025/). <br>
[[Full Paper]](#)  [[Appendices]](./Appendices.pdf)  [[Oral Presentation]](#)<br>

</div>

> **Abstract:** *Brick-and-mortar retailers face many different challenges that involve understanding thoroughly its products catalog and customer preferences. In particular, assortment optimization - proposing the ideal mix of products - and promotion planning hold a pivotal role in their strategy. By leveraging sales data, retailers can make informed decisions on which products to sell and how to manage inventory, based on customer preferences as well as regional and seasonal trends. It is especially crucial to capture interactions between products, in order to minimize the number of items that cannibalize each other’s sales and to ensure that complementary products, which are often purchased together, are conjointly available and sold across all stores. In this paper, we propose a model of shopping basket that learns embeddings to represent interactions between products, prices and stores. Our model is built to uncover sales patterns from very large transaction datasets. In particular, the optimization loss is computed with random negative samples in order to overcome the computational bottlenecks that arise with large number of items. Our experiments on synthetic data show the efficiency of drawing such negative samples based on the actual assortment of available products, with better results than approaches from the literature. We also validate our approach by training and evaluating our model on a dataset composed of billions of transactions from a leading European retail company. Our model showcases promising applications in the sector of retail, with enriched interfaces to efficiently support category managers.*

# 🌿 Installation

First you can clone the repository:

```bash
git clone git@github.com:artefactory/alea-carta-est.git
```

To import and train the models you will need the [choice-learn](https://github.com/artefactory/choice-learn) library. You can pip install it:

```bash
pip install choice-learn
```

If you want to specifically run the experiments, you can install all the dependencies at once with:

```bash
pip install -r requirements.txt
```

# 🌿 Synthetic Experiments

# 🌿 Train the model on your own dataset
You can train the model on your own dataset once it is instantiated as a ```TripDataset``` with:
```python
from choice_learn.basket_models import AleaCarta

dataset = your_own_dataset()

model = AleaCarta()
model.fit(data)
```
You can check the [notebook](./notebooks/train_on_your_own_data.ipynb)[![Open In Colab](https://img.shields.io/badge/-grey?logo=googlecolab)](https://colab.research.google.com/github/artefactory/alea-carta-est/blob/main/notebooks/train_on_your_own_data.ipynb)

You can also check [choice-learn](https://github.com/artefactory/choice-learn/blob/main/notebooks/basket_models/alea_carta.ipynb) and its [documentation](https://artefactory.github.io/choice-learn/references/basket_models/references_shopper/) or contact us if you have any question.
# 🌿 Citation

If you find our work or any of its feature useful for your research, consider starring the repository and citing our paper:

<a href="https://ecmlpkdd.org/">
<img align="left" width="100"src="https://ecmlpkdd-storage.s3.eu-central-1.amazonaws.com/ECML_1_e012008d41.png" />
</a>

```bash
@article{
  doi = {},
  url = {},
  year = {},
  publisher = {},
  volume = {},
  number = {},
  pages = {},
  author = {},
  title = {},
  journal = {} }
```

If you make use of the choice-learn library you also cite us:
If you consider this package or any of its feature useful for your research, consider citing our [paper](https://joss.theoj.org/papers/10.21105/joss.06899):

<a href="https://joss.theoj.org/papers/10.21105/joss.06899">
<img align="left" width="100"src="https://github.com/openjournals/joss/blob/main/docs/logos/joss-logo.png?raw=true" />
</a>

```bash
@article{Auriau2024,
  doi = {10.21105/joss.06899},
  url = {https://doi.org/10.21105/joss.06899},
  year = {2024},
  publisher = {The Open Journal},
  volume = {9},
  number = {101},
  pages = {6899},
  author = {Vincent Auriau and Ali Aouad and Antoine Désir and Emmanuel Malherbe},
  title = {Choice-Learn: Large-scale choice modeling for operational contexts through the lens of machine learning},
  journal = {Journal of Open Source Software} }
```

<p align="center">
  <a href="https://www.artefact.com/data-consulting-transformation/artefact-research-center/">
    <img src="https://raw.githubusercontent.com/artefactory/alea-carta-est/main/doc/logo_arc.png" height="60" />
  </a>
  &emsp;
  &emsp;
  <a href="https://mics.centralesupelec.fr/">
    <img src="https://raw.githubusercontent.com/artefactory/alea-carta-est/main/doc/logo_CS.png" height="65" />
  </a>
  &emsp;
  &emsp;
  <a href="https://www.universite-paris-saclay.fr/">
    <img src="https://raw.githubusercontent.com/artefactory/alea-carta-est/main/doc/logo_paris_saclay.png" height="65" />
  </a>
  <a href="https://fortenova.hr/en/home/">
    <img src="https://raw.githubusercontent.com/artefactory/alea-carta-est/main/doc/fortenova.png" height="65" />
  </a>
  &emsp;
  &emsp;
</p>


## License
The use of this software is under the MIT license, with no limitation of usage, including for commercial applications.
