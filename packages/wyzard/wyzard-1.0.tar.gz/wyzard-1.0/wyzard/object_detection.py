import torch
from transformers import AutoImageProcessor, AutoModelForObjectDetection
from PIL import Image
import matplotlib.pyplot as plt
from random import choice


COLORS = ["#ff7f7f", "#ff7fbf", "#ff7fff", "#bf7fff",
            "#7f7fff", "#7fbfff", "#7fffff", "#7fffbf",
            "#7fff7f", "#bfff7f", "#ffff7f", "#ffbf7f"]


class Loader:
    def __init__(self, model, device):
        self.device = device
        self.image_processor = AutoImageProcessor.from_pretrained(model)
        self.model = AutoModelForObjectDetection.from_pretrained(model).to(device)

    def get_figure(self, in_pil_img, in_results, font_size, font_color):
        fdic = {
            "style" : "normal",
            "size" : font_size,
            "color" : font_color,
            "weight" : "bold"
        }
        plt.figure(figsize=(16, 10))
        plt.imshow(in_pil_img)
        ax = plt.gca()

        for score, label, box in zip(in_results["scores"], in_results["labels"], in_results["boxes"]):
            selected_color = choice(COLORS)

            box_int = [i.item() for i in torch.round(box).to(torch.int32)]
            x, y, w, h = box_int[0], box_int[1], box_int[2]-box_int[0], box_int[3]-box_int[1]

            ax.add_patch(plt.Rectangle((x, y), w, h, fill=False, color=selected_color, linewidth=3, alpha=0.8))
            ax.text(x, y, f"{self.model.config.id2label[label.item()]}: {round(score.item()*100, 2)}%", fontdict=fdic, alpha=0.8)

        plt.axis("off")

        return plt.gcf()


    def infer(self, input_img, output_img, threshold, font_size, font_color):
        input_img = Image.open(input_img)
        target_sizes = torch.tensor([input_img.size[::-1]])

        inputs = self.image_processor(images=input_img, return_tensors="pt").to(self.device)
        outputs = self.model(**inputs)

        results = self.image_processor.post_process_object_detection(outputs, threshold=threshold, target_sizes=target_sizes)[0]

        figure = self.get_figure(input_img, results, font_size, font_color)
        figure.savefig(output_img, bbox_inches='tight')

        return results
    
    def models(self):
        return self.model
    

class ObjectDetection:
    def __init__(self, model:str="hustvl/yolos-small", device:str="cuda"):
        self.loader = Loader(model, device)

    def detect(self, input_img, output_img, threshold:int=0.9, font_size:int=18, font_color:str="yellow"):
        return self.loader.infer(input_img, output_img, threshold, font_size, font_color)
    
    def coordinates(self, results):
        coordinates = []
        for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
            box = [round(i, 2) for i in box.tolist()]
            coordinates.append({"object": self.loader.models().config.id2label[label.item()], "coordinates": box, "precision": round(score.item()*100, 2)})

        return coordinates