# LLM Engineering Projects

A collection of hands-on LLM (Large Language Model) engineering projects demonstrating practical applications of AI in real-world scenarios.

---

## 📑 Table of Contents

- [Project 1: Scraper Summarizer](#project-1-scraper-summarizer)
- [Project 2: Synthetic Data Generator](#project-2-synthetic-data-generator)
- [Getting Started](#getting-started)
- [Requirements](#requirements)

---

## Project 1: Scraper Summarizer

A comprehensive web scraping and summarization toolkit that leverages both proprietary and open-source LLMs to analyze and summarize website content.

### 🎯 Overview

This project demonstrates how to build intelligent web scrapers that can:
- Extract and clean content from websites
- Generate concise summaries using AI
- Create professional business brochures from company websites
- Work with both cloud-based (OpenAI) and local (Ollama) models

### 📂 Project Structure

```
1_Scraper_Summarizer/
├── 1.1_Scraper_Summarizer.ipynb          # Basic scraper using OpenAI GPT-4o-mini
├── 1.2_Scraper_Summarizer_Ollama.ipynb   # Local implementation using Ollama
└── 1.3_BusinessBrochureGenerator.ipynb   # Advanced multi-page brochure generator
```

### 🚀 Features

#### 1.1 Basic Scraper Summarizer
- **Web Scraping**: Uses BeautifulSoup to extract clean text from websites
- **AI Summarization**: Leverages OpenAI's GPT-4o-mini for intelligent content summarization
- **Markdown Output**: Generates well-formatted summaries
- **System & User Prompts**: Demonstrates proper prompt engineering techniques

**Key Technologies:**
- `requests` & `BeautifulSoup` for web scraping
- OpenAI API for summarization
- Custom `Website` class for content extraction

#### 1.2 Ollama-Powered Scraper
- **Local AI Models**: Run LLMs locally using Ollama (Llama 3.2, DeepSeek)
- **Privacy-First**: No data leaves your machine
- **Cost-Free**: No API charges
- **Multiple Integration Methods**: Direct HTTP calls, Ollama package, or OpenAI-compatible API

**Benefits:**
- ✅ No API costs
- ✅ Complete data privacy
- ✅ Works offline
- ⚠️ Requires local compute resources

**Supported Models:**
- Llama 3.2 (3B parameters)
- Llama 3.2:1b (lightweight variant)
- DeepSeek-R1:1.5b (reasoning model)

#### 1.3 Business Brochure Generator
- **Multi-Page Analysis**: Intelligently identifies and scrapes relevant company pages
- **Smart Link Detection**: Uses LLM to determine which links are relevant (About, Careers, etc.)
- **Structured Output**: Generates professional markdown brochures
- **Streaming Responses**: Real-time typewriter-style output
- **Customizable Tone**: Easily adjust from professional to humorous

**Workflow:**
1. Scrape company landing page
2. AI identifies relevant links (About, Careers, Services)
3. Scrape identified pages
4. Generate comprehensive brochure from all content
5. Stream formatted output

**Use Cases:**
- Competitive analysis
- Investor presentations
- Recruitment materials
- Market research
- Sales enablement

### 💡 Business Applications

- **Content Generation**: Automatically create marketing materials
- **Competitive Intelligence**: Analyze competitor websites at scale
- **Lead Qualification**: Quickly understand prospect companies
- **Market Research**: Summarize industry trends from multiple sources
- **Documentation**: Generate company overviews for internal use

### 🛠️ Usage Examples

**Basic Summarization:**
```python
from scraper import Website, summarize, display_summary

# Simple summary
display_summary("https://example.com")
```

**Business Brochure Generation:**
```python
from brochure_generator import create_brochure, stream_brochure

# Generate streaming brochure
stream_brochure("Company Name", "https://company.com")
```

**Local Model with Ollama:**
```python
import ollama

response = ollama.chat(
    model="llama3.2",
    messages=[{"role": "user", "content": "Summarize this content..."}]
)
```

### 📋 Prerequisites

**For OpenAI Version:**
- OpenAI API key (set in `.env` file)
- Python packages: `requests`, `beautifulsoup4`, `openai`, `python-dotenv`

**For Ollama Version:**
- Ollama installed locally ([ollama.com](https://ollama.com))
- Models pulled: `ollama pull llama3.2`
- Python packages: `requests`, `beautifulsoup4`, `ollama`

---

## Project 2: Synthetic Data Generator

A powerful tool for generating realistic synthetic datasets using LLMs, supporting multiple data formats and both cloud and local models.

### 🎯 Overview

This project provides two implementations for generating synthetic datasets tailored to specific business problems:
- **Version 1**: Uses HuggingFace models (DeepSeek, Llama, Qwen2) with quantization
- **Version 2**: Uses OpenAI/Claude with code generation and execution capabilities

### 📂 Project Structure

```
2_Synthetic_Data_Generator/
├── 2.1_Synthetic_Data_Generator_v1.ipynb  # HuggingFace-based generator
└── 2.2_Synthetic_Dataset_Generator_v2.ipynb  # OpenAI/Claude with code execution
```

### 🚀 Features

#### Version 1: HuggingFace Models
- **Multiple Open-Source Models**:
  - DeepSeek-LLM-7B-Chat
  - Meta-Llama-3.1-8B-Instruct
  - Qwen2-7B-Instruct
- **4-bit Quantization**: Efficient model loading with BitsAndBytes
- **Gradio UI**: User-friendly web interface
- **Format Support**: CSV, JSON, Tabular
- **Customizable Record Count**: 50, 100, 150, or 200 records

**Key Features:**
- GPU acceleration support
- Streaming text generation
- Chat template formatting
- Memory-efficient quantization

#### Version 2: OpenAI/Claude with Code Execution
- **Dual Model Support**: OpenAI GPT-4o-mini and Claude 3.5 Sonnet
- **Dataset Types**:
  - **Tabular Data**: Structured datasets with columns
  - **Time-Series Data**: Temporal datasets
  - **Text Data**: Unstructured text datasets
- **Output Formats**: JSON, CSV, Parquet, Markdown
- **Code Generation**: Automatically generates Python code for dataset creation
- **Code Execution**: Runs generated code in virtual environment
- **Multi-Entity Support**: Separates output into multiple files when needed

**Workflow:**
1. User describes business problem
2. Specifies dataset type and format
3. LLM generates dataset structure and Python code
4. Code is extracted and executed locally
5. Dataset files are saved automatically

### 💡 Business Applications

- **ML Model Training**: Generate training data when real data is scarce
- **Testing & QA**: Create realistic test datasets
- **Privacy Compliance**: Replace sensitive data with synthetic alternatives
- **Prototyping**: Quickly create mock data for demos
- **Data Augmentation**: Expand existing datasets
- **Simulation**: Model business scenarios with synthetic data

### 🛠️ Usage Examples

**Version 1 (HuggingFace):**
```python
# Generate dataset using Gradio interface
# 1. Enter business description
# 2. Select model (DeepSeek/Llama/Qwen2)
# 3. Choose format (CSV/JSON/Tabular)
# 4. Set number of records
# 5. Click Generate
```

**Version 2 (OpenAI/Claude):**
```python
from dataset_generator import generate_dataset

# Generate and execute
result = generate_dataset(
    business_problem="E-commerce product catalog",
    dataset_format="Tabular",
    file_format="csv",
    num_samples=100,
    model="GPT"
)
```

### 📊 Supported Dataset Types

#### Tabular Data
- Structured rows and columns
- Perfect for databases and spreadsheets
- Example: Customer records, product inventories

#### Time-Series Data
- Temporal sequences
- Date/timestamp indexed
- Example: Stock prices, sensor readings, user activity logs

#### Text Data
- Unstructured text content
- Natural language datasets
- Example: Product descriptions, customer reviews, support tickets

### 🎨 Gradio Interface Features

Both versions include interactive web UIs with:
- **Input Fields**: Business problem description
- **Dropdowns**: Model selection, format selection, sample count
- **Buttons**: Generate dataset, execute code
- **Output Panels**: Display generated data and execution results
- **Real-time Streaming**: Watch generation in progress

### 📋 Prerequisites

**Version 1 (HuggingFace):**
- HuggingFace account and token
- GPU recommended (CUDA support)
- Python packages: `transformers`, `torch`, `bitsandbytes`, `gradio`, `huggingface_hub`

**Version 2 (OpenAI/Claude):**
- OpenAI API key and/or Anthropic API key
- Python packages: `openai`, `anthropic`, `gradio`, `pandas`, `numpy`

---

## Getting Started

### Installation

1. **Clone the repository:**
```bash
git clone <repository-url>
cd LLM_Engineering_Projects
```

2. **Create a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**

For Scraper Summarizer:
```bash
pip install requests beautifulsoup4 openai python-dotenv ipython
```

For Ollama support:
```bash
pip install ollama
# Install Ollama from https://ollama.com
ollama pull llama3.2
```

For Synthetic Data Generator (Version 1):
```bash
pip install transformers torch bitsandbytes gradio huggingface_hub
```

For Synthetic Data Generator (Version 2):
```bash
pip install openai anthropic gradio pandas numpy python-dotenv
```

4. **Set up environment variables:**

Create a `.env` file in the project root:
```env
# For OpenAI projects
OPENAI_API_KEY=sk-proj-your-key-here

# For Anthropic/Claude projects
ANTHROPIC_API_KEY=your-key-here

# For HuggingFace projects
HF_TOKEN=your-token-here
```

### Running the Projects

**Jupyter Notebooks:**
```bash
jupyter notebook
# Navigate to the desired project folder and open the notebook
```

**Gradio Interfaces:**
- Run the cells in the notebook until you reach the `ui.launch()` cell
- The interface will open automatically in your browser
- Default URL: `http://127.0.0.1:7860`

---

## Requirements

### Common Dependencies
- Python 3.8+
- Jupyter Notebook or JupyterLab
- Internet connection (for cloud models)

### API Keys Required
- **OpenAI**: For GPT-4o-mini models
- **Anthropic**: For Claude models (optional)
- **HuggingFace**: For downloading open-source models (optional)

### Hardware Recommendations

**Minimum:**
- 8GB RAM
- Dual-core processor
- 10GB free disk space

**Recommended for Local Models:**
- 16GB+ RAM
- GPU with 8GB+ VRAM (for HuggingFace models)
- 50GB+ free disk space (for multiple models)

---

## 🔧 Troubleshooting

### OpenAI API Issues
- Ensure API key starts with `sk-proj-`
- Check for whitespace in `.env` file
- Verify API key has sufficient credits

### Ollama Issues
- Confirm Ollama is running: visit `http://localhost:11434`
- Start server: `ollama serve`
- Pull models: `ollama pull llama3.2`

### HuggingFace Issues
- Authenticate: `huggingface-cli login`
- Accept model licenses on HuggingFace website
- Ensure sufficient disk space for model downloads

### Memory Issues
- Use smaller models (e.g., `llama3.2:1b`)
- Enable 4-bit quantization
- Reduce batch sizes
- Close other applications

---

## 📚 Learning Resources

These projects demonstrate key LLM engineering concepts:
- **Prompt Engineering**: System and user prompts
- **API Integration**: Multiple LLM providers
- **Web Scraping**: Practical data extraction
- **Streaming Responses**: Real-time output
- **Code Generation**: LLM-generated executable code
- **Model Quantization**: Efficient model deployment
- **Agentic Patterns**: Multi-step LLM workflows

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

---

## 📄 License

This project is provided for educational purposes. Please ensure compliance with:
- OpenAI's Terms of Service
- Anthropic's Terms of Service
- HuggingFace's Terms of Service
- Website scraping policies and robots.txt

---

## 🙏 Acknowledgments

- OpenAI for GPT models
- Anthropic for Claude models
- Meta for Llama models
- DeepSeek for reasoning models
- HuggingFace for model hosting
- Ollama for local model serving

---

**Happy Building! 🚀**
