# LLM Engineering Projects

A collection of hands-on LLM (Large Language Model) engineering projects demonstrating practical applications of AI in real-world scenarios.

---

## 📑 Table of Contents

- [Project 1: Scraper Summarizer](#project-1-scraper-summarizer)
- [Project 2: Synthetic Data Generator](#project-2-synthetic-data-generator)
- [Project 3: Code Generator with HuggingFace Deployment](#project-3-code-generator-with-huggingface-deployment)
- [Project 4: Python to C++ Converter](#project-4-python-to-c-converter)
- [Project 5: Your Local RAG Assistant](#project-5-your-local-rag-assistant)
- [Project 6: LangGraph](#project-6-langgraph)
- [Project 7: RAG Solutions](#project-7-rag-solutions)
- [Project 8: News Research Assistant](#project-8-news-research-assistant)
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

## Project 5: Your Local RAG Assistant

A complete Retrieval-Augmented Generation (RAG) system that creates and queries a local vector database from your documents, enabling accurate question-answering with source attribution.

### 🎯 Overview

This project demonstrates building a production-ready RAG system:
- Create vector databases from local documents (PDF, DOCX)
- Use free HuggingFace embeddings or OpenAI embeddings
- Visualize embeddings in 2D using t-SNE
- Query documents with natural language
- Get answers with source attribution
- Interactive Gradio chat interface

### 📂 Project Structure

```
5_Your_Local_RAG_Assistant/
├── 5.1_Your_Local_RAG_Creation.ipynb    # Vector database creation
└── 5.2_Your_Local_RAG_Retreival.ipynb   # Query and retrieval system
```

### 🚀 Features

#### Part 1: RAG Creation (5.1)
- **Document Discovery**: Recursively finds PDF and DOCX files
- **Document Loading**: Uses LangChain loaders (PyPDFLoader, Docx2txtLoader)
- **Text Chunking**: Splits documents into manageable chunks with overlap
- **Embedding Options**:
  - OpenAI Embeddings (paid, high quality)
  - HuggingFace Sentence Transformers (free, good quality)
- **Vector Database**: Chroma DB with SQLite backend
- **Visualization**: 2D t-SNE plots of embedding space

**Key Features:**
```python
# Find and load documents
document_paths = find_documents(search_directory)
documents = load_documents(document_paths)

# Chunk and embed
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = text_splitter.split_documents(documents)

# Create vector store with free embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = Chroma.from_documents(documents=chunks, embedding=embeddings, persist_directory="mj_vector_db")
```

#### Part 2: RAG Retrieval (5.2)
- **Vector Database Loading**: Load existing Chroma databases
- **Conversational Retrieval**: LangChain ConversationalRetrievalChain
- **Source Attribution**: Includes source documents in responses
- **Multi-Model Support**: Switch between GPT and Claude
- **Memory**: Conversation history tracking
- **Streaming Responses**: Real-time answer generation
- **Gradio Chat Interface**: User-friendly web UI

**Advanced Features:**
```python
# Custom prompt with source information
template = """Answer the question based on the following context and include relevant source information:

Context with Sources: {context}
Question: {question}

Please provide your answer along with the sources used:"""

# Format documents with metadata
def format_docs_with_metadata(docs):
    formatted_docs = []
    for doc in docs:
        metadata_str = "\n".join([f"{k}: {v}" for k, v in doc.metadata.items()])
        formatted_doc = f"\n---\nContent: {doc.page_content}\nSource Information:\n{metadata_str}\n---"
        formatted_docs.append(formatted_doc)
    return "\n".join(formatted_docs)
```

### 💡 Use Cases

- **Knowledge Base Q&A**: Query company documentation
- **Research Assistant**: Search through research papers
- **Legal Document Analysis**: Find relevant clauses and precedents
- **Technical Documentation**: Get answers from manuals and guides
- **Personal Knowledge Management**: Query your notes and documents

### 🎨 Visualization Features

The project includes beautiful 2D visualizations of the embedding space:
- **t-SNE Dimensionality Reduction**: 384D vectors → 2D plot
- **Interactive Plotly Charts**: Hover to see document content
- **Color-Coded by Type**: Visualize document clustering
- **Metadata Display**: See source, type, and content preview

### 📊 Technical Details

**Embedding Dimensions:**
- HuggingFace `all-MiniLM-L6-v2`: 384 dimensions
- OpenAI `text-embedding-ada-002`: 1536 dimensions

**Chunking Strategy:**
- Chunk size: 1000 characters
- Overlap: 200 characters
- Preserves context across chunks

**Vector Database:**
- Chroma DB (open-source)
- SQLite backend
- Persistent storage
- Fast similarity search

### 🛠️ Usage Examples

**Creating a Vector Database:**
```python
# Find all documents
document_paths = find_documents("/path/to/documents")

# Load and chunk
documents = load_documents(document_paths)
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = text_splitter.split_documents(documents)

# Create vector store
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = Chroma.from_documents(
    documents=chunks, 
    embedding=embeddings, 
    persist_directory="my_vector_db"
)
```

**Querying the Database:**
```python
# Load existing database
vectorstore = load_or_check_db("my_vector_db")

# Set up retrieval chain
llm = ChatOpenAI(temperature=0.7, model_name="gpt-4o-mini")
retriever = vectorstore.as_retriever()
conversation_chain = ConversationalRetrievalChain.from_llm(
    llm=llm, 
    retriever=retriever, 
    memory=memory
)

# Query
result = conversation_chain.invoke({"question": "What is quantization?"})
print(result["answer"])
```

### 📋 Prerequisites

**Required:**
- Python 3.8+
- OpenAI API key (for GPT models) or Anthropic API key (for Claude)

**Python Packages:**
```bash
pip install langchain langchain-openai langchain-anthropic langchain-chroma
pip install sentence-transformers chromadb
pip install pypdf docx2txt chardet
pip install scikit-learn plotly gradio
pip install python-dotenv
```

**Document Support:**
- PDF files (via PyPDFLoader)
- DOCX files (via Docx2txtLoader)
- Markdown files (via TextLoader)

### 🎯 Key Advantages

**Cost-Effective:**
- Use free HuggingFace embeddings
- Use budget-friendly GPT-4o-mini
- Local vector database (no cloud costs)

**Privacy-First:**
- Documents never leave your machine
- Local embedding generation option
- Self-hosted vector database

**Production-Ready:**
- Conversation memory
- Source attribution
- Error handling
- Gradio web interface

---

## Project 6: LangGraph

A comprehensive introduction to LangGraph for building stateful, multi-agent AI systems with conditional logic, tool calling, and memory.

### 🎯 Overview

This project teaches LangGraph fundamentals through progressive examples:
- Build simple state graphs with conditional edges
- Add reasoning and tool calling capabilities
- Implement persistent memory across conversations
- Visualize graph structures with Mermaid diagrams

### 📂 Project Structure

```
6_LangGraph/
├── 1_SimpleGraph.ipynb                              # Basic graph structure
├── 2_SimpleGraph_with_Reasoning_&_Tools.ipynb       # Add tools and reasoning
├── 3_SimpleGraph_with_Reasoning_&_Tools_&_Memory.ipynb  # Add memory
├── requirements.txt                                  # Dependencies
└── images/
    ├── arithmetic.png                                # Graph visualization
    └── mermaid_image.png                            # Mermaid diagram
```

### 🚀 Features

#### Notebook 1: Simple Graph
**Core Concepts:**
- State management with TypedDict
- Node creation and execution
- Conditional edges
- Graph visualization

**Example:**
```python
class state(TypedDict):
    graph_state: str

def node_1(state):
    print("---Node 1---")
    return {"graph_state": state["graph_state"] + ": 1"}

def decide_next(state) -> Literal["node_2","node_3"]:
    if random.random() < 0.5:
        return "node_2"
    return "node_3"

# Build graph
builder = StateGraph(state)
builder.add_node("node_1", node_1)
builder.add_node("node_2", node_2)
builder.add_node("node_3", node_3)
builder.add_edge(START, "node_1")
builder.add_conditional_edges("node_1", decide_next)
builder.add_edge("node_2", END)
builder.add_edge("node_3", END)

graph = builder.compile()
```

#### Notebook 2: Reasoning & Tools
**Advanced Concepts:**
- Tool binding to LLMs
- ReAct pattern (Reasoning + Acting)
- Arithmetic operations as tools
- Tool condition checking

**Arithmetic Agent:**
```python
def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def add(a, b):
    """Add two numbers"""
    return a + b

def divide(a, b):
    """Divide two numbers"""
    return a / b

tools = [multiply, add, divide]
llm = ChatOpenAI(model="gpt-4o")
llm_with_tools = llm.bind_tools(tools)

# Define assistant node
def assistant(state: MessagesState):
    return {"messages": [llm_with_tools.invoke([system_message] + state["messages"])]}

# Build graph with tools
builder = StateGraph(MessagesState)
builder.add_node("assistant", assistant)
builder.add_node("tools", ToolNode(tools))
builder.add_edge(START, "assistant")
builder.add_conditional_edges("assistant", tools_condition)
builder.add_edge("tools", "assistant")

react_graph = builder.compile()
```

**Example Interaction:**
```
User: "What is 2 times 3?"
AI: [Calls multiply tool with a=2, b=3]
Tool: Returns 6
AI: "The result of 2 times 3 is 6."
```

#### Notebook 3: Memory Integration
**Memory Features:**
- MemorySaver for persistent state
- Thread-based conversations
- Context retention across queries
- Checkpointing

**With Memory:**
```python
memory = MemorySaver()
thread_id = "1"
config = {"configurable": {"thread_id": thread_id}}

react_graph = builder.compile(checkpointer=memory)

# First query
messages = [HumanMessage(content="What is 2 times 3?")]
result = react_graph.invoke({"messages": messages}, config)
# AI: "2 times 3 is 6"

# Follow-up query (remembers previous context)
messages = [HumanMessage(content="Add 4 to it")]
result = react_graph.invoke({"messages": messages}, config)
# AI: "Adding 4 to 6 gives you 10"
```

### 💡 Use Cases

**Agentic Workflows:**
- Multi-step reasoning tasks
- Tool-using agents
- Conditional logic flows
- State machine implementations

**Business Applications:**
- Customer service bots with context
- Data analysis agents
- Automated workflows
- Decision trees

**Research & Development:**
- Agent behavior testing
- Prompt engineering experiments
- Tool integration prototypes
- Graph-based AI architectures

### 🎨 Graph Visualization

LangGraph automatically generates Mermaid diagrams:

```python
# Generate and save graph visualization
mermaid_image = Image(graph.get_graph().draw_mermaid_png())
with open("images/mermaid_image.png", "wb") as f:
    f.write(mermaid_image.data)
```

**Visualization Shows:**
- Nodes (processing steps)
- Edges (transitions)
- Conditional branches
- Start and end points

### 📊 Key Concepts

**State Management:**
- TypedDict for type safety
- State updates via return values
- Immutable state patterns

**Conditional Logic:**
- Literal types for type-safe routing
- Dynamic edge selection
- Probabilistic branching

**Tool Integration:**
- Function binding to LLMs
- Automatic tool calling
- Tool result processing

**Memory & Persistence:**
- Checkpointing for state recovery
- Thread-based conversations
- Cross-session memory

### 🛠️ Technical Architecture

**LangGraph Components:**
1. **StateGraph**: Main graph builder
2. **MessagesState**: Built-in state for chat
3. **ToolNode**: Automatic tool execution
4. **MemorySaver**: Persistent state storage
5. **Conditional Edges**: Dynamic routing

**Integration with LangChain:**
- Uses LangChain tools
- Compatible with LangChain LLMs
- Supports LangChain messages

### 📋 Prerequisites

**Required:**
- OpenAI API key
- Python 3.8+

**Python Packages:**
```bash
pip install langgraph langchain-openai python-dotenv
```

### 🎯 Learning Path

1. **Start Simple**: Understand state and nodes (Notebook 1)
2. **Add Intelligence**: Learn tool calling (Notebook 2)
3. **Add Memory**: Implement persistence (Notebook 3)
4. **Build Custom**: Create your own agents

### 🔍 Advanced Patterns

**ReAct Pattern:**
- Reasoning: LLM thinks about what to do
- Acting: LLM calls appropriate tools
- Observation: LLM sees tool results
- Repeat: Continue until answer found

**Multi-Agent Systems:**
- Multiple specialized agents
- Agent coordination
- Shared state management
- Conditional agent selection

---

## Project 7: RAG Solutions

A comprehensive collection of RAG (Retrieval-Augmented Generation) implementations, from basic to advanced, demonstrating best practices and common pitfalls.

### 🎯 Overview

This project provides a complete RAG learning path:
- Basic RAG without chunking
- Chunking strategies
- Embedding visualizations
- Complete pipelines with Chroma and FAISS
- Fixing relevancy issues

### 📂 Project Structure

```
7_RAG_Solutions/
├── 1_RAG_Basic.ipynb                                    # Simple RAG
├── 2_RAG_withChunking.ipynb                            # Add chunking
├── 3_RAG_withChunkingEmbeddingsVisualizations.ipynb    # Visualize embeddings
├── 4_1_RAG_CompletePipeline_Chroma.ipynb               # Production Chroma
├── 4_2_RAG_CompletePiepline_FAISS.ipynb                # Production FAISS
└── 5_RAG_FixingCommonIssue_Relevency.ipynb             # Improve relevancy
```

### 🚀 Progressive Learning Path

#### 1. RAG Basic
**Concepts:**
- Simple context retrieval
- Brute-force keyword matching
- Direct context injection
- No vector embeddings

**Implementation:**
```python
# Simple keyword-based retrieval
def get_relevant_context(message):
    relevant_context = []
    for context_title, context_details in context.items():
        if context_title.lower() in message.lower():
            relevant_context.append(context_details)
    return relevant_context

# Direct context in prompt
system_message = "You are an expert in answering accurate questions about Insurellm..."
context = get_relevant_context(user_message)
response = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": system_message + "\n" + "\n".join(context)},
        {"role": "user", "content": user_message}
    ]
)
```

**Limitations:**
- No semantic understanding
- Keyword matching only
- Doesn't scale well
- No similarity ranking

#### 2. RAG with Chunking
**Improvements:**
- Document chunking
- Chunk size optimization
- Overlap strategies
- Better context management

**Chunking Strategy:**
```python
text_splitter = CharacterTextSplitter(
    chunk_size=1000,  # Characters per chunk
    chunk_overlap=200  # Overlap to preserve context
)
chunks = text_splitter.split_documents(documents)
```

**Benefits:**
- Manageable context sizes
- Better token usage
- Preserved context across boundaries
- Scalable to large documents

#### 3. RAG with Embeddings & Visualizations
**Advanced Features:**
- Vector embeddings
- Semantic similarity
- t-SNE visualizations
- Embedding space analysis

**Visualization:**
```python
# Reduce 384D embeddings to 2D
tsne = TSNE(n_components=2, random_state=42)
reduced_vectors = tsne.fit_transform(vectors)

# Plot with Plotly
fig = go.Figure(data=[go.Scatter(
    x=reduced_vectors[:, 0],
    y=reduced_vectors[:, 1],
    mode='markers',
    text=[f"Type: {t}<br>Text: {d[:100]}..." for t, d in zip(doc_types, documents)],
    hoverinfo='text'
)])
```

**Insights:**
- See document clustering
- Identify similar content
- Debug embedding quality
- Understand semantic relationships

#### 4. Complete Pipeline - Chroma
**Production Features:**
- Chroma vector database
- Persistent storage
- Efficient retrieval
- Metadata filtering
- Conversational memory

**Implementation:**
```python
# Create persistent vector store
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="vector_db"
)

# Set up retrieval chain
llm = ChatOpenAI(temperature=0.7, model_name="gpt-4o-mini")
memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
retriever = vectorstore.as_retriever()

conversation_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=retriever,
    memory=memory
)
```

#### 5. Complete Pipeline - FAISS
**FAISS Advantages:**
- Extremely fast similarity search
- Optimized for large-scale
- GPU acceleration support
- Multiple index types

**When to Use FAISS:**
- Large document collections (>100K documents)
- Need for sub-millisecond search
- GPU available
- Read-heavy workloads

**When to Use Chroma:**
- Smaller collections
- Need persistence
- Metadata filtering
- Easier setup

#### 6. Fixing Relevancy Issues
**Common Problems:**
- Irrelevant chunks retrieved
- Missing relevant information
- Poor ranking
- Context window overflow

**Solutions:**
```python
# 1. Adjust retrieval parameters
retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 5}  # Retrieve top 5 chunks
)

# 2. Use MMR (Maximum Marginal Relevance)
retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 5, "fetch_k": 20, "lambda_mult": 0.5}
)

# 3. Hybrid search (keyword + semantic)
# 4. Re-ranking with cross-encoder
# 5. Query expansion
# 6. Metadata filtering
```

### 💡 Use Cases

**Enterprise Knowledge Management:**
- Company documentation Q&A
- Policy and procedure lookup
- Employee onboarding
- Compliance checking

**Customer Support:**
- Product documentation search
- Troubleshooting guides
- FAQ automation
- Ticket resolution

**Research & Analysis:**
- Literature review
- Patent search
- Legal document analysis
- Medical records query

### 📊 RAG Architecture Comparison

| Feature | Basic RAG | With Chunking | With Embeddings | Complete Pipeline |
|---------|-----------|---------------|-----------------|-------------------|
| **Semantic Search** | ❌ | ❌ | ✅ | ✅ |
| **Scalability** | Low | Medium | High | Very High |
| **Accuracy** | Low | Medium | High | Very High |
| **Setup Complexity** | Simple | Simple | Medium | Complex |
| **Cost** | Very Low | Low | Medium | Medium |
| **Best For** | Prototypes | Small docs | Medium docs | Production |

### 🛠️ Best Practices

**Chunking:**
- Chunk size: 500-1000 characters
- Overlap: 10-20% of chunk size
- Preserve sentence boundaries
- Consider document structure

**Embeddings:**
- Use domain-specific models when available
- Cache embeddings for reuse
- Monitor embedding quality
- Consider fine-tuning for specialized domains

**Retrieval:**
- Start with k=3-5 chunks
- Use MMR to reduce redundancy
- Implement re-ranking for better results
- Add metadata filters for precision

**Evaluation:**
- Test with diverse queries
- Measure retrieval accuracy
- Monitor response quality
- Track latency and costs

### 📋 Prerequisites

**Required:**
- OpenAI API key
- Python 3.8+

**Python Packages:**
```bash
pip install langchain langchain-openai langchain-chroma
pip install sentence-transformers chromadb faiss-cpu
pip install pypdf docx2txt
pip install scikit-learn plotly gradio
pip install python-dotenv
```

### 🎯 Key Takeaways

1. **Start Simple**: Basic RAG for prototyping
2. **Add Chunking**: Essential for scalability
3. **Use Embeddings**: Semantic search is crucial
4. **Choose Vector DB**: Chroma for ease, FAISS for scale
5. **Optimize Relevancy**: Tune retrieval parameters
6. **Monitor Quality**: Continuous evaluation

---

## Project 8: News Research Assistant

A sophisticated multi-agent system that automatically researches news topics, analyzes articles, and generates comprehensive reports with source attribution.

### 🎯 Overview

This project demonstrates advanced agentic AI patterns:
- Multi-agent coordination
- NewsAPI integration
- Automated article ranking
- Sentiment and bias analysis
- Comprehensive report generation
- Markdown output with citations

### 📂 Project Structure

```
8_News_Research_Assistant/
├── runme.py                              # Main entry point
├── news_research_coordinator_light.py    # Orchestration logic
├── config.py                             # Configuration
├── agents/
│   ├── __init__.py
│   ├── base_agent.py                    # Base agent class
│   ├── search_agent.py                  # Article search
│   ├── analysis_agent.py                # Content analysis
│   └── report_agent.py                  # Report generation
├── reports/                              # Generated reports
└── requirements.txt
```

### 🚀 Features

#### Multi-Agent Architecture

**1. Search Agent**
- **NewsAPI Integration**: Fetches articles by topic and date range
- **GPT-Powered Ranking**: Uses LLM to evaluate article relevance
- **Source Evaluation**: Assesses credibility and quality
- **Smart Filtering**: Returns only the most relevant articles

```python
class SearchAgent(BaseAgent):
    async def process(self, query: Dict[str, str]) -> List[Dict]:
        # Fetch articles from NewsAPI
        raw_articles = await self._fetch_articles(query)
        
        # Use GPT to rank by relevance
        ranked_articles = await self._rank_articles(raw_articles, query['topic'])
        
        return ranked_articles[:MAX_ARTICLES_PER_SEARCH]
```

**2. Analysis Agent**
- **Article Summarization**: Concise summaries of each article
- **Key Point Extraction**: Identifies main takeaways
- **Sentiment Analysis**: Scores sentiment (-1 to 1)
- **Topic Identification**: Extracts main themes
- **Bias Detection**: Identifies potential biases
- **Overall Analysis**: Synthesizes findings across articles

```python
class AnalysisAgent(BaseAgent):
    async def process(self, articles: List[Dict]) -> Dict:
        results = {
            'summaries': [],
            'key_points': [],
            'sentiment': [],
            'topics': [],
            'biases': []
        }
        
        # Analyze each article
        for article in articles:
            analysis = await self._analyze_article(article)
            results['summaries'].append(analysis['summary'])
            # ... collect other metrics
        
        # Perform overall analysis
        results['overall_analysis'] = await self._perform_overall_analysis(results)
        
        return results
```

**3. Report Agent**
- **Executive Summary**: High-level findings
- **Detailed Analysis**: In-depth topic and source analysis
- **Recommendations**: Actionable insights
- **Source Attribution**: Full citation tracking
- **Markdown Formatting**: Professional output

#### Workflow Orchestration

```python
class NewsResearchCoordinatorLight:
    async def research_topic(self, topic: str, time_range: Dict[str, str] = None) -> Dict:
        # Step 1: Search for articles
        articles = await self.search_agent.process({
            'topic': topic,
            'time_range': time_range
        })
        
        # Step 2: Analyze articles
        analysis_results = await self.analysis_agent.process(articles)
        
        # Step 3: Generate report
        report_data = {
            'topic': topic,
            'timestamp': datetime.now().isoformat(),
            'articles': articles,
            'analysis': analysis_results
        }
        final_report = await self.report_agent.process(report_data)
        
        # Format and save
        markdown_content = self._format_report_markdown(final_report, topic)
        filename = self._save_report(markdown_content, topic)
        
        return final_report
```

### 💡 Use Cases

**Business Intelligence:**
- Competitive analysis
- Market trend monitoring
- Industry news tracking
- Brand sentiment analysis

**Research:**
- Literature review automation
- Topic exploration
- Source credibility assessment
- Trend identification

**Journalism:**
- Story research
- Source gathering
- Fact-checking
- Bias detection

**Investment:**
- Market sentiment analysis
- Company news monitoring
- Industry trend tracking
- Risk assessment

### 🎨 Report Structure

**Generated Report Includes:**

1. **Executive Summary**
   - Main findings
   - Key trends
   - Critical insights
   - Reliability assessment

2. **Detailed Analysis**
   - Topic analysis (main topics, relationships, emerging themes)
   - Source analysis (distribution, credibility, biases)
   - Sentiment overview
   - Conflicting viewpoints

3. **Recommendations**
   - Prioritized action items
   - Rationale for each recommendation
   - Implementation considerations

4. **Source Citations**
   - Full article references
   - Publication dates
   - Source credibility notes

### 📊 Technical Architecture

**Async/Await Pattern:**
```python
async def main():
    coordinator = NewsResearchCoordinatorLight()
    
    report = await coordinator.research_topic(
        topic="Artificial Intelligence Ethics",
        time_range={'start': '2025-05-17', 'end': '2025-05-19'}
    )
```

**Progress Tracking:**
```python
# Visual progress bars for each stage
search_pbar = tqdm(total=1, desc="🔍 Searching for articles", position=0)
analysis_pbar = tqdm(total=1, desc="📊 Analyzing articles", position=1)
report_pbar = tqdm(total=1, desc="📝 Generating final report", position=2)
```

**Error Handling:**
- Graceful degradation
- Default values for failed analyses
- Comprehensive error logging
- Retry logic for API calls

### 🛠️ Usage Examples

**Basic Usage:**
```python
import asyncio
from news_research_coordinator_light import NewsResearchCoordinatorLight

async def main():
    coordinator = NewsResearchCoordinatorLight()
    
    report = await coordinator.research_topic(
        topic="Climate Change Technology",
        time_range={
            'start': '2025-01-01',
            'end': '2025-01-31'
        }
    )
    
    print(f"Report saved to: {report['filename']}")

if __name__ == "__main__":
    asyncio.run(main())
```

**Custom Configuration:**
```python
# config.py
MAX_ARTICLES_PER_SEARCH = 10
OPENAI_MODEL = "gpt-4o-mini"
NEWS_API_KEY = "your-key-here"

SEARCH_AGENT_PROMPT = "You are an expert news curator..."
ANALYSIS_AGENT_PROMPT = "You are an expert content analyst..."
REPORT_AGENT_PROMPT = "You are an expert research report writer..."
```

### 📋 Prerequisites

**Required:**
- OpenAI API key
- NewsAPI key (free tier available at [newsapi.org](https://newsapi.org))
- Python 3.8+

**Python Packages:**
```bash
pip install openai newsapi-python python-dotenv tqdm asyncio
```

**Environment Variables:**
```env
OPENAI_API_KEY=your-openai-key
NEWS_API_KEY=your-newsapi-key
```

### 🎯 Key Features

**Intelligent Article Ranking:**
- GPT evaluates relevance, credibility, and quality
- Scores articles on multiple dimensions
- Filters out low-quality sources

**Comprehensive Analysis:**
- Multi-dimensional article evaluation
- Cross-article synthesis
- Bias and sentiment tracking
- Topic clustering

**Professional Output:**
- Markdown formatted reports
- Automatic file naming with timestamps
- Source attribution
- Executive summaries

**Scalable Architecture:**
- Async/await for performance
- Modular agent design
- Easy to extend with new agents
- Configurable parameters

### 🔍 Advanced Features

**JSON Response Parsing:**
```python
async def _parse_json_response(self, response: str, default_value: Any) -> Any:
    """Safely parse JSON from LLM response with fallback."""
    try:
        # Try to extract JSON from markdown code blocks
        if "```json" in response:
            json_str = response.split("```json")[1].split("```")[0].strip()
        else:
            json_str = response.strip()
        
        return json.loads(json_str)
    except Exception as e:
        print(f"Error parsing JSON: {str(e)}")
        return default_value
```

**Progress Visualization:**
- Real-time progress bars
- Stage-by-stage updates
- Article-by-article tracking
- Time estimates

**Report Persistence:**
- Automatic report saving
- Organized file structure
- Timestamp-based naming
- Markdown format for easy sharing

### 💰 Cost Considerations

**NewsAPI:**
- Free tier: 100 requests/day
- Developer tier: $449/month (unlimited)

**OpenAI:**
- GPT-4o-mini: ~$0.15 per report (typical)
- GPT-4o: ~$1.50 per report (higher quality)

**Optimization Tips:**
- Use GPT-4o-mini for cost savings
- Limit articles per search
- Cache article analyses
- Batch API calls

### 🚀 Future Enhancements

**Potential Additions:**
- Web scraping for full article content
- Multi-language support
- Custom source lists
- Historical trend analysis
- Interactive web UI
- Email report delivery
- Scheduled automated research

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

For Local RAG Assistant (Project 5):
```bash
pip install langchain langchain-openai langchain-anthropic langchain-chroma
pip install sentence-transformers chromadb pypdf docx2txt chardet
pip install scikit-learn plotly gradio python-dotenv
```

For LangGraph (Project 6):
```bash
pip install langgraph langchain-openai python-dotenv
```

For RAG Solutions (Project 7):
```bash
pip install langchain langchain-openai langchain-chroma
pip install sentence-transformers chromadb faiss-cpu
pip install pypdf docx2txt scikit-learn plotly gradio python-dotenv
```

For News Research Assistant (Project 8):
```bash
pip install openai newsapi-python python-dotenv tqdm asyncio
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

# For News Research Assistant (Project 8)
NEWS_API_KEY=your-newsapi-key-here
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
- **OpenAI**: For GPT models (Projects 1-8)
- **Anthropic**: For Claude models (Projects 1-5, optional)
- **HuggingFace**: For open-source models (Projects 2-3, optional)
- **NewsAPI**: For news article search (Project 8, free tier available)

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

**For RAG Projects (5 & 7):**
- 8GB+ RAM (for vector databases)
- 5GB+ free disk space (for embeddings and databases)
- SSD recommended for faster retrieval

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

### RAG/Vector Database Issues
- **Chroma DB**: Ensure persist_directory has write permissions
- **FAISS**: May require `faiss-gpu` for GPU support
- **Embeddings**: First run downloads models (~500MB)
- **Memory**: Large document collections may require more RAM
- Clear old databases if encountering corruption

### LangGraph Issues
- Ensure `langgraph` and `langchain-openai` versions are compatible
- Check that state TypedDict matches node return types
- Verify conditional edge return types match Literal types
- Use `graph.get_graph().draw_mermaid_png()` to debug structure

### News Research Assistant Issues
- **NewsAPI**: Free tier limited to 100 requests/day
- **Rate Limits**: Add delays between API calls if hitting limits
- **Async Issues**: Ensure using `asyncio.run()` for async functions
- **JSON Parsing**: LLM responses may need retry logic

---

## 📚 Learning Resources

These projects demonstrate key LLM engineering concepts:
- **Prompt Engineering**: System and user prompts
- **API Integration**: Multiple LLM providers (OpenAI, Anthropic, HuggingFace)
- **Web Scraping**: Practical data extraction
- **Streaming Responses**: Real-time output generation
- **Code Generation**: LLM-generated executable code
- **Code Execution**: Running generated code safely
- **Model Quantization**: Efficient model deployment
- **Model Deployment**: Production deployment with HuggingFace
- **Agentic Patterns**: Multi-step LLM workflows and multi-agent systems
- **RAG (Retrieval-Augmented Generation)**: Vector databases and semantic search
- **Vector Embeddings**: Document embeddings and similarity search
- **LangGraph**: Stateful graph-based agent workflows
- **LangChain**: Chains, memory, and retrieval
- **Performance Optimization**: Python to C++ conversion
- **Cross-Platform Development**: Multi-OS compiler support
- **Interactive UIs**: Gradio web interfaces
- **Async Programming**: Concurrent API calls and processing
- **Data Visualization**: t-SNE, Plotly, and embedding visualizations

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

- **OpenAI** for GPT models and embeddings
- **Anthropic** for Claude models
- **Meta** for Llama models
- **DeepSeek** for reasoning models
- **HuggingFace** for model hosting, inference endpoints, and sentence transformers
- **Ollama** for local model serving
- **Qwen team** for CodeQwen models
- **Google** for CodeGemma models
- **Gradio** for the UI framework
- **LangChain** for the orchestration framework
- **LangGraph** for stateful agent workflows
- **Chroma** for vector database
- **FAISS** (Facebook AI) for similarity search
- **NewsAPI** for news article access
- **Sentence Transformers** for embedding models

---

**Happy Building! 🚀**
