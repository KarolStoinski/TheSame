import tensorflow as tf
import numpy as np
import os
from tensorboard.plugins import projector

# Load your vectors and metadata
vectors = np.loadtxt('tensor/vectors.tsv', delimiter='\t')
metadata = np.loadtxt('tensor/metadata.tsv', dtype=str)

# Create a logs directory
log_dir = 'logs'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Create a TensorFlow variable for the vectors
embeddings = tf.Variable(vectors, name='embeddings')

# Save the embeddings in the log directory
checkpoint = tf.train.Checkpoint(embedding=embeddings)
checkpoint_prefix = os.path.join(log_dir, "embeddings.ckpt")
checkpoint.save(checkpoint_prefix)

# Set up the config for TensorBoard
config = projector.ProjectorConfig()
embedding = config.embeddings.add()
embedding.tensor_name = "embedding/.ATTRIBUTES/VARIABLE_VALUE"
embedding.metadata_path = 'metadata.tsv' # Ensure this is the correct path to your metadata file

# Save the projector config
projector.visualize_embeddings(log_dir, config)

