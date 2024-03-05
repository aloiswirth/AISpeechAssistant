import torch
from transformers import AutoTokenizer, AutoModelWithLMHead, AutoModelForCausalLM


def sent_scoring(model, tokenizer, text, cuda):
    input_ids = torch.tensor(tokenizer.encode(text)).unsqueeze(0)
    if cuda:
        input_ids = input_ids.to("cuda")
    with torch.no_grad():
        outputs = model(input_ids, labels=input_ids)
    loss, _ = outputs[:2]
    perplexity = loss.item()
    return perplexity


if __name__ == "__main__":
    # Initialisiere Modell und Tokenizer
    tokenizer = AutoTokenizer.from_pretrained("dbmdz/german-gpt2")
    # model = AutoModelWithLMHead.from_pretrained("dbmdz/german-gpt2")
    model = AutoModelForCausalLM.from_pretrained("dbmdz/german-gpt2")
    model.eval()
    cuda = torch.cuda.is_available()
    if cuda:
        model.to("cuda")

    # Berechne Score
    print(sent_scoring(model, tokenizer, "Goldfische sind pflegeleicht.", cuda))
    print(sent_scoring(model, tokenizer, "Gold Fische sind pflegeleicht.", cuda))
    print(
        sent_scoring(model, tokenizer, "Das ist ja mal eine schöne Überraschung.", cuda)
    )
    print(
        sent_scoring(
            model, tokenizer, "Na, das ist ja mal eine schöne Überraschung.", cuda
        )
    )
