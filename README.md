# LLM Engineering Projects

A collection of hands-on LLM (Large Language Model) engineering projects demonstrating practical applications of AI in real-world scenarios.

---

## 📑 Table of Contents

- [Project 1: Scraper Summarizer](#project-1-scraper-summarizer)
- [Project 2: Synthetic Data Generator](#project-2-synthetic-data-generator)
- [Project 3: Code Generator with HuggingFace Deployment](#project-3-code-generator-with-huggingface-deployment)
- [Project 4: Python to C++ Converter](#project-4-python-to-c-converter)
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

## Project 3: Code Generator with HuggingFace Deployment

An advanced code translation system that converts Python code to high-performance C++ using frontier LLMs and open-source models deployed on HuggingFace endpoints.

### 🎯 Overview

This project demonstrates:
- Converting Python code to optimized C++ using AI
- Deploying open-source models to production via HuggingFace endpoints
- Building interactive code conversion interfaces with Gradio
- Benchmarking performance improvements (4x-15x speedup)
- Cross-platform C++ compilation (Windows, Linux, macOS)

### 📂 Project Structure

```
3_Code_Generator_with_HuggingFace_Deployment_&_UI/
├── Code_Generator_with_HuggingFace_Deployment.ipynb  # Full implementation
└── Final_UI.png                                       # UI screenshot
```

### 🚀 Features

#### Core Capabilities
- **Multi-Model Support**:
  - OpenAI GPT-4o / GPT-4o-mini
  - Claude 3.5 Sonnet / Claude 3 Haiku
  - CodeQwen1.5-7B-Chat (HuggingFace)
  - CodeGemma-7B-IT (HuggingFace)
- **Streaming Responses**: Real-time code generation with typewriter effect
- **Automatic Compilation**: Compiles and executes generated C++ code
- **Performance Benchmarking**: Side-by-side Python vs C++ execution comparison
- **Cross-Platform Support**: Auto-detects and uses appropriate compiler

#### HuggingFace Deployment
- **Production-Ready**: Deploy open-source models behind API endpoints
- **Inference Endpoints**: Use HuggingFace's managed infrastructure
- **Cost-Effective**: Pay only for compute time used
- **Scalable**: Easy to scale up/down based on demand

#### Gradio Interface Features
- **Dual Code Panels**: Python input and C++ output side-by-side
- **Model Selection**: Switch between GPT, Claude, and CodeQwen
- **Sample Programs**: Pre-loaded examples (Pi calculation, max subarray)
- **Execution Buttons**: Run Python and C++ code with one click
- **Results Comparison**: Visual comparison of outputs and execution times
- **Compiler Detection**: Automatically identifies available compilers

### 💡 Use Cases

#### Performance Optimization
Convert computationally intensive Python code to C++ for:
- Scientific computing
- Data processing pipelines
- Algorithm implementations
- Numerical simulations

#### Example Performance Gains

**Test 1: Pi Calculation (100M iterations)**
- Python: 15.23 seconds
- C++: 0.22 seconds
- **Speedup: ~70x faster**

**Test 2: Maximum Subarray Sum (10K elements, 20 runs)**
- Python: 3.25 seconds
- C++: 0.21 seconds
- **Speedup: ~15x faster**

### 🛠️ Technical Implementation

#### Prompt Engineering
```python
system_message = "You are an assistant that reimplements Python code in high performance C++ for an M1 Mac. "
system_message += "Respond only with C++ code; use comments sparingly and do not provide any explanation other than occasional comments. "
system_message += "The C++ response needs to produce an identical output in the fastest possible time."
```

#### Code Execution Pipeline
1. **Generate**: LLM converts Python to C++
2. **Clean**: Remove markdown code fences
3. **Write**: Save to `optimized.cpp`
4. **Compile**: Auto-detect and use appropriate compiler
5. **Execute**: Run and capture output
6. **Compare**: Display results side-by-side

#### Compiler Support
- **macOS**: Clang++ with `-O3 -march=native`
- **Linux**: GCC (g++) or Clang++
- **Windows**: Visual Studio 2019/2022 (cl.exe)

### 🌐 HuggingFace Endpoint Setup

1. **Create Endpoint**:
   - Visit [HuggingFace Endpoints](https://ui.endpoints.huggingface.co/)
   - Select model (CodeQwen1.5-7B-Chat or CodeGemma-7B-IT)
   - Choose instance type and region
   - Deploy endpoint

2. **Get Endpoint URL**:
   ```python
   CODE_QWEN_URL = "https://your-endpoint.endpoints.huggingface.cloud"
   ```

3. **Use in Code**:
   ```python
   from huggingface_hub import InferenceClient
   
   client = InferenceClient(CODE_QWEN_URL, token=hf_token)
   stream = client.text_generation(prompt, stream=True, max_new_tokens=3000)
   ```

4. **Important**: Pause endpoints when not in use to avoid charges!

### 📋 Prerequisites

**Required:**
- OpenAI API key (for GPT models)
- Anthropic API key (for Claude models)
- HuggingFace token (for endpoint access)
- C++ compiler (Clang++, GCC, or Visual Studio)

**Python Packages:**
```bash
pip install openai anthropic gradio huggingface_hub transformers python-dotenv
```

**Compilers:**
- **macOS**: Xcode Command Line Tools (`xcode-select --install`)
- **Linux**: GCC (`sudo apt install g++`) or Clang (`sudo apt install clang`)
- **Windows**: Visual Studio 2019/2022 with C++ tools

### 🎨 Gradio Interface

The interactive UI includes:
- **Python Code Editor**: Input your Python code
- **C++ Code Display**: View generated C++ code
- **Model Selector**: Choose GPT, Claude, or CodeQwen
- **Sample Programs**: Quick-load example code
- **Run Buttons**: Execute Python and C++ independently
- **Output Panels**: Compare results and execution times
- **Compiler Info**: Display detected compiler and architecture

### 💰 Cost Considerations

**HuggingFace Endpoints:**
- Pay per compute hour (varies by instance type)
- **Important**: Pause endpoints when not in use!
- Alternative: Use Modal for pay-per-use pricing

**API Costs:**
- GPT-4o-mini: Most cost-effective for this task
- Claude 3 Haiku: Budget-friendly alternative
- CodeQwen (self-hosted): No per-request costs

### 🔍 Advanced Features

#### Chat Template Formatting
```python
tokenizer = AutoTokenizer.from_pretrained(code_qwen)
messages = messages_for(python_code)
text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
```

#### Automatic Compiler Detection
The system automatically detects and tests compilers:
1. Writes test C++ program
2. Attempts compilation with available compilers
3. Verifies execution
4. Selects best option for platform

#### Streaming Integration
All models support streaming for real-time feedback:
```python
def stream_gpt(python):    
    stream = openai.chat.completions.create(
        model=OPENAI_MODEL, 
        messages=messages_for(python), 
        stream=True
    )
    reply = ""
    for chunk in stream:
        fragment = chunk.choices[0].delta.content or ""
        reply += fragment
        yield reply
```

### 📊 Business Applications

- **Legacy Code Migration**: Modernize Python codebases to C++
- **Performance Engineering**: Optimize critical code paths
- **Algorithm Development**: Prototype in Python, deploy in C++
- **Education**: Learn C++ by seeing Python translations
- **Code Review**: Understand performance implications
- **Cross-Language Teams**: Bridge Python and C++ developers

---

## Project 4: Python to C++ Converter

A streamlined version of the code generator focused on practical Python-to-C++ conversion with comprehensive compiler support and performance benchmarking.

### 🎯 Overview

This project provides a production-ready tool for:
- Converting Python algorithms to high-performance C++
- Automatic compiler detection across all platforms
- Side-by-side performance comparison
- Interactive web interface for easy use

### 📂 Project Structure

```
4_Python_to_C++_Convertor_with_UI/
├── Python_to_C++_Convertor.ipynb        # Core conversion logic
├── Python_to_C++_Convertor_with_UI.ipynb  # Full Gradio interface
└── Final_UI.png                          # UI screenshot
```

### 🚀 Features

#### Simplified Workflow
- **Two-Model Support**: GPT-4o and Claude 3.5 Sonnet
- **Optimized Prompts**: Tuned for accurate C++ generation
- **Identical Output Guarantee**: Ensures Python and C++ produce same results
- **Performance Focus**: Optimizations for fastest execution time

#### Key Improvements Over Project 3
- **Simpler Setup**: No HuggingFace endpoints required
- **Better Compiler Detection**: Robust cross-platform support
- **Enhanced UI**: More intuitive interface
- **Sample Programs**: Built-in examples to get started quickly

### 💻 Sample Programs

#### Program 1: Pi Calculation
Calculates π using the Leibniz formula with 100 million iterations:
```python
def calculate(iterations, param1, param2):
    result = 1.0
    for i in range(1, iterations+1):
        j = i * param1 - param2
        result -= (1/j)
        j = i * param1 + param2
        result += (1/j)
    return result

result = calculate(100_000_000, 4, 1) * 4
```

**Results:**
- Python: ~15 seconds
- C++: ~0.22 seconds
- **Improvement: 68x faster**

#### Program 2: Maximum Subarray Sum
Implements Kadane's algorithm with random number generation:
```python
def max_subarray_sum(n, seed, min_val, max_val):
    # Linear Congruential Generator
    lcg_gen = lcg(seed)
    random_numbers = [next(lcg_gen) % (max_val - min_val + 1) + min_val 
                     for _ in range(n)]
    # Find maximum subarray sum
    max_sum = float('-inf')
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += random_numbers[j]
            if current_sum > max_sum:
                max_sum = current_sum
    return max_sum
```

**Results:**
- Python: ~3.2 seconds
- C++: ~0.21 seconds
- **Improvement: 15x faster**

### 🔧 Compiler Detection System

The project includes intelligent compiler detection:

```python
def c_compiler_cmd(filename_base):
    # Automatically detects and tests:
    # - Windows: Visual Studio 2022, 2019
    # - Linux: GCC, Clang++
    # - macOS: Clang++ with Apple Silicon optimizations
    
    # Returns: [Platform, Compiler, Command]
```

**Supported Compilers:**
- **Windows**: 
  - Visual Studio 2022 Community
  - Visual Studio 2019 Build Tools
- **Linux**: 
  - GCC (g++)
  - Clang++
- **macOS**: 
  - Clang++ (with `-march=native` for M1/M2/M3)

### 🎨 Enhanced Gradio Interface

**Layout:**
```
┌─────────────────────────────────────────────┐
│  Python Code        │    C++ Code           │
├─────────────────────────────────────────────┤
│  Sample Program     │  Architecture         │
│  Model Selection    │  Compiler Info        │
├─────────────────────────────────────────────┤
│  [Convert Code]                             │
├─────────────────────────────────────────────┤
│  [Run Python]       │  [Run C++]            │
├─────────────────────────────────────────────┤
│  Python Output      │  C++ Output           │
└─────────────────────────────────────────────┘
```

**Features:**
- Color-coded output panels (Python: blue, C++: green)
- Real-time streaming during conversion
- Automatic compiler status display
- One-click sample program loading

### 🛠️ Usage Examples

**Basic Conversion:**
```python
# In Jupyter notebook
from converter import optimize_gpt, execute_cpp

python_code = """
# Your Python code here
"""

# Generate C++ code
optimize_gpt(python_code)

# Compile and run
result = execute_cpp(generated_cpp)
print(result)
```

**Using Gradio Interface:**
1. Select a sample program or paste your own Python code
2. Choose model (GPT or Claude)
3. Click "Convert code"
4. Watch C++ code generate in real-time
5. Click "Run Python" and "Run C++" to compare performance

### 📊 Performance Analysis

#### Why C++ is Faster

1. **Compilation vs Interpretation**:
   - C++ compiles to native machine code
   - Python interprets bytecode at runtime

2. **Memory Management**:
   - C++ has direct memory control
   - Python has garbage collection overhead

3. **Type System**:
   - C++ uses static typing (compile-time optimization)
   - Python uses dynamic typing (runtime checks)

4. **Compiler Optimizations**:
   - `-O3`: Aggressive optimization
   - `-march=native`: CPU-specific instructions
   - Loop unrolling, vectorization, inlining

#### When to Use Each

**Use Python When:**
- Rapid prototyping needed
- Code readability is priority
- Development time is limited
- Performance is acceptable

**Use C++ When:**
- Performance is critical
- Processing large datasets
- Real-time requirements
- Embedded systems

### 💡 Business Applications

- **Algorithm Optimization**: Speed up critical code paths
- **Data Processing**: Handle large-scale data efficiently
- **Scientific Computing**: Accelerate simulations and calculations
- **Game Development**: Optimize game logic and physics
- **Financial Systems**: High-frequency trading algorithms
- **IoT/Embedded**: Resource-constrained environments

### 📋 Prerequisites

**Required:**
- OpenAI API key or Anthropic API key
- C++ compiler installed
- Python 3.8+

**Python Packages:**
```bash
pip install openai anthropic gradio python-dotenv
```

**Compiler Installation:**

*macOS:*
```bash
xcode-select --install
```

*Linux (Ubuntu/Debian):*
```bash
sudo apt update
sudo apt install g++ clang
```

*Windows:*
- Download Visual Studio Community 2022
- Select "Desktop development with C++"

### 🎯 Key Differences from Project 3

| Feature | Project 3 | Project 4 |
|---------|-----------|-----------|
| **Models** | GPT, Claude, CodeQwen, CodeGemma | GPT, Claude |
| **Setup** | Requires HuggingFace endpoints | Direct API only |
| **Complexity** | Advanced (deployment focus) | Simplified (usage focus) |
| **Compiler** | Basic detection | Robust cross-platform |
| **UI** | Standard Gradio | Enhanced with colors |
| **Best For** | Learning deployment | Production use |

### 🔍 Advanced Features

#### Identical Output Guarantee
The system ensures C++ produces identical results:
- Preserves random number generator behavior
- Maintains numerical precision
- Handles edge cases (overflow, underflow)
- Uses appropriate data types (long long, double)

#### Optimization Flags
```bash
# macOS/Linux
clang++ -O3 -std=c++17 -march=native -o optimized optimized.cpp

# Windows
cl /O2 /std:c++17 optimized.cpp
```

**Flags Explained:**
- `-O3`: Maximum optimization level
- `-std=c++17`: Use C++17 standard
- `-march=native`: Optimize for current CPU
- `/O2`: Windows optimization level 2

### 🚀 Getting Started

1. **Set up environment:**
```bash
# Create .env file
echo "OPENAI_API_KEY=your-key-here" > .env
echo "ANTHROPIC_API_KEY=your-key-here" >> .env
```

2. **Install compiler:**
```bash
# macOS
xcode-select --install

# Linux
sudo apt install g++

# Windows: Install Visual Studio
```

3. **Run notebook:**
```bash
jupyter notebook
# Open Python_to_C++_Convertor_with_UI.ipynb
# Run all cells
```

4. **Use interface:**
- Interface opens at `http://127.0.0.1:7860`
- Select sample program or paste code
- Click "Convert code"
- Compare results!

### 📈 Performance Tips

**For Best Results:**
- Use `-O3` optimization flag
- Enable `-march=native` for CPU-specific optimizations
- Profile code to identify bottlenecks
- Consider parallelization for multi-core systems
- Use appropriate data structures

**Common Optimizations:**
- Replace Python lists with C++ vectors
- Use `std::array` for fixed-size arrays
- Leverage `constexpr` for compile-time computation
- Minimize memory allocations
- Use references to avoid copies

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

For Code Generator (Project 3):
```bash
pip install openai anthropic gradio huggingface_hub transformers python-dotenv
```

For Python to C++ Converter (Project 4):
```bash
pip install openai anthropic gradio python-dotenv
```

**C++ Compiler Installation:**

macOS:
```bash
xcode-select --install
```

Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install g++ clang
```

Windows:
- Download and install Visual Studio Community 2022
- Select "Desktop development with C++" workload

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
- C++ compiler (for Projects 3 & 4)

**Recommended for Local Models:**
- 16GB+ RAM
- GPU with 8GB+ VRAM (for HuggingFace models)
- 50GB+ free disk space (for multiple models)

**Recommended for C++ Compilation:**
- Quad-core processor
- 16GB RAM
- SSD for faster compilation

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

### C++ Compilation Issues
- **macOS**: Ensure Xcode Command Line Tools installed
- **Linux**: Install build-essential: `sudo apt install build-essential`
- **Windows**: Verify Visual Studio C++ tools are installed
- Check compiler path is in system PATH
- Try compiling simple test program first

### HuggingFace Endpoint Issues
- Verify endpoint is running (not paused)
- Check endpoint URL is correct
- Ensure HF_TOKEN is valid
- Monitor endpoint logs for errors
- Remember to pause endpoints when not in use to avoid charges

---

## 📚 Learning Resources

These projects demonstrate key LLM engineering concepts:
- **Prompt Engineering**: System and user prompts
- **API Integration**: Multiple LLM providers
- **Web Scraping**: Practical data extraction
- **Streaming Responses**: Real-time output
- **Code Generation**: LLM-generated executable code
- **Code Execution**: Running generated code safely
- **Model Quantization**: Efficient model deployment
- **Model Deployment**: Production deployment with HuggingFace
- **Agentic Patterns**: Multi-step LLM workflows
- **Performance Optimization**: Python to C++ conversion
- **Cross-Platform Development**: Multi-OS compiler support
- **Interactive UIs**: Gradio web interfaces

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
- HuggingFace for model hosting and inference endpoints
- Ollama for local model serving
- Qwen team for CodeQwen models
- Google for CodeGemma models
- Gradio team for the UI framework

---

**Happy Building! 🚀**
