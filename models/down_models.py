from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = ''
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.bfloat16, cache_dir = '.')
token = AutoTokenizer.from_pretrained(model_name)

model.save_pretrained(model_name.split('/')[1])
token.save_pretrained(model_name.split('/')[1])

