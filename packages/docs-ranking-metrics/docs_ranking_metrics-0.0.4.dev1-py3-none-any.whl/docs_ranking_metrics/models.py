import tensorflow_hub as hub
from tensorflow_text import SentencepieceTokenizer
import tensorflow as tf

class ModelUSE():
    def __init__(self):
        # Ограничение потребляемой памяти моделью
        gpus = tf.config.experimental.list_physical_devices('GPU')
        tf.config.experimental.set_virtual_device_configuration(gpus[0],
                                                                [tf.config.experimental.VirtualDeviceConfiguration(
                                                                    memory_limit=1024)])
        self.model = hub.load("https://tfhub.dev/google/universal-sentence-encoder-multilingual-large/3")

    def encode(self, sentences, batch_size=32, **kwargs):
        embeddings = []
        for i in range(0, len(sentences), batch_size):
            batch_sentences = sentences[i:i+batch_size]
            batch_embeddings = self.model(batch_sentences)
            embeddings.extend(batch_embeddings)
        return embeddings