# Reward Debug Repository

This repository contains analysis tools and data for debugging reinforcement learning reward functions, specifically focused on AWS DeepRacer model training.

## Contents

### 📊 Analysis Notebook
- **`JimmyModelv4clone3_Analysis.ipynb`** - Jupyter notebook for analyzing training logs from reinforcement learning models
  - Loads and analyzes training log data from compressed archives
  - Provides data structure analysis and visualization tools
  - Designed for AWS DeepRacer autonomous driving model debugging

### 📁 Training Data
- **`JimmyModelv4clone3_traininglog.tar.gz`** - Compressed training log archive (908KB)
  - Contains reinforcement learning training logs
  - Used for reward function analysis and model performance debugging

## Getting Started

1. **Extract Training Logs**
   ```bash
   tar -xzf JimmyModelv4clone3_traininglog.tar.gz
   ```

2. **Run Analysis**
   ```bash
   jupyter notebook JimmyModelv4clone3_Analysis.ipynb
   ```

## Requirements

- Python 3.x
- Jupyter Notebook
- Required Python packages:
  - pandas
  - numpy
  - matplotlib
  - csv
  - tarfile

## Purpose

This repository is designed for:
- **Reward Function Debugging** - Analyze and debug reinforcement learning reward functions
- **Training Log Analysis** - Visualize and understand model training progress
- **AWS DeepRacer Development** - Specific tools for autonomous driving model development
- **Performance Optimization** - Identify areas for model improvement

## Usage

The main analysis workflow:
1. Load training logs using the Jupyter notebook
2. Analyze reward patterns and training progress
3. Debug issues with reward function design
4. Optimize model performance based on insights

## Notes

- Training logs are from JimmyModelv4clone3, suggesting this is version 4 of an iterative development process
- The repository focuses on reward debugging, indicating challenges with reward function tuning
- Tools are specifically tailored for reinforcement learning in autonomous driving contexts
- Sensitive configuration files are excluded for security reasons

## Security

This repository excludes sensitive files such as API keys and authentication tokens. If you need to set up the full environment, create your own configuration files locally.

---

*This repository is part of an ongoing reinforcement learning project focused on reward function optimization and debugging.*
