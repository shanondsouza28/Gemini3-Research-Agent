# 🤖 Gemini 3 Autonomous Research Agent

> **An autonomous AI research agent powered by Gemini 3.0 Flash and DuckDuckGo. Unlike standard chatbots, this agent uses a self-correcting loop to browse the live web, synthesize findings, and generate structured, validated reports without human intervention.**

---

## 🌟 Key Features
* **Self-Correcting Search**: Uses advanced reasoning to determine if more research is needed based on initial findings.
* **Autonomous Navigation**: Loops through search results until a high-quality answer is formulated.
* **Structured Output**: Enforces data integrity using **Pydantic** schemas for topic, summary, and sources.
* **Clean Architecture**: Separated concerns with a modular `tools.py` and a central `main.py` controller.

---

## 🛠️ Tools & Data Sources
To ensure high-quality research, the agent utilizes the following:
* **DuckDuckGo Search API**: Integrated for anonymous, real-time web retrieval.
* **Wikipedia API**: Used for fetching high-level background and foundational data.
* **Gemini 3.0 Flash**: Leveraged for high-speed reasoning and synthesis of complex search data.
* **File System Tool**: Automatically saves finalized reports to `research_output.txt`.

---

## 🧠 How It Works: The Agentic Loop
This project utilizes a **ReAct (Reason + Act)** pattern. In your `main.py`, the `agent_executor` manages a cycle that allows the agent to self-correct:

1. **Analysis**: The agent evaluates the user's prompt to determine what information is missing.
2. **Tool Selection**: It autonomously chooses between `DuckDuckGo`, `Wikipedia`, or `Save File`.
3. **Observation & Refinement**: After each tool call, the agent "observes" the result. If the data is incomplete or irrelevant, it **re-runs the loop** with a refined query until the research goals are met.
4. **Structured Output**: Once satisfied, the agent validates the data against a Pydantic model to ensure a professional, error-free final report.

---

## 🚀 Getting Started

### 1. Installation
```bash
# Clone the repository
git clone [https://github.com/shanondsouza28/Gemini3-Research-Agent.git](https://github.com/shanondsouza28/Gemini3-Research-Agent.git)
cd Gemini3-Research-Agent

# Set up virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
2. Configuration
Create a .env file in the root directory:

Bash
cp .env.example .env
Open .env and add your API key:

Plaintext
GOOGLE_API_KEY=your_actual_key_here
3. Running the Agent
Bash
python main.py

```
🛠 Project Structure
main.py: The central controller. Contains the LLM logic and agent loop.

tools.py: Contains the search functions and file-saving tools.

.env.example: A template for environment variables.

.gitignore: Security filters for your API keys and local environment.

🛡 License
Distributed under the MIT License.

Developed by Shanon DSouza Building the future of autonomous agents. Feel free to reach out for collaboration!
