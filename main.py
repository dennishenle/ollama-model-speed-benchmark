import requests
import subprocess
import sys

def get_installed_models():
    result = subprocess.run(["ollama", "list"], capture_output=True, text=True)
    lines = result.stdout.strip().split("\n")
    # Skip the header line
    models = []
    for line in lines[1:]:
        if line.strip():
            model_name = line.split()[0]
            models.append(model_name)
    return models

def choose_model(models):
    print("\n📦 Installed Ollama Models:")
    print("-" * 30)
    for i, model in enumerate(models, 1):
        print(f"  [{i}] {model}")
    print("-" * 30)

    while True:
        try:
            choice = int(input("\nSelect a model (number): "))
            if 1 <= choice <= len(models):
                return models[choice - 1]
            else:
                print(f"❌ Please enter a number between 1 and {len(models)}.")
        except ValueError:
            print("❌ Invalid input. Please enter a number.")

def benchmark(model, prompt):
    print(f"\n🚀 Running benchmark for: {model}")
    print(f"📝 Prompt: {prompt}\n")

    response = requests.post("http://localhost:11434/api/generate", json={
        "model": model,
        "prompt": prompt,
        "stream": False
    })

    if response.status_code != 200:
        print(f"❌ Error: {response.status_code} - {response.text}")
        sys.exit(1)

    data = response.json()
    tokens = data.get("eval_count", 0)
    duration_ns = data.get("eval_duration", 1)
    prompt_tokens = data.get("prompt_eval_count", 0)
    prompt_duration_ns = data.get("prompt_eval_duration", 1)

    gen_tps = tokens / duration_ns * 1e9
    prompt_tps = prompt_tokens / prompt_duration_ns * 1e9

    print("=" * 40)
    print(f"  Model             : {model}")
    print(f"  Tokens generated  : {tokens}")
    print(f"  Generation time   : {duration_ns / 1e9:.2f}s")
    print(f"  🔥 Tokens/sec     : {gen_tps:.2f}")
    print("-" * 40)
    print(f"  Prompt tokens     : {prompt_tokens}")
    print(f"  Prompt eval time  : {prompt_duration_ns / 1e9:.2f}s")
    print(f"  ⚡ Prompt tok/sec : {prompt_tps:.2f}")
    print("=" * 40)

if __name__ == "__main__":
    models = get_installed_models()

    if not models:
        print("❌ No models found. Pull a model first with: ollama pull <model>")
        sys.exit(1)

    model = choose_model(models)
    prompt = input("\n✏️  Enter your prompt (or press Enter for default): ").strip()
    if not prompt:
        prompt = "Explain the theory of relativity in detail."

    benchmark(model, prompt)
