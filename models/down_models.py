import argparse
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

def main(args):
    model_name = args.model_name
    model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.bfloat16, cache_dir = '.')
    token = AutoTokenizer.from_pretrained(model_name)
    
    model.save_pretrained(model_name.split('/')[1])
    token.save_pretrained(model_name.split('/')[1])

if __name__=="__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--model-name', required=True, type=str)
    args = parser.parse_args()

    main(args)

