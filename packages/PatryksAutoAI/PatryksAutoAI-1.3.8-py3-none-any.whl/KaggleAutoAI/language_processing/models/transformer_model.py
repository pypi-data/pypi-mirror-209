import tensorflow as tf
from sklearn.metrics import log_loss
import optuna.visualization as vis
from ...classification.metrics import Metrics
from transformers import TFAutoModel
import optuna
import numpy as np
optuna.logging.disable_default_handler()

class TransformerModel(Metrics):
    def __init__(self, num_classes, seq_len=128, bert_model_name='bert-base-uncased'):
        self.classes = num_classes
        self.bert_model = TFAutoModel.from_pretrained(bert_model_name)
        self.layers = []
        self.seq_len = seq_len
        self.model

    def add_dense(self, dimensions=128, activation="relu"):
        self.layers.append(tf.keras.layers.Dense(dimensions, activation=activation))

    def build(self):
        inputs_ids = tf.keras.Input(shape=(self.seq_len, ), dtype=tf.int32)
        attention_mask = tf.keras.Input(shape=(self.seq_len, ), dtype=tf.int32)

        outputs = self.bert_model(self.input_ids, attention_mask=self.mask)
        x = outputs.last_hidden_state
        for layer in self.layers:
            x = layer(x)
        if self.classes < 2:
            y = tf.keras.layers.Dense(self.classes, activation='sigmoid')(x)
        else:
            y = tf.keras.layers.Dense(self.classes, activation='softmax')(x)

        self.model = tf.keras.Model(inputs=[inputs_ids, attention_mask], outputs=y)

    def compile(self, compiler):
        self.model.compile(**compiler)
    
    def fit(self, data_train, data_val, epochs=1):
        self.model.fit(data_train, validation_data=data_val, epochs=epochs)

    def predict(self, data):
        predictions = []
        for val in data:
            print(val)
            pred = self.model.predict(val)
            predictions.append(pred)
        return predictions





    