from transformers import AutoTokenizer, AutoModel, utils
from bertviz import head_view

utils.loggers.set_verbosity_error()

model_name = "bert-base-german-cased"
input_text = "Der Hund mag seinen Knochen."
model = AutoModel.from_pretrained(model_name, output_attentions=True)
tokenizer = AutoTokenizer.from_pretrained(model_name)
inputs = tokenizer.encode(input_text, return_tensors='pt', add_special_tokens=True)
outputs = model(inputs)
attention = outputs[-1]
tokens = tokenizer.convert_ids_to_tokens(inputs[0])
head_view(attention, tokens)