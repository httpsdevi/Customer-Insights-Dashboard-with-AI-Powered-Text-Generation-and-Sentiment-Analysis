from flask import Flask, render_template, request, jsonify
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
import warnings

# Suppress warnings
warnings.filterwarnings("ignore")

app = Flask(__name__)

# Initialize sentiment analyzer
try:
    analyzer = SentimentIntensityAnalyzer()
except LookupError:
    nltk.download('vader_lexicon')
    analyzer = SentimentIntensityAnalyzer()

# Initialize GPT-2 model and tokenizer
print("Loading GPT-2 model...")
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

# Add pad token to tokenizer
tokenizer.pad_token = tokenizer.eos_token

print("Model loaded successfully!")

def analyze_sentiment(text):
    """Analyze sentiment of the given text"""
    scores = analyzer.polarity_scores(text)
    
    # Determine overall sentiment
    compound = scores['compound']
    if compound >= 0.05:
        overall = 'Positive'
        color = 'success'
    elif compound <= -0.05:
        overall = 'Negative'
        color = 'danger'
    else:
        overall = 'Neutral'
        color = 'warning'
    
    return {
        'positive': scores['pos'],
        'negative': scores['neg'],
        'neutral': scores['neu'],
        'compound': scores['compound'],
        'overall': overall,
        'color': color
    }

def generate_text(prompt, max_length=100):
    """Generate text using GPT-2 model"""
    try:
        # Encode the prompt
        inputs = tokenizer.encode(prompt, return_tensors='pt', max_length=512, truncation=True)
        
        # Generate text
        with torch.no_grad():
            outputs = model.generate(
                inputs,
                max_length=len(inputs[0]) + max_length,
                num_return_sequences=1,
                temperature=0.8,
                do_sample=True,
                pad_token_id=tokenizer.eos_token_id,
                no_repeat_ngram_size=2,
                top_p=0.9
            )
        
        # Decode the generated text
        generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # Remove the original prompt from the generated text
        generated_text = generated_text[len(prompt):].strip()
        
        return generated_text
    
    except Exception as e:
        return f"Error generating text: {str(e)}"

@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    """Analyze text and generate additional content"""
    text = request.form.get('text', '').strip()
    
    if not text:
        return render_template('index.html', error="Please enter some text to analyze.")
    
    # Perform sentiment analysis
    sentiment = analyze_sentiment(text)
    
    # Generate additional text
    generated = generate_text(text)
    
    return render_template('result.html', 
                         original_text=text,
                         sentiment=sentiment,
                         generated_text=generated)

@app.route('/api/analyze', methods=['POST'])
def api_analyze():
    """API endpoint for text analysis"""
    data = request.get_json()
    text = data.get('text', '').strip()
    
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    
    sentiment = analyze_sentiment(text)
    generated = generate_text(text)
    
    return jsonify({
        'sentiment': sentiment,
        'generated_text': generated
    })

if __name__ == '__main__':
    app.run(debug=True)
