<h1 align="center">Inshorts News Headline Generation using BART</h1>

<div align="center">

[![Language](https://img.shields.io/badge/Python-darkblue.svg?style=flat&logo=python&logoColor=white)](https://www.python.org) 
[![Framework](https://img.shields.io/badge/PyTorch-red.svg?style=flat&logo=pytorch&logoColor=white)](https://pytorch.org/) 
[![Model](https://img.shields.io/badge/BART-lightgreen.svg?style=flat)](https://arxiv.org/abs/1910.13461) 
[![Transformer](https://img.shields.io/badge/Transformers-yellow.svg?style=flat)](https://arxiv.org/abs/1706.03762) 
[![Repo Size](https://img.shields.io/github/repo-size/Oyebamiji-Micheal/Inshorts-News-Headline-Generation-using-BART)](https://github.com/Oyebamiji-Micheal/Inshorts-News-Headline-Generation-using-BART) 
[![Topic](https://img.shields.io/badge/Text%20Summarization-lightblue.svg?style=flat)]() 
[![License](https://img.shields.io/github/license/Oyebamiji-Micheal/Inshorts-News-Headline-Generation-using-BART)](https://github.com/Oyebamiji-Micheal/Inshorts-News-Headline-Generation-using-BART/blob/main/LICENSE) 

</div>

<h4 align="center">Text Summarization: Fine-tuning BART-Large model to generate concise news headlines</h4>

<br/>

<img src="images/repo-cover.jpg">
<p>Image Credit: Abhinav Garg</p>

You can view the live project <a href="https://inshorts-news-summariser.streamlit.app/">here</a>

<h2>Table of Contents</h2>

- [Overview](#overview)
- [Dataset](#dataset)
- [Model](#model)
- [Result](#result)

<a id="overview"></a>
<h2>Overview</h2>
<p align="justify">
This project involves fine-tuning the BART (Bidirectional and Auto-Regressive Transformers) model for the task of generating headlines for news articles. This is actually the same as a summarization task, where the model is trained to generate a concise summary of the news article. BART is a denoising autoencoder that maps a document to a document in a self-supervised way. It is trained by corrupting text with an arbitrary noising function, and then learning to reconstruct the original text - <a href="https://arxiv.org/abs/1910.13461">Lewis et al., 2019</a> 
</p>

<a id="dataset"></a>
<h2>Dataset</h2>
<p align="justify">
The dataset used for this project is available on <a href="https://www.kaggle.com/datasets/shivamtaneja2304/inshorts-dataset-english/versions/147">Kaggle</a> and contains 307,696 rows of news articles and their respective headlines. To optimize training time, I used a subset of 10,000 samples from the dataset for fine-tuning. The dataset comprises text articles and their corresponding concise headlines, making it suitable for a summarization task. Each row represents a pair of input text and output headline.
</p>

<a id="model"></a>
<h2>Model</h2>
<p align="justify">
The <a href="https://arxiv.org/abs/1910.13461">BART</a> model architecture, developed by Facebook, combines bidirectional and auto-regressive transformers. It is particularly effective for text generation and summarization tasks. The model was fine-tuned using the Hugging Face Transformers library with the following hyperparameters: </p>

- Batch Size: 32
- Learning Rate: 5.6e-5
- Epochs: 10

<a id="result"></a>
<h2>Result</h2>
<p align="justify">
The fine-tuned model was evaluated based on ROUGE metrics. The table below shows the training and validation loss, as well as the ROUGE-1, ROUGE-2, ROUGE-L, and ROUGE-Lsum scores for each epoch. </p>

| Epoch | Training Loss | Validation Loss | Rouge1 | Rouge2 | Rougel | Rougelsum |
|-------|---------------|-----------------|--------|--------|--------|-----------|
| 1     | 2.079600      | 1.652206        | 0.4837 | 0.2736 | 0.4424 | 0.4428    |
| 2     | 1.569100      | 1.567577        | 0.5168 | 0.3068 | 0.4755 | 0.4759    |
| 3     | 1.265400      | 1.531981        | 0.5267 | 0.3242 | 0.4859 | 0.4851    |
| 4     | 1.045300      | 1.567422        | 0.5404 | 0.3374 | 0.4988 | 0.4987    |
| 5     | 0.878600      | 1.591885        | 0.5431 | 0.3514 | 0.5046 | 0.5049    |
| 6     | 0.741100      | 1.589573        | 0.5519 | 0.3607 | 0.5146 | 0.5139    |
| 7     | 0.645300      | 1.657856        | 0.5563 | 0.3704 | 0.5197 | 0.5198    |
| 8     | 0.565900      | 1.648749        | 0.5612 | 0.3776 | 0.5247 | 0.5245    |
| 9     | 0.506600      | 1.661315        | 0.5694 | 0.3844 | 0.5322 | 0.5311    |
| 10    | 0.469300      | 1.676505        | 0.5686 | 0.3861 | 0.5329 | 0.5322    |

Here is an example of the model's output on unseen data:

```
Slim PlayStation triples sales..Sony PlayStation 2's slimmer shape has proved popular with UK gamers, with 50,000 sold in its first week on sale...Sales have tripled since launch, outstripping Microsoft's Xbox, said market analysts Chart-Track. The numbers were also boosted by the release of the PS2-only game Grand Theft Auto: San Andreas. The title broke the UK sales record for video games in its first weekend of release. Latest figures suggest it has sold more than 677,000 copies..."It is obviously very, very encouraging for Sony because Microsoft briefly outsold them last week," John Houlihan, editor of Computerandvideogames.com told BBC News. "And with Halo 2 [for Xbox] out next week, it really is a head-to-head contest between them and Xbox."..Although Xbox sales over the last week also climbed, PS2 sales were more than double that. The figures mean Sony is reaching the seven million barrier for UK sales of the console. Edinburgh-based developer, Rockstar, which is behind the GTA titles, has seen San Andreas pull in an estimated £24m in gross revenues over the weekend. In comparison, blockbuster films like Harry Potter and The Prisoner Of Azkaban took £11.5m in its first three days at the UK box office. The Lord of the Rings: The Return of the King took nearly £10m over its opening weekend, although games titles are four to five times more expensive than cinema tickets...Gangster-themed GTA San Andreas is the sequel to Grand Theft Auto Vice City which previously held the record for the fastest-selling video game ever. The Xbox game Halo 2, released on 11 November in the UK, is also widely tipped to be one of the best-selling games of the year. The original title won universal acclaim in 2001, and sold more than four million copies...Mr Houlihan added that Sony had done well with the PS2, but it definitely helped that the release of San Andreas coincided with the slimline PS2 hitting the shelves. The run-up to Christmas is a huge battlefield for games consoles and titles. Microsoft's Xbox had been winning the race up until last week in sales. The sales figures also suggest that it may be a largely adult audience driving demand, since GTA San Andreas has an 18 certificate. Sony and Microsoft have both reduced console prices recently and are preparing the way for the launches of their next generation consoles in 2005. "Both have hit crucial price points at around £100 and that really does open up new consoles to new audience, plus the release of two really important games in terms of development are also driving those sales," said Mr Houlihan.</p>
```

Original BART Summary:

```
Slim PlayStation triples sales..Sony PlayStation 2's slimmer shape has proved popular with UK gamers, with 50,000 sold in its first week on sale... (Image: Sony)Sales have tripled since launch, outstripping
```

Fine-tuned BART Summary:

```
Slim PlayStation triples sales in UK, Microsoft's 'Xbox One' rival hits 7 million sales mark: Report
```

Everything you need to know about the project is in the [notebook](https://github.com/Oyebamiji-Micheal/Inshorts-News-Headline-Generation-using-BART/blob/main/headline-generation-by-fine-tuning-bart.ipynb).