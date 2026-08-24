# Open Source AI Tools to Make Money

> Last updated: 2026-08-24 · 30 projects · [How to refresh](#refresh)


A curated, auto-ranked list of open-source AI projects you can build a business on.
Ranked by GitHub stars. Updated weekly via GitHub Actions — free to run, free to host.

| # | Project | ⭐ Stars | Category | How to Make Money |
|---|---------|---------|----------|-------------------|
| 1 | [n8n](https://github.com/n8n-io/n8n) | 202.2k | Automation | Run an n8n automation agency: build and maintain no-code AI workflows for SMBs on a retainer. |
| 2 | [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) | 186.8k | AI Agents | Offer autonomous task execution as a service — charge per completed task or workflow run. |
| 3 | [ollama](https://github.com/ollama/ollama) | 179.3k | Local Models | Run local LLMs on your hardware and offer a private AI API to businesses worried about data leaks — charge monthly per seat. |
| 4 | [stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui) | 164.6k | Image Generation | Run an image-as-a-service API for e-commerce product shots — charge per image or bundle credits. |
| 5 | [open-webui](https://github.com/open-webui/open-webui) | 149.7k | LLM Tools | Deploy a private ChatGPT interface for corporate teams and charge per seat for managed hosting and SSO setup. |
| 6 | [langchain](https://github.com/langchain-ai/langchain) | 144.9k | LLM Tools | Build and sell AI chatbot integrations for SMBs using LangChain pipelines — fixed project fee plus monthly retainer. |
| 7 | [ComfyUI](https://github.com/Comfy-Org/ComfyUI) | 129.6k | Image Generation | Build a specialised image-generation SaaS for a niche (real estate renders |
| 8 | [llama.cpp](https://github.com/ggml-org/llama.cpp) | 125.4k | Local Models | Package on-premise LLM inference for legal and healthcare firms that cannot send data to the cloud — license per deployment. |
| 9 | [browser-use](https://github.com/browser-use/browser-use) | 110.3k | Automation | Build lead generation and data extraction bots for sales teams — charge per thousand records delivered. |
| 10 | [whisper](https://github.com/openai/whisper) | 107.9k | Audio & Transcription | Run a pay-per-minute transcription API for podcasters and legal firms using Whisper — batch discount tiers. |
| 11 | [playwright](https://github.com/microsoft/playwright) | 95.0k | Automation | Offer a QA automation service for web apps using Playwright — fixed monthly fee per client project. |
| 12 | [vllm](https://github.com/vllm-project/vllm) | 89.8k | LLM Tools | Run a high-throughput LLM inference API and undercut OpenAI pricing for startups that need scale — charge per million tokens. |
| 13 | [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | 88.2k | OCR | Offer document extraction for paper-heavy industries (insurance |
| 14 | [crawl4ai](https://github.com/unclecode/crawl4ai) | 79.3k | Automation | Sell web scraping as a service for market intelligence — tiered pricing by page volume per month. |
| 15 | [tesseract](https://github.com/tesseract-ocr/tesseract) | 76.1k | OCR | Build an invoice and receipt processing service for accounting firms — charge per document or monthly volume. |
| 16 | [mem0](https://github.com/mem0ai/mem0) | 63.9k | AI Agents | Add persistent memory to client chatbots and sell as a SaaS add-on billed monthly per active user. |
| 17 | [autogen](https://github.com/microsoft/autogen) | 60.6k | AI Agents | Build multi-agent automation pipelines for repetitive back-office work and sell as a managed service. |
| 18 | [meilisearch](https://github.com/meilisearch/meilisearch) | 59.1k | Search & Retrieval | Embed fast search into client web apps as a managed add-on — revenue share or flat monthly fee. |
| 19 | [crewAI](https://github.com/crewAIInc/crewAI) | 57.5k | AI Agents | Assemble industry-specific agent teams (legal research |
| 20 | [litellm](https://github.com/BerriAI/litellm) | 57.1k | LLM Tools | Build a cost-routing layer over multiple LLM providers and resell optimised inference to AI product teams — margin on token spend. |
| 21 | [LocalAI](https://github.com/mudler/LocalAI) | 48.6k | Local Models | Offer a drop-in OpenAI-compatible private API to data-sensitive organisations — monthly subscription per team. |
| 22 | [dspy](https://github.com/stanfordnlp/dspy) | 37.6k | LLM Tools | Build optimised LLM prompt pipelines for enterprises and sell prompt engineering as a managed service. |
| 23 | [diffusers](https://github.com/huggingface/diffusers) | 34.4k | Image Generation | Fine-tune diffusion models on brand assets and sell a model marketplace — licence per fine-tune download. |
| 24 | [qdrant](https://github.com/qdrant/qdrant) | 34.2k | Search & Retrieval | Build a semantic search API for e-commerce catalogues — monthly subscription per store. |
| 25 | [EasyOCR](https://github.com/JaidedAI/EasyOCR) | 29.9k | OCR | Build a receipt scanning and expense-tracking tool for small business owners — SaaS with free tier. |
| 26 | [chroma](https://github.com/chroma-core/chroma) | 29.1k | Search & Retrieval | Sell a RAG-powered document Q&A SaaS to law firms and consultancies — per-user monthly licence. |
| 27 | [haystack](https://github.com/deepset-ai/haystack) | 26.3k | LLM Tools | Create enterprise document Q&A systems and license per concurrent user or department. |
| 28 | [surya](https://github.com/datalab-to/surya) | 21.3k | OCR | Create a legal and financial document OCR pipeline with structured JSON output — sell API access by the page. |
| 29 | [pydantic-ai](https://github.com/pydantic/pydantic-ai) | 19.5k | AI Agents | Sell structured AI output integrations to companies replacing brittle regex parsing — charge per integration delivered. |
| 30 | [txtai](https://github.com/neuml/txtai) | 12.9k | Search & Retrieval | Offer a semantic search API service for content platforms needing intelligent discovery — usage-based pricing. |

---

## Refresh

Run this once locally to regenerate the README with fresh star counts:

```bash
pip install -r requirements.txt
cp .env.example .env   # paste your GitHub token (free — needs no scopes)
python refresh.py
```

**Add a repo:**
```bash
python refresh.py --add owner/repo "Category" "How you would monetize it."
```

**Skip a repo:**
```bash
python refresh.py --skip owner/repo
```

Or just edit `repos.csv` directly — set `include` to `yes` or `no`.

## Deployment (free)

This README is refreshed automatically every Monday at 08:00 UTC by a GitHub Actions
workflow (`.github/workflows/refresh.yml`). It uses the built-in `GITHUB_TOKEN` — no
secrets to configure.

To publish as a website: **Settings → Pages → Branch: main / folder: / (root)**.
GitHub Pages is free for public repos.
