# Character Consistent Storyboarding with Amazon Nova on Amazon Bedrock

This repository contains code and resources for a two-part blog series on building character-consistent storyboards using Amazon Nova on Amazon Bedrock.

## Project Overview

The art of storyboarding is essential in content production across filmmaking, animation, advertising, and UX design. This project demonstrates how to leverage Amazon Nova Canvas and Amazon Nova Reel to create character-consistent storyboards, addressing one of the key challenges in AI-generated visual content: maintaining visual consistency across multiple scenes.

## Blog Series

### Part 1: Prompt Engineering and Character Development

In the first part, we explore prompt engineering techniques and character development pipelines to establish reliable prompt patterns that yield consistent results using Amazon Nova Canvas and Reel models.

Key components:
- Prompt engineering strategies for character consistency
- Character development workflows
- Practical examples using Amazon Nova Canvas and Reel

### Part 2: Character-Compliant Fine-Tuning

The second part focuses on advanced techniques, specifically fine-tuning the Amazon Nova Canvas model to achieve exceptional visual consistency and character control.

Key components:
- Preparing training data from the animated short film "Picchu"
- Fine-tuning Amazon Nova Canvas for specific characters (Mayu and her mom)
- Generating storyboard concepts with the fine-tuned model

## Repository Structure

- `01-character-consistent-storyboarding-with-amazon-nova/`: Code and resources for Part 1
- `02-character-consistent-fine-tuning-with-amazon-nova-canvas/`: Code and resources for Part 2

## Prerequisites

- AWS account with access to Amazon Bedrock
- Appropriate IAM permissions for Bedrock, S3, and related services
- Python environment with required dependencies

## Getting Started

1. Clone this repository
2. Navigate to either part 1 or part 2 directory
3. Install the required dependencies for the respective part
4. Follow the instructions in the notebooks to explore each approach

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

## Contributing

We welcome contributions! Please see the [CONTRIBUTING](CONTRIBUTING.md) file for how to contribute.

## Additional Resources

- [Amazon Bedrock Documentation](https://docs.aws.amazon.com/bedrock/)
- [Amazon Nova Canvas Documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-nova-canvas.html)
- [Amazon Nova Reel Documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-nova-reel.html)
