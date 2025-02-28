import os
from io import open
import torch
from transformers import GPT2Tokenizer

class Corpus(object):
    def __init__(self, path):
        self.tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
        self.train = None
        self.valid = None
        self.test = None
        if not self.load_cache(path):
            self.train = self.tokenize(os.path.join(path, 'train.txt'))
            self.valid = self.tokenize(os.path.join(path, 'valid.txt'))
            self.test = self.tokenize(os.path.join(path, 'test.txt'))
            self.save_cache(path)

    def load_cache(self, path):
        for cache in ['tokenizer.pt', 'train.pt', 'valid.pt', 'test.pt']:
            cache_path = os.path.join(path, cache)
            if not os.path.exists(cache_path):
                return False
        self.tokenizer = torch.load(os.path.join(path, 'tokenizer.pt'))
        self.train = torch.load(os.path.join(path, 'train.pt'))
        self.valid = torch.load(os.path.join(path, 'valid.pt'))
        self.test = torch.load(os.path.join(path, 'test.pt'))
        return True

    def save_cache(self, path):
        torch.save(self.tokenizer, os.path.join(path, 'tokenizer.pt'))
        torch.save(self.train, os.path.join(path, 'train.pt'))
        torch.save(self.valid, os.path.join(path, 'valid.pt'))
        torch.save(self.test, os.path.join(path, 'test.pt'))

    def tokenize(self, path):
        """Tokenizes a text file using GPT2Tokenizer."""
        assert os.path.exists(path)
        with open(path, 'r', encoding="utf8") as f:
            text = f.read()
        tokens = self.tokenizer.encode(text, add_special_tokens=True)
        return torch.tensor(tokens).type(torch.int64)
