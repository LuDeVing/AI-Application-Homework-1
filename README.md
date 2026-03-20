# HW01 — Gemini API Exploration

Calls two Gemini models with the same prompt, prints responses, and logs
token usage, latency, and paid-tier cost equivalents.

## How to run

```bash
pip install google-genai python-dotenv

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
| 1 | gemini-3-flash-preview | 28 | 140 | 418 | 3,405 | $0.00005880 |
| 2 | gemini-3.1-flash-lite-preview | 28 | 115 | 143 | 1,741 | $0.00003660 |

## Reflection

1. Both models got the trick question right.
2. The flash model was nearly twice as slow despite receiving the same short prompt.
3. Its total token count was far higher than input + output, hinting at hidden reasoning tokens.
4. The lite model gave an equally clear answer, so the quality difference was smaller than I expected.
5. Costs were tiny overall, but the flash model still cost nearly twice as much as the lite variant.
