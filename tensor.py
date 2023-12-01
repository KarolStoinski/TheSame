import json
import os

# Directory containing your JSON files
embedding_dir = 'embeddings'
tensor_dir = 'tensor'
splitted_dir = 'splitted'

for filename in os.listdir(embedding_dir):
    # Path to your JSON file
    json_path = os.path.join(embedding_dir, filename)
    splited_path = os.path.join(splitted_dir, filename)

    # Create vectors.tsv and metadata.tsv
    vectors_path = os.path.join(tensor_dir, 'vectors.tsv')
    metadata_path = os.path.join(tensor_dir, 'metadata.tsv')

    with open(json_path, 'r') as json_file, open(splited_path, 'r', encoding='utf-8') as splited_file:
        data = json.load(json_file)

        with open(vectors_path, 'a') as vectors_file, open(metadata_path, 'a') as metadata_file:
            # Write the embedding vector
            vectors_file.write('\t'.join([str(x) for x in data]) + '\n')
            
            # Write the metadata (label, identifier, etc.)
            metadata_file.write(splited_file.read().replace('\n', ' ') + '\n')