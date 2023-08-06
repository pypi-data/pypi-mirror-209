#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : AI.  @by PyCharm
# @File         : llama_ziya
# @Time         : 2023/5/19 17:56
# @Author       : betterme
# @WeChat       : meutils
# @Software     : PyCharm
# @Description  :

from meutils.pipe import *
from chatllm.utils import DEVICE

from transformers import AutoTokenizer
from transformers import LlamaForCausalLM
import torch

device = torch.device("cuda")

query = "帮我写一份去西安的旅游计划"
model = LlamaForCausalLM.from_pretrained('IDEA-CCNL/Ziya-LLaMA-13B-v1', torch_dtype=torch.float16, device_map="auto")
tokenizer = AutoTokenizer.from_pretrained('IDEA-CCNL/Ziya-LLaMA-13B-v1')
inputs = '<human>:' + query.strip() + '\n<bot>:'

input_ids = tokenizer(inputs, return_tensors="pt").input_ids.to(device)
generate_ids = model.generate(
    input_ids,
    max_new_tokens=1024,
    do_sample=True,
    top_p=0.85,
    temperature=1.0,
    repetition_penalty=1.,
    eos_token_id=2,
    bos_token_id=1,
    pad_token_id=0)
output = tokenizer.batch_decode(generate_ids)[0]
print(output)


def load_llm(model_name_or_path="IDEA-CCNL/Ziya-LLaMA-13B-v1", device=DEVICE, num_gpus=2, **kwargs):
    model = LlamaForCausalLM.from_pretrained(model_name_or_path, trust_remote_code=True)
    tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, trust_remote_code=True)

    if torch.cuda.is_available() and device.lower().startswith("cuda"):
        num_gpus = min(num_gpus, torch.cuda.device_count())

        if num_gpus == 1:  # 单卡
            model = model.half().cuda()
            # model.transformer.prefix_encoder.float()
        elif 'chatglm' in model_name_or_path:  # chatglm多卡
            pass # todo: 增加多卡

    else:
        model = model.float().to(device)

    return model.eval(), tokenizer


def stream_chat():
    pass


def chat():
    pass
