# AI-Powered Text Generation and Sentiment Analysis Dashboard

A comprehensive Flask web application that performs advanced text sentiment analysis using NLTK's VADER sentiment analyzer and generates contextually relevant text using the GPT-2 model from Hugging Face Transformers.

## ✨ Features

### 🎯 Sentiment Analysis
- **VADER Sentiment Analysis**: Utilizes NLTK's VADER (Valence Aware Dictionary and sEntiment Reasoner) for comprehensive sentiment scoring
- **Detailed Metrics**: Provides positive, negative, neutral, and compound sentiment scores
- **Visual Representation**: Interactive progress bars and color-coded results
- **Overall Classification**: Automatically categorizes text as Positive, Negative, or Neutral

### 🤖 AI Text Generation
- **GPT-2 Integration**: Leverages Hugging Face's GPT-2 model for contextual text generation
- **Customizable Parameters**: Optimized generation settings for creative and coherent output
- **Context-Aware**: Generates text that continues naturally from your input

### 🎨 Modern UI/UX
- **Responsive Design**: Bootstrap-powered responsive interface that works on all devices
- **Interactive Dashboard**: Real-time analysis with smooth animations and transitions
- **Copy Functionality**: Easy-to-use copy buttons for generated content
- **Visual Feedback**: Loading states, progress indicators, and success notifications

### 🚀 Advanced Features
- **RESTful API**: JSON API endpoints for programmatic access
- **Error Handling**: Comprehensive error handling and user feedback
- **Performance Optimization**: Efficient model loading and caching
- **Print Support**: Print-friendly results page

## 🛠️ Technologies Used

### Backend
- **Python 3.8+**: Core programming language
- **Flask 2.3.3**: Web framework for the application
- **NLTK 3.8.1**: Natural Language Toolkit for sentiment analysis
- **Transformers 4.35.2**: Hugging Face library for GPT-2 integration
- **PyTorch 2.1.0**: Deep learning framework for model inference

### Frontend
- **HTML5 & CSS3**: Modern web standards
- **Bootstrap 5.3.0**: Responsive CSS framework
- **Font Awesome 6.4.0**: Icon library
- **JavaScript ES6+**: Interactive functionality

### AI Models
- **VADER Sentiment Analyzer**: Rule-based sentiment analysis tool
- **GPT-2**: Generative Pre-trained Transformer 2 for text generation

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- 4GB+ RAM (recommended for GPT-2 model)

### Step-by-Step Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd ai-text-dashboard
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Download required NLTK data**:
   ```bash
   python -c "import nltk; nltk.download('vader_lexicon')"
   ```
   Or run:
   ```bash
   python -m nltk.downloader vader_lexicon
   ```

5. **Run the application**:
   ```bash
   python run.py
   ```

6. **Access the application**:
   Open your web browser and navigate to `http://localhost:5000`

## 📁 Project Structure

```
ai-text-dashboard/
├── app.py                 # Main Flask application with routes and logic
├── run.py                 # Application entry point and server configuration
├── requirements.txt       # Python package dependencies
├── templates/
│   ├── index.html        # Home page with input form
│   └── result.html       # Results page with analysis display
├── static/               # Static files (if needed for custom assets)
├── README.md             # Project documentation
└── .gitignore           # Git ignore file
```

### File Descriptions

- **`app.py`**: Core application logic including sentiment analysis, text generation, and route handling
- **`run.py`**: Application runner with server configuration
- **`requirements.txt`**: Complete list of Python dependencies with version specifications
- **`templates/index.html`**: Responsive home page with modern UI and input form
- **`templates/result.html`**: Comprehensive results page with visual sentiment analysis and generated text display

## 🚀 Usage Guide

### Web Interface

1. **Navigate to the home page** at `http://localhost:5000`
2. **Enter your text** in the provided textarea (any length supported)
3. **Click "Analyze & Generate"** to process your text
4. **View comprehensive results**:
   - Original input text
   - Detailed sentiment analysis with visual progress bars
   - AI-generated continuation text
5. **Use additional features**:
   - Copy text to clipboard with one click
   - Print results for offline reference
   - Analyze new text with the "Analyze New Text" button

### API Endpoints

#### POST /api/analyze
Programmatic access to the analysis functionality.

