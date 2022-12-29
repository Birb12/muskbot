from datasetmanager import MuskDataset
import os
import time
import datetime

import pandas as pd
import seaborn as sns
import numpy as np
import random

import matplotlib.pyplot as plt

import torch
from torch.utils.data import Dataset, DataLoader, random_split, RandomSampler, SequentialSampler
torch.manual_seed(42)

from transformers import GPT2LMHeadModel,  GPT2Tokenizer, GPT2Config, GPT2LMHeadModel
from transformers import AdamW, get_linear_schedule_with_warmup


def generate_tweet():
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2', bos_token='<|startoftext|>', eos_token='<|endoftext|>', pad_token='<|pad|>') 
    configuration = GPT2Config.from_pretrained('musk_modelamazing', output_hidden_states=False) # pretrained directory in my local machine, no you're not getting it, YOUR money didnt pay for the cloud service

    model = GPT2LMHeadModel.from_pretrained("musk_modelamazing", config=configuration)

    model.resize_token_embeddings(len(tokenizer))

    device = torch.device("cpu")
    model.to("cpu")

    seed_val = random.randint(0, 50000000) # reproducibility? whats that?

    random.seed(seed_val)
    np.random.seed(seed_val)
    torch.manual_seed(seed_val)
    torch.cuda.manual_seed_all(seed_val)


    sample_outputs = model.generate(
                                        bos_token_id=random.randint(1,30000),
                                        do_sample=True,   
                                        top_k=50, 
                                        max_length = 200,
                                        top_p=0.95, 
                                        num_return_sequences=1
                                    )
    for i, sample_output in enumerate(sample_outputs):
        return tokenizer.decode(sample_output, skip_special_tokens=True)

def pretty_tweet(tweet): # for some reason, the model always outputs some random word (big, eject) before the actual tweet starts, this is probably my fault by messing up the loading of the data, but im not paying for more cloud processing time
    if '@' in tweet:
        while (tweet[0] != '@'):
            tweet = tweet[1:]
        return tweet
        

