# acoustic_classifier_seaturtles

# Environment Setup

We use Conda to manage the project environment.

## 1. Create the Shared Environment

Clone the repository and create the environment from the provided file:

```bash
conda env create -f environment.yml
```

Activate the environment:

```bash
conda activate acoustic-ST
```

---

# PyTorch Installation

PyTorch must be installed separately depending on whether your machine supports GPU acceleration or not.

## Option 1 — GPU (CUDA)

Install the GPU version of PyTorch.

### Using pip

```bash
pip install torch --index-url https://download.pytorch.org/whl/cu121
```

> Make sure the CUDA version matches your local CUDA installation.

---

## Option 2 — CPU Only

Install the CPU version of PyTorch.

### Using pip

```bash
pip install torch 
```

---

# Verify Installation

Run the following command to verify the installation:

```python
import torch

print("PyTorch version:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())
```

---

# Device Configuration

The code automatically detects whether CUDA is available:

```python
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print("Using device:", device)
```

# Updating the Environment

If new dependencies are added, update the shared environment file with:

```bash
conda env export --from-history > environment.yml
```

> **Note:** PyTorch is intentionally excluded from the shared environment file to avoid GPU/CPU compatibility issues across different machines.