**Request:**
```json
{
  "text": "Your text to analyze here"
}
```

**Response:**
```json
{
  "sentiment": {
    "positive": 0.234,
    "negative": 0.087,
    "neutral": 0.679,
    "compound": 0.4215,
    "overall": "Positive",
    "color": "success"
  },
  "generated_text": "AI-generated continuation text..."
}
```

## 📊 Sentiment Analysis Details

### VADER Sentiment Analyzer
The application uses NLTK's VADER (Valence Aware Dictionary and sEntiment Reasoner) sentiment analysis tool, which provides:

#### Metrics Explained
- **Positive Score (0-1)**: Proportion of text that expresses positive sentiment
- **Negative Score (0-1)**: Proportion of text that expresses negative sentiment  
- **Neutral Score (0-1)**: Proportion of text that expresses neutral sentiment
- **Compound Score (-1 to +1)**: Normalized weighted composite score

#### Classification Rules
- **Positive**: Compound score ≥ 0.05
- **Negative**: Compound score ≤ -0.05  
- **Neutral**: Compound score between -0.05 and 0.05

### Advantages of VADER
- Handles social media text, slang, and emoticons
- Considers capitalization, punctuation, and word-shape
- No training data required (lexicon and rule-based)
- Fast and efficient for real-time analysis

## 🤖 AI Text Generation

### GPT-2 Model Configuration
The application uses Hugging Face's GPT-2 model with optimized parameters:

- **Model**: `gpt2` (117M parameters)
- **Max Length**: 100 additional tokens
- **Temperature**: 0.8 (balanced creativity/coherence)
- **Top-p Sampling**: 0.9 (nucleus sampling)
- **No Repeat N-gram**: 2 (prevents repetition)

### Generation Features
- **Context-Aware**: Continues from your input text naturally
- **Creative Output**: Balanced between creativity and coherence
- **Configurable**: Easy to adjust generation parameters
- **Error Handling**: Graceful handling of generation failures

## ⚙️ Configuration

### Environment Variables
You can customize the application behavior using environment variables:

```bash
export FLASK_ENV=development    # Enable debug mode
export FLASK_PORT=5000         # Change port (default: 5000)
export MODEL_CACHE_DIR=./models # GPT-2 model cache directory
```

### Model Parameters
Modify generation parameters in `app.py`:

```python
outputs = model.generate(
    inputs,
    max_length=len(inputs[0]) + max_length,  # Adjust max_length
    temperature=0.8,                         # Adjust creativity (0.1-2.0)
    top_p=0.9,                              # Adjust diversity (0.1-1.0)
    # Add more parameters as needed
)
```

## 🔧 Troubleshooting

### Common Issues

#### 1. VADER Lexicon Not Found
```
LookupError: VADER lexicon not found
```
**Solution:**
```bash
python -c "import nltk; nltk.download('vader_lexicon')"
```

#### 2. Out of Memory Error
```
RuntimeError: CUDA out of memory
```
**Solution:**
- Reduce `max_length` parameter
- Use CPU instead of GPU: `device = torch.device('cpu')`
- Increase system RAM or use swap

#### 3. Model Download Issues
**Solution:**
- Ensure stable internet connection
- Clear cache: `rm -rf ~/.cache/huggingface/`
- Manual download: Use `transformers-cli download gpt2`

#### 4. Port Already in Use
```
OSError: [Errno 48] Address already in use
```
**Solution:**
- Change port in `run.py`: `app.run(port=5001)`
- Kill existing process: `lsof -ti:5000 | xargs kill -9`

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and test thoroughly
4. Commit with descriptive messages: `git commit -m "Add feature X"`
5. Push to your fork: `git push origin feature-name`
6. Submit a pull request

### Development Guidelines
- Follow PEP 8 style guidelines
- Add comments for complex logic
- Test all new features
- Update documentation as needed

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **NLTK Team** for the VADER sentiment analysis tool
- **Hugging Face** for the Transformers library and GPT-2 model
- **Flask Community** for the excellent web framework
- **Bootstrap Team** for the responsive CSS framework

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Troubleshooting](#-troubleshooting) section
2. Search existing [Issues](../../issues)
3. Create a new issue with detailed information
4. Contact the maintainers

---

**Made with ❤️ using Flask, NLTK, and GPT-2**
