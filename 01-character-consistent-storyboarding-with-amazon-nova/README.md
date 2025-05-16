# Character Consistent Storyboarding with Amazon Nova - Part 1

This directory contains code and resources for the first part of our blog series on building character-consistent storyboards using Amazon Nova on Amazon Bedrock.

## Introduction

The art of storyboarding has long been the backbone of content production, serving as a critical visualization tool across filmmaking, animation, advertising, and UX design. As creators craft sequential illustrations to map out their narratives, generative AI serves as a powerful assistant. Foundation models like Amazon Nova Canvas and Amazon Nova Reel offer capabilities in transforming text and image inputs into professional-grade images, as well as short clips poised to revolutionize the pre-production process.

While these models can generate concepts en masse, which is great for creative exploration, achieving consistent character designs and maintaining stylistic coherence across scenes remains a challenge. Even minor adjustments to prompts or configurations can result in dramatically different visual outputs, making it difficult to maintain narrative continuity.

In this first part, we dive into prompt engineering and character development pipelines, demonstrating how to establish reliable prompt patterns that yield consistent results using Amazon Nova Canvas and Reel models.

## Contents

- `storybook_demo.ipynb`: Original notebook for character-consistent storyboarding
- `storybook_demo_with_instructions.ipynb`: Enhanced notebook with detailed instructions and explanations
- `helpers/`: Directory containing utility functions and helper scripts:
  - `bedrock_helpers.py`: Functions for interacting with Amazon Bedrock
  - `display_helpers.py`: Functions for visualizing storyboards and results
  - `prompt_helpers.py`: Templates and functions for creating effective prompts
- `requirements.txt`: Python dependencies required for the project (boto3)

## Prerequisites

- AWS account with access to Amazon Bedrock
- Appropriate IAM permissions for Bedrock, S3, and related services
- Python 3.x environment

## Installation

1. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Configure your AWS credentials with appropriate permissions for Amazon Bedrock.

## Usage

1. Open and run either notebook:
   ```
   jupyter notebook storybook_demo_with_instructions.ipynb
   ```
   or
   ```
   jupyter notebook storybook_demo.ipynb
   ```

2. Follow the step-by-step instructions in the notebook to:
   - Define your story parameters (genre, idea, scene count)
   - Generate a structured story with consistent characters
   - Create detailed image prompts for each scene
   - Generate consistent storyboard frames using Amazon Nova Canvas
   - Visualize your complete storyboard

## Key Techniques Covered

- **Character Definition**: Methods to establish clear character attributes and visual identities
- **Prompt Engineering**: Strategies for crafting prompts that maintain consistency
- **Style Consistency**: Approaches to maintain artistic style across multiple frames
- **Scene Transitions**: Techniques for creating coherent visual narratives

## Prompt Engineering for Character Consistency

The notebook demonstrates several key techniques for maintaining character consistency:

1. **Detailed Character Descriptions**: Creating comprehensive descriptions that are reused across scenes
2. **Style Presets**: Using consistent style parameters for all generated images
3. **Seed Control**: Using the same random seed for all image generations
4. **Negative Prompts**: Specifying elements to avoid in the generated images

## Next Steps

After exploring the prompt engineering approach in this part, check out Part 2 in the `02-character-consistent-fine-tuning-with-amazon-nova-canvas` directory to learn about fine-tuning Amazon Nova Canvas for even greater character consistency.

## Security

See [CONTRIBUTING](../CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.
