# AI Agent Assistant - Technical Challenge 

This project is an AI assistant developed with **LangChain** and **Streamlit**, capable of autonomously deciding when to use external tools to answer user questions.

## Features

- **Intelligent Reasoning**: Uses the GPT-3.5-Turbo model to decide the response flow.
- **Calculator**: A custom tool for precise mathematical operations.
- **NASA API**: Integration to fetch astronomical information and the Astronomy Picture of the Day.
- **Web Interface**: A user-friendly interface built with Streamlit.

## Technologies Used

- **Python**
- **LangChain**
- **LangChain Community** (NASA toolkit)
- **LangChain OpenAI**
- **OpenAI API**
- **Streamlit**
- **python-dotenv**


## Project Structure

```text
AI_Assistant/                         # GitHub repository root
│
├── ai_chatbot/                       # Core application package (business logic)
│   ├── llm/                          # LLM configuration and abstraction
│   │   └── model.py                  # Initializes and configures the LLM
│   │
│   └── tools/                        # Custom tools used by the agent
│       ├── calculator.py             # Local math calculator tool
│       └── nasa.py                   # NASA tool using LangChain NASA toolkit
│
├── app.py                            # Streamlit entry point (UI + agent execution)
├── requirements.txt                  # Project dependencies
├── .env.example                      # Example environment variables (no secrets)
└── README.md                         # Project documentation
```


## How to Run

1. Create a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate   # Linux / macOS
# .venv\Scripts\activate    # Windows
```
2. Install the dependencies:
```bash
   pip install -r requirements.txt
```

3. Environment configuration
- Create a .env file in the project root with the following variables:
```bash
OPENAI_API_KEY=your_openai_api_key
NASA_API_KEY=DEMO_KEY
```
The .env file is intentionally ignored by Git to avoid leaking secrets.

4. Run the application

```bash
streamlit run app.py
```
