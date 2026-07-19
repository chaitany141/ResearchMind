# ResearchMind 🔬

ResearchMind is an advanced Multi-Agent AI System built with Streamlit and LangChain. It uses a team of specialized AI agents working together to search the web, extract content, and write detailed, well-structured research reports on any given topic.

Demo : https://researchmind-multi-ai-agent.streamlit.app/

## Features ✨

- **Multi-Agent Pipeline**: Utilizes four distinct steps (Search, Reader, Writer, Critic) for high-quality outputs.
  1. **Search Agent**: Gathers recent web information using Tavily.
  2. **Reader Agent**: Scrapes and extracts deep content from the most relevant URLs.
  3. **Writer Agent**: Synthesizes the gathered information into a detailed research report.
  4. **Critic Agent**: Reviews, scores, and provides feedback on the generated report.
- **Modern UI**: A sleek, custom-designed Streamlit interface with step-by-step progress tracking.
- **Powered by Groq**: Uses Groq's blazing-fast Llama 3 models for natural language generation and reasoning.

## Prerequisites 📦

- Python 3.10+
- A [Groq API Key](https://console.groq.com/keys) (for the LLM)
- A [Tavily API Key](https://tavily.com/) (for web searching)

## Installation 🚀

1. **Clone the repository**
   ```bash
   git clone https://github.com/chaitany141/ResearchMind.git
   cd ResearchMind
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install the dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your environment variables**
   Create a `.env` file in the root directory and add your API keys:
   ```env
   GROQ_API_KEY="your_groq_api_key_here"
   TAVILY_API_KEY="your_tavily_api_key_here"
   ```

## Usage 💡

Start the Streamlit app:
```bash
streamlit run app.py
```

1. Open your browser to `http://localhost:8501`.
2. Enter a research topic (e.g., "Quantum computing breakthroughs in 2025").
3. Click **Run Research Pipeline** and watch the agents work in real-time!
4. Download the generated research report directly as a Markdown (`.md`) file.

## Tech Stack 🛠️

- [Streamlit](https://streamlit.io/) - Frontend web framework
- [LangChain](https://langchain.com/) - LLM orchestration and Agent creation
- [Groq](https://groq.com/) - High-speed LLM inference
- [Tavily](https://tavily.com/) - AI-powered Search API
