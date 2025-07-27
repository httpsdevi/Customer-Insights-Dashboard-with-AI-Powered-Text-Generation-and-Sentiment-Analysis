from flask import Flask, render_template, request, redirect, url_for
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

app = Flask(__name__)

# Initialize models
try:
    nltk.data.find('vader_lexicon')
except LookupError:
    nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

# Load GPT-2 model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')
tokenizer.pad_token = tokenizer.eos_token

def analyze_sentiment(text):
    """Analyze sentiment using NLTK's Vader"""
    scores = sia.polarity_scores(text)
    
    # Determine overall sentiment
    if scores['compound'] >= 0.05:
        sentiment = 'Positive'
    elif scores['compound'] <= -0.05:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'
    
    return {
        'sentiment': sentiment,
        'scores': scores
    }

def generate_text(prompt, max_length=100):
    """Generate text using GPT-2"""
    try:
        # Encode input text
        inputs = tokenizer.encode(prompt, return_tensors='pt', max_length=512, truncation=True)
        
        # Generate text
        with torch.no_grad():
            outputs = model.generate(
                inputs,
                max_length=len(inputs[0]) + max_length,
                num_return_sequences=1,
                temperature=0.7,
                do_sample=True,
                pad_token_id=tokenizer.eos_token_id
            )
        
        # Decode generated text
        generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # Return only the generated part (remove the original prompt)
        return generated_text[len(prompt):].strip()
    
    except Exception as e:
        return f"Error generating text: {str(e)}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    user_text = request.form.get('text', '').strip()
    
    if not user_text:
        return redirect(url_for('index'))
    
    # Perform sentiment analysis
    sentiment_result = analyze_sentiment(user_text)
    
    # Generate additional text
    generated_text = generate_text(user_text, max_length=80)
    
    return render_template('result.html', 
                         original_text=user_text,
                         sentiment_result=sentiment_result,
                         generated_text=generated_text)

if __name__ == '__main__':
    app.run(debug=True)
