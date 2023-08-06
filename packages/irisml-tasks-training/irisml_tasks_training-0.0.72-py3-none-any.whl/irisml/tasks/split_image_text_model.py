import copy
import dataclasses
import torch.nn
import irisml.core


class Task(irisml.core.TaskBase):
    """Split a image-text model into an image model and a text model.

    Inputs:
        model (torch.nn.Module): An input model. It must have 'image_model' and 'text_model' attributes.
    """
    VERSION = '0.1.1'

    @dataclasses.dataclass
    class Inputs:
        model: torch.nn.Module

    @dataclasses.dataclass
    class Outputs:
        image_model: torch.nn.Module
        text_model: torch.nn.Module
        logit_scale: torch.Tensor

    def execute(self, inputs):
        image_model = torch.nn.Sequential(copy.deepcopy(inputs.model.image_model), copy.deepcopy(inputs.model.image_projection), NormModule())
        text_model = torch.nn.Sequential(copy.deepcopy(inputs.model.text_model), copy.deepcopy(inputs.model.text_projection), NormModule())
        logit_scale = copy.deepcopy(inputs.model.logit_scale)
        return self.Outputs(image_model, text_model, logit_scale)

    def dry_run(self, inputs):
        return self.execute(inputs)


class NormModule(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x = x / x.norm(dim=-1, keepdim=True)
        return x
