# Code Review Automation with Language Models

[![Static Badge](https://img.shields.io/badge/jupyter-book-orange?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAZCAMAAAAVHr4VAAAAXVBMVEX////v7+/zdybv7+/zdybv7+/zdybv7+/zdybv7+/zdybv7+/zdybv7+/zdybv7+/zdybv7+/zdybv7+/v7+/zdybv7+/zdybv7+/v7+/zdybv7+/zdybv7+/zdyaSmqV2AAAAHXRSTlMAEBAgIDAwQEBQUGBgcHCAgJCQoLCwwMDQ4ODw8MDkUIUAAADJSURBVHjaddAFkgNBCAXQP+7uAvc/5tLFVseYF8crUB0560r/5gwvjYYm8gq8QJoyIJNwlnUH0WEnART6YSezV6c5tjOTaoKdfGXtnclFlEBEXVd8JzG4pa/LDql9Jff/ZCC/h2zSqF5bzf4vqkgNwEzeClUd8uMadLE6OnhBFsES5niQh2BOYUqZsfGdmrmbN+TMvPROHUOkde8sEs6Bnr0tDDf2Roj6fmVfubuGyttejCeLc+xFm+NLuLnJeFAyl3gS932MF/wBoukfUcwI05kAAAAASUVORK5CYII=&style=for-the-badge)](https://alexkovrigin.me/Code-Review-Automation-LM)

![CodeReviewer Overview](https://alexkovrigin.me/data/Screenshot%202023-09-17%20121440.png)

## Overview

Code review is a crucial aspect of the software development process, ensuring that code changes are thoroughly examined
for quality, security, and adherence to coding standards. However, the code review process can be time-consuming, and
human reviewers may overlook certain issues.

In this series of Jupyter notebooks, we embark on a journey to collect code review data from GitHub repositories and
perform code review predictions using a prominent language model: [CodeReviewer](https://arxiv.org/abs/2203.09095) from
Microsoft Research. Our primary goal is to explore the capabilities of this model in generating code reviews and
evaluate its performance.

## Contents

### 1. Data Collection

First, we collect the code review data from popular GitHub repositories. This data includes code changes and associated
human-authored code reviews. By leveraging this data, the model learns to generate contextually relevant code reviews.

### 2. Model Inference and Fine-Tuning

We take the pre-trained language checkpoint and fine-tune the model on code review datasets. Fine-tuning allows the models to
specialize in generating code reviews, making them more effective in this task.

Once the models are trained, they can generate code reviews for new code changes. These generated reviews can highlight
potential issues, suggest improvements, and provide feedback to developers.

### 3. Evaluation Metrics

We use the BLEU-4 score metric to assess the quality of generated code reviews. This metric measures the similarity
between model-generated reviews and target human reviews.

## Getting Started

To get started with our work, follow these steps:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/waleko/Code-Review-Automation-LM.git
   cd Code-Review-Automation-LM
   ```

2. Set up the required dependencies from `requirements.txt`. E.g.: using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the provided notebooks to explore data collection, model inference, and evaluation.

## Acknowledgements
Incredible thanks to the authors of [CodeReviewer](https://arxiv.org/abs/2203.09095) for their scientific contributions.
This work is basically an in-depth exploration of their research, and I am grateful for their efforts.

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or inquiries, please contact [inbox@alexkovrigin.me](mailto:inbox@alexkovrigin.me).
