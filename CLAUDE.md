# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a command-line tool to benchmark the inference speed of locally installed Ollama models. It measures both prompt evaluation and token generation performance in tokens per second by interacting with the Ollama REST API.

## Key Files

- `main.py` - The core benchmarking script that:
  - Lists installed Ollama models
  - Prompts user to select a model
  - Takes user input for prompt or uses default
  - Sends requests to Ollama API and displays performance metrics
- `README.md` - Documentation explaining usage and installation

## How to Run

1. Ensure Ollama is installed and running locally:
   ```bash
   ollama serve
   ```
2. Pull at least one model:
   ```bash
   ollama pull llama3
   ```
3. Install Python dependencies:
   ```bash
   pip install requests
   ```
4. Run the benchmark:
   ```bash
   python main.py
   ```

## Development Workflow

The tool is a simple Python script that makes HTTP requests to the local Ollama API. It uses:
- `subprocess` to call `ollama list` to get installed models
- `requests` library to communicate with Ollama API at `http://localhost:11434/api/generate`
- Parses JSON responses to extract timing metadata for performance calculations

## Architecture

The tool follows a straightforward command-line interface pattern:
1. Discover available models via `ollama list` subprocess call
2. Present model selection to user
3. Get user prompt input
4. Make POST request to Ollama API with streaming disabled
5. Parse response metadata to calculate performance metrics
6. Display results in a formatted table

The tool is designed to be simple and focused on benchmarking Ollama models specifically, without additional features or complexity.