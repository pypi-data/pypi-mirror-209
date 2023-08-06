# import os
#
# import torch
# from diffusers import StableDiffusionPipeline
#
# model_id = "CompVis/stable-diffusion-v1-4"
# device = "cuda"
#
# pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
# pipe = pipe.to(device)
# # save some memory in exchange for a small speed decrease
# # pipe.enable_attention_slicing()
#
# prompt = "bella twins"
# image = pipe(prompt).images[0]
#
# image.save("bella_twins.png")

from diffusers import StableDiffusionPipeline
import torch

model_id = "runwayml/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16, safety_checker=None).to("cuda")
prompt = "Emma Watson with blond hair, crying, white background"

image = pipe(prompt).images[0]
image.save("character.png")