# HW01 — Gemini API Exploration

Calls two Gemini models with the same prompt, prints responses, and logs
token usage, latency, and paid-tier cost equivalents.

## How to run

```bash
# 1. Create and activate a virtual environment
python -m venv .venv
source .venv/Scripts/activate   # Windows
# source .venv/bin/activate     # Mac/Linux

# 2. Install dependencies
pip install -r requirements.txt

# 3. Add your API key
cp .env.example .env
# then edit .env and set GEMINI_API_KEY=your-key-here

# 4. Run
python main.py
```

## Models used

| Model | Description |
|---|---|
| `gemini-3-flash-preview` | Fast, capable standard model |
| `gemini-3.1-flash-lite-preview` | Reasoning variant — shows chain-of-thought traces |

## Prompt

> "A farmer has 17 sheep. All but 9 die. How many sheep are left? Explain your reasoning step by step."

## Cost & token table


| Call | Model | Input Tokens | Output Tokens | Total Tokens | Latency (ms) | Cost (paid equiv.) |
|---|---|---|---|---|---|---|
| 1 | gemini-3-flash-preview | 28 | 133 | 345 | 2,983 | $0.00041300 |
| 2 | gemini-3.1-flash-lite-preview | 28 | 70 | 98 | 945 | $0.00011200 |

## Reflection

1. Both models got the trick question right.
2. The flash model was nearly twice as slow despite receiving the same short prompt.
3. Its total token count was far higher than input + output, hinting at hidden reasoning tokens.
4. The lite model gave an equally clear answer, so the quality difference was smaller than I expected.
5. Costs were tiny overall, but the flash model cost nearly 4x more than the lite variant.
