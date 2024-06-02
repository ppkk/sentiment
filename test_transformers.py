from transformers import BertTokenizer, BertModel
import torch

# Load pre-trained BERT tokenizer and model
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

# Tokenize input
inputs = tokenizer("Hello, my dog is cute", return_tensors="pt")

# Get model output
outputs = model(**inputs)

print(outputs.last_hidden_state)
