# Code Review Automation with Language Models

## Introduction

In this series of Jupyter notebooks, we embark on a journey to collect code review data from GitHub repositories and
perform code review predictions using language models. Our primary goal is to explore the capabilities of the [CodeReviewer](https://arxiv.org/abs/2203.09095) model in generating code reviews and evaluate its performance.

![CodeReviewer Overview](https://alexkovrigin.me/data/Screenshot%202023-09-17%20121440.png)

### Collecting Code Review Data

In this initial notebook, we dive into the process of collecting code review data from GitHub repositories. We leverage
the PyGithub library to interact with the GitHub API, ensuring seamless data retrieval.

Three prominent repositories, namely `microsoft/vscode`, `JetBrains/kotlin`, and `transloadit/uppy`, are selected for
data collection due to their popularity and rich code review history. Additionally, we are going to use data from the
original CodeReviewer dataset `msg-test` that is provided by the authors of {cite}`li2022codereviewer`.

### CodeReviewer Model Inference

The second notebook focuses on generating code reviews using the `microsoft/codereviewer` model. We delve into the
tokenization and dataset preparation process, emphasizing the importance of specialized tokens.

We explore the model inference process, employing both a HuggingFace pre-trained checkpoint and a fine-tuned
CodeReviewer model. The fine-tuning process details are outlined, showcasing parameters and resources used. Model
predictions are saved.

### Predictions Evaluation

In this notebook, we assess the quality of code review predictions generated by the models. Both HuggingFace pre-trained and
fine-tuned models are evaluated across different datasets, shedding light on their performance.

Qualitative assessment is conducted to gain insights into how the models generate code reviews. We present samples of
code, along with predictions from both models, enabling a visual comparison with human reviews.

Lastly, we quantitatively evaluate the models' performance using BLEU-4 scores. We calculate scores for each dataset,
providing a comprehensive overview of how well the models align with human reviews.


## Acknowledgements
Incredible thanks to the authors of [CodeReviewer](https://arxiv.org/abs/2203.09095) for their scientific contributions.
This work is basically an in-depth exploration of their research, and I am grateful for their efforts.

## Table of Contents

```{tableofcontents}
```

## Bibliography

```{bibliography}
```