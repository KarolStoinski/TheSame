import os
import torch.nn.functional as F
import json

from torch import Tensor
from transformers import AutoTokenizer, AutoModel


def average_pool(last_hidden_states: Tensor,
                 attention_mask: Tensor) -> Tensor:
    last_hidden = last_hidden_states.masked_fill(~attention_mask[..., None].bool(), 0.0)
    return last_hidden.sum(dim=1) / attention_mask.sum(dim=1)[..., None]


# Each input text should start with "query: " or "passage: ", even for non-English texts.
# For tasks other than retrieval, you can simply use the "query: " prefix.

tokenizer = AutoTokenizer.from_pretrained('intfloat/multilingual-e5-large')
model = AutoModel.from_pretrained('intfloat/multilingual-e5-large')

# Specify the directory containing the split files
directory = 'splitted'

# List all files in the directory
for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)
    
    # Check if it's a file and not a directory
    if os.path.isfile(filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                input_texts = ['passage: ' + file.read()]

                # Tokenize the input texts
                batch_dict = tokenizer(input_texts, max_length=512, padding=True, truncation=True, return_tensors='pt')

                outputs = model(**batch_dict)
                embeddings = average_pool(outputs.last_hidden_state, batch_dict['attention_mask'])

                # normalize embeddings
                embeddings = F.normalize(embeddings, p=2, dim=1)

                # Convert to list
                embeddings_list = embeddings.tolist()[0]

                # Save as JSON
                with open('embeddings/' + filename, 'w') as f:
                    json.dump(embeddings_list, f)

        except IOError as e:
            print(f"Error reading file {filename}: {e}")