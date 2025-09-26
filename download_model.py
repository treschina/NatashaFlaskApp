from transformers import AutoModelForSequenceClassification, AutoTokenizer

model_name = "tabularisai/multilingual-sentiment-analysis"
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

model.save_pretrained("./model/model")
tokenizer.save_pretrained("./tokenizer")
