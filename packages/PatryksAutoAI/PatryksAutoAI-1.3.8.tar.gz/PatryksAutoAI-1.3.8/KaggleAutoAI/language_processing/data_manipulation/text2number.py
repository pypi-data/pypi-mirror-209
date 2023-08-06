from transformers import BertTokenizer, GPT2Tokenizer, RobertaTokenizer, DistilBertTokenizer, AlbertTokenizer, ElectraTokenizer
import numpy as np
import tensorflow as tf

class Text2Number():
    def __init__(self, batch_size=32):
        self.token = None
        self.batch_size = batch_size

    def tokenize_bert(self, data, seq_len=128, model="bert-base-cased"):
        '''
            Computationally expensive due to their large size, and the tokenization process can be slower
        '''
        tokenizer = BertTokenizer.from_pretrained(model)
        token = tokenizer(data.tolist(),
                          max_length=seq_len,
                          truncation=True,
                          padding='max_length',
                          add_special_tokens=True,
                          return_tensors="tf")
        self.token = token

    def tokenize_gpt2(self, data, seq_len=128, model="gpt2-medium"):
        '''
            Unidirectional
        '''
        tokenizer = GPT2Tokenizer.from_pretrained(model)
        token = tokenizer(data.tolist(),
                          max_length=seq_len,
                          truncation=True,
                          padding='max_length',
                          add_special_tokens=True,
                          return_tensors="tf")
        self.token = token

    def tokenize_robert(self, data, seq_len=128, model="roberta-base"):
        '''
            Requiring more computational resources for training and inference.
        '''
        tokenizer = RobertaTokenizer.from_pretrained(model)
        token = tokenizer(data.tolist(),
                          max_length=seq_len,
                          truncation=True,
                          padding='max_length',
                          add_special_tokens=True,
                          return_tensors="tf")
        self.token = token

    def tokenize_distilBERT(self, data, seq_len=128, model="distilbert-base-uncased"):
        '''
            Scenarios where memory and computational resources are limited
        '''
        tokenizer = DistilBertTokenizer.from_pretrained(model)
        token = tokenizer(data.tolist(),
                          max_length=seq_len,
                          truncation=True,
                          padding='max_length',
                          add_special_tokens=True,
                          return_tensors="tf")
        self.token = token

    def tokenize_Albert(self, data, seq_len=128, model="albert-base-v2"):
        '''
            Fewer parameters, making them more memory-efficient and faster during training and inference
        '''
        tokenizer = AlbertTokenizer.from_pretrained(model)
        token = tokenizer(data.tolist(),
                          max_length=seq_len,
                          truncation=True,
                          padding='max_length',
                          add_special_tokens=True,
                          return_tensors="tf")
        self.token = token

    def tokenize_Electra(self, data, seq_len=128, model="google/electra-base-discriminator"):
        '''
            Rely on a discriminator-generator setup, which means they may not capture certain aspects of language semantics
        '''
        tokenizer = ElectraTokenizer.from_pretrained(model)
        token = tokenizer(data.tolist(),
                          max_length=seq_len,
                          truncation=True,
                          padding='max_length',
                          add_special_tokens=True,
                          return_tensors="tf")
        self.token = token

    def train_val_test(self, labels, train_size=0.8, val_size=0.1):
        '''
            Creates the train and validation datasets
        '''
        labels = np.array(labels.tolist()).reshape(-1,1)
        size = int(labels.shape[0] / self.batch_size * train_size)
        size_val = int(labels.shape[0] / self.batch_size * val_size)

        dataset = tf.data.Dataset.from_tensor_slices((self.token['input_ids'], self.token['attention_mask'], labels))
        dataset = dataset.map(self.map_func)
        dataset = dataset.shuffle(10000).batch(self.batch_size,drop_remainder=True)

        train_ds = dataset.take(size)
        data = dataset.skip(size)
        val_ds = data.take(size_val)
        test_ds = data.skip(size_val)
        return train_ds, val_ds, test_ds
    
    def test(self, labels):
        labels = np.array(labels.tolist()).reshape(-1,1)
        dataset = tf.data.Dataset.from_tensor_slices((self.token['input_ids'], self.token['attention_mask']))
        dataset = dataset.map(self.map_func)
        return dataset, labels
    
    def map_func_test(self, input_ids, masks):
        return {'input_ids':input_ids,
                'attention_mask':masks}
    
    def map_func(self, input_ids, masks, labels):
        return {'input_ids':input_ids,
                'attention_mask':masks}, labels
    
    def get(self):
        return self.token
    