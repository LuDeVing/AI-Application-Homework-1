import os
import time
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env")

client = genai.Client(api_key=API_KEY)

MODELS = [
    "gemini-3-flash-preview",
    "gemini-3.1-flash-lite-preview",
]

PROMPT = (
    "A farmer has 17 sheep. All but 9 die. How many sheep are left? "
    "Explain your reasoning step by step."
)

# Pricing (paid tier, per 1M tokens) — March 2026
COST_PER_1M = {
    "gemini-3-flash-preview":        {"input": 0.50, "output": 3.00},
    "gemini-3.1-flash-lite-preview": {"input": 0.25, "output": 1.50},
}


def calc_cost(model: str, input_tokens: int, output_tokens: int) -> float:
    rates = COST_PER_1M.get(model, {"input": 0.10, "output": 0.40})
    return (input_tokens * rates["input"] + output_tokens * rates["output"]) / 1_000_000


results = []

print(f"Prompt: {PROMPT}\n")
print("=" * 70)

for model_name in MODELS:
    print(f"\nModel: {model_name}")
    print("-" * 40)

    start = time.monotonic()
    response = client.models.generate_content(
        model=model_name,
        contents=PROMPT,
    )
    latency_ms = int((time.monotonic() - start) * 1000)

    text = response.text
    usage = response.usage_metadata
    input_tokens = usage.prompt_token_count
    output_tokens = usage.candidates_token_count
    total_tokens = usage.total_token_count
    cost = calc_cost(model_name, input_tokens, output_tokens)

    print(f"Response:\n{text}")
    print(f"\nTokens  — input: {input_tokens}  output: {output_tokens}  total: {total_tokens}")
    print(f"Latency — {latency_ms:,} ms")
    print(f"Cost    — ${cost:.8f} (paid-tier equivalent)")

    results.append({
        "model": model_name,
        "input": input_tokens,
        "output": output_tokens,
        "total": total_tokens,
        "latency_ms": latency_ms,
        "cost": cost,
    })

print("\n" + "=" * 70)
print("\nSummary table")
print(f"{'Call':<5} {'Model':<30} {'Input':>8} {'Output':>8} {'Total':>8} {'Latency':>12} {'Cost':>14}")
print("-" * 90)
for i, r in enumerate(results, 1):
    print(
        f"{i:<5} {r['model']:<30} {r['input']:>8} {r['output']:>8} {r['total']:>8} "
        f"{r['latency_ms']:>10,} ms  ${r['cost']:.8f}"
    )
