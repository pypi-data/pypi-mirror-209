def run_abc(tokenizer, model, start_token, sep_token):
    import torch
    import pandas as pd
    from abc_lm_utilities import run_abc, eval_abc
    from transformers import AutoTokenizer, AutoModelForMaskedLM
    
    # SPECIFY HERE
    model_name = "NbAiLab/nb-bert-large"
    start_token = "[CLS] "
    sep_token = " [SEP]"

    model = AutoModelForMaskedLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model.eval()

    # create results df 
    df = run_abc(tokenizer, model, start_token, sep_token)
    
    # calculate difference with evaluation func
    dif = eval_abc(df)
    return dif

