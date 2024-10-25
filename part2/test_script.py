# test_script.py
import torch
from transformers import AutoModel, AutoTokenizer

# Check if CUDA is available
if torch.cuda.is_available():
    print(f"CUDA is available. Using GPU: {torch.cuda.get_device_name(0)}")
else:
    print("CUDA is not available. Using CPU.")

# Test loading a Hugging Face model on GPU
model_name = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# Move the model to GPU (if available)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Perform a forward pass with dummy input
inputs = tokenizer("This is a test sentence.", return_tensors="pt").to(device)
outputs = model(**inputs)
print("Model output:", outputs.last_hidden_state)
