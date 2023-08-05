"""
Modification of BurhanUlTayyab/GPTZero
Thanks to Burhan Ul tayyab and Nicholas Chua
"""

import torch
import re
from transformers import GPT2LMHeadModel, GPT2TokenizerFast
import time
from .exceptions import *


class Loader:
    def __init__(self, model, device):
        self.device = device
        self.model = model
        self.start_time = time.time()
        self.model = GPT2LMHeadModel.from_pretrained(model).to(device)
        self.tokenizer = GPT2TokenizerFast.from_pretrained(model)

        self.max_length = self.model.config.n_positions
        self.stride = 512
        
    def getResults(self, threshold):
        if threshold < 60:
            label = 0
            return {"output": "The text is likely to be written entirely by a AI.", "code": label}
        elif threshold < 80:
            label = 1
            return {"output": "The text is likely to be written by a combination of Human and AI.", "code":label}
        else:
            label = 2
            return {"output": "The text is likely to be written entirely by a Human.", "code": label}

    def getPPL(self, sentence):
        device = self.device
        encodings = self.tokenizer(sentence, return_tensors="pt").to(device)
        seq_len = encodings.input_ids.size(1)

        nlls = []
        likelihoods = []
        prev_end_loc = 0
        for begin_loc in range(0, seq_len, self.stride):
            end_loc = min(begin_loc + self.max_length, seq_len)
            trg_len = end_loc - prev_end_loc
            input_ids = encodings.input_ids[:, begin_loc:end_loc].to(self.device)
            target_ids = input_ids.clone()
            target_ids[:, :-trg_len] = -100

            with torch.no_grad():
                outputs = self.model(input_ids, labels=target_ids)
                neg_log_likelihood = outputs.loss * trg_len
                likelihoods.append(neg_log_likelihood)

            nlls.append(neg_log_likelihood)

            prev_end_loc = end_loc
            if end_loc == seq_len:
                break
        ppl = int(torch.exp(torch.stack(nlls).sum() / end_loc))
        return ppl
    

    def check(self, sentence):
        total_valid_char = re.findall("[a-zA-Z0-9]+", sentence)
        total_valid_char = sum([len(x) for x in total_valid_char])

        if total_valid_char < 100:
            return {"output": "Please input more text (min 100 characters)"}, "Please input more text (min 100 characters)"
        
        lines = re.split(r'(?<=[.?!][ \[\(])|(?<=\n)\s*',sentence)
        lines = list(filter(lambda x: (x is not None) and (len(x) > 0), lines))

        ppl = self.getPPL(sentence)
        self.perplexity = ppl

        offset = ""
        pp_line = []
        for i, line in enumerate(lines):
            if re.search("[a-zA-Z0-9]+", line) == None:
                continue
            if len(offset) > 0:
                line = offset + line
                offset = ""

            if line[0] == "\n" or line[0] == " ":
                line = line[1:]
            if line[-1] == "\n" or line[-1] == " ":
                line = line[:-1]
            elif line[-1] == "[" or line[-1] == "(":
                offset = line[-1]
                line = line[:-1]
            ppl = self.getPPL(line)
            pp_line.append(ppl)
            
        perplexity_per_line = sum(pp_line)/len(pp_line)
        self.ppl = ppl
        self.burstiness = max(pp_line)
        results = self.getResults(perplexity_per_line)
        self.results = results
        self.process_time = round(time.time() - self.start_time)
        return results
    
    def details(self):
        data = {
            "process_time": self.process_time,
            "output": self.results["output"],
            "perplexity": self.perplexity,
            "perplexity_per_line": self.ppl,
            "burstiness": self.burstiness,
            "code": self.results["code"]
        }

        return data
    


class GPTDetector:
    def __init__(self, model:str="gpt2", device:str="cuda"):
        self.loader = Loader(model=model, device=device)

    def check(self, prompt:str):
        return self.loader.check(prompt)
    
    def details(self):
        return self.loader.details()