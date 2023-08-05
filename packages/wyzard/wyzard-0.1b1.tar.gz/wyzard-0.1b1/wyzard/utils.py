from .exceptions import *
import os
import torch
from transformers import AutoModel, AutoTokenizer
from diffusers import StableDiffusionPipeline

def LoadLocalModel(path:str):
    if os.path.exists(path) == True:
        if os.path.exists(os.path.join(path, "pytorch_model.bin")) is True:
            return path
        else:
            raise PytorchModelNotFound()
    else:
        raise LocalModelNotFound()
    

def DownloadModelToLocal(model_name:str, path:str):
    if os.path.exists(path) == True:
        model = AutoModel.from_pretrained(model_name, output_attentions=True)
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model.save_pretrained(path)
        tokenizer.save_pretrained(path)
        return f"\nModel downloaded to {path}"
    else:
        raise PathDoesntExists()


def DiffusersDownloader(model_name:str, path:str, torch_dtype):
    if os.path.exists(path) == True:
        model = StableDiffusionPipeline.from_pretrained(model_name, torch_dtype=torch_dtype)
        model.save_pretrained(path)
        return f"\nModel downloaded to {path}"
    else:
        raise PathDoesntExists()