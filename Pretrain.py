from transformers import pipeline

# Load a pre-trained text generation pipeline
generator = pipeline('text-generation', model='gpt2')

# Generate text
result = generator("Hello, I'm a language model,", max_length=50, num_return_sequences=1)
print(result[0]['generated_text'])
