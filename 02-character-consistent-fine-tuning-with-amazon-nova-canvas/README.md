# Character Consistent Storyboarding with Amazon Nova Canvas Fine-tuning - Part 2

This directory contains code and resources for the second part of our blog series on building character-consistent storyboards using Amazon Nova on Amazon Bedrock.

## Introduction

Building on the prompt engineering and character development approach covered in Part 1 of this two-part blog series, we now push the consistency level for specific characters by fine-tuning an Amazon Nova Canvas foundation model. While careful prompt crafting can yield good results, achieving professional-grade visual consistency often requires adapting the underlying model itself. Through character-compliant fine-tuning of Amazon Nova Canvas, creators can "teach" the model to maintain precise control over character appearances, expressions, and stylistic elements across multiple scenes.

In this part, we take an animated short film, Picchu, produced by FuzzyPixel from Amazon Web Services (AWS), prepare training data by extracting key character frames, and fine-tune a character-consistent model for the main character Mayu and her mom, enabling quick generation of storyboard concepts for new sequels.

## Contents

- `picchu-finetuning.ipynb`: Jupyter notebook containing the complete fine-tuning workflow
- `image_processing.py`: Helper functions for image processing and S3 operations
- `requirements.txt`: Python dependencies required for the project

## Prerequisites

- AWS account with access to Amazon Bedrock
- Appropriate IAM permissions for Bedrock, S3, and related services
- Python 3.x environment
- Access to Amazon Bedrock model fine-tuning capabilities

## Installation

1. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Configure your AWS credentials with appropriate permissions for Amazon Bedrock.

## Usage

1. Open and run the `picchu-finetuning.ipynb` notebook:
   ```
   jupyter notebook picchu-finetuning.ipynb
   ```

2. Follow the step-by-step instructions in the notebook to:
   - Prepare your training data from the Picchu animated short film
   - Upload images to S3
   - Configure and start the fine-tuning job
   - Generate and evaluate images with your fine-tuned model

**Note**: The notebook should be run in the `us-east-1` AWS region for compatibility with Bedrock services.

## Key Techniques Covered

- **Training Data Preparation**: Methods to extract and prepare character frames for fine-tuning
- **Fine-tuning Configuration**: Setting up the fine-tuning job with appropriate parameters
- **Character-Consistent Generation**: Using the fine-tuned model to create consistent storyboards
- **Evaluation and Iteration**: Assessing results and refining the fine-tuning process

## Fine-tuning Process Overview

1. **Data Collection**: Extract frames featuring the target characters from the Picchu animated short
2. **Data Preparation**: Process images and create training manifests
3. **Fine-tuning Job**: Configure and execute the fine-tuning job on Amazon Bedrock
4. **Model Evaluation**: Test the fine-tuned model with various prompts
5. **Storyboard Generation**: Create consistent storyboard sequences with the fine-tuned model

## Security

See [CONTRIBUTING](../CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.
