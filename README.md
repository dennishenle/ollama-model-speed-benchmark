# Ollama Model Speed Benchmark

A command-line tool to benchmark the inference speed of locally installed [Ollama](https://ollama.com/) models. Measures both prompt evaluation and token generation performance in tokens per second.

## Requirements

- **Python 3.7+**
- **[Ollama](https://ollama.com/)** — must be installed and running locally
- **requests** — Python HTTP library

### Installing Ollama

Download and install Ollama from [https://ollama.com/download](https://ollama.com/download), or install via Homebrew on macOS:

```bash
brew install ollama
```

Start the Ollama server:

```bash
ollama serve
```

Pull at least one model before running the benchmark:

```bash
ollama pull llama3
```

### Installing Python Dependencies

```bash
pip install requests
```

## Usage

Run the benchmark script:

```bash
python main.py
```

The tool will:

1. List all locally installed Ollama models
2. Prompt you to select a model
3. Prompt you for a custom input (or use the default: *"Explain the theory of relativity in detail."*)
4. Send the prompt to the Ollama API and display performance metrics

### Example Output

```
📦 Installed Ollama Models:
------------------------------
  [1] llama3:latest
  [2] mistral:latest
------------------------------

Select a model (number): 1

✏️  Enter your prompt (or press Enter for default):

🚀 Running benchmark for: llama3:latest
📝 Prompt: Explain the theory of relativity in detail.

========================================
  Model             : llama3:latest
  Tokens generated  : 512
  Generation time   : 8.34s
  🔥 Tokens/sec     : 61.39
----------------------------------------
  Prompt tokens     : 9
  Prompt eval time  : 0.21s
  ⚡ Prompt tok/sec : 42.86
========================================
```

## How It Works

The script calls the Ollama REST API at `http://localhost:11434/api/generate` with streaming disabled, then extracts timing metadata from the response to compute:

- **Tokens/sec** — token generation throughput (`eval_count / eval_duration`)
- **Prompt tok/sec** — prompt evaluation throughput (`prompt_eval_count / prompt_eval_duration`)

## License

MIT
