from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
import torch
from PIL import Image

class ImageCaptioning:
    def __init__(self, model:str="nlpconnect/vit-gpt2-image-captioning", device:str="cuda"):
        self.device = device
        self.model = VisionEncoderDecoderModel.from_pretrained(model).to(device)
        self.feature_extractor = ViTImageProcessor.from_pretrained(model)
        self.tokenizer = AutoTokenizer.from_pretrained(model)

    def predict(self, path:str, max_length:int=16, num_beams:int=4):
        gen_kwargs = {"max_length": max_length, "num_beams": num_beams}
        images = Image.open(path)
        if images.mode != "RGB":
          images = images.convert(mode="RGB")

        pixel_values = self.feature_extractor(images=images, return_tensors="pt").pixel_values
        pixel_values = pixel_values.to(self.device)

        output_ids = self.model.generate(pixel_values, **gen_kwargs)

        preds = self.tokenizer.batch_decode(output_ids, skip_special_tokens=True)
        return preds[0]
