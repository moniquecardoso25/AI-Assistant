# AI Agent Assistant - Technical Challenge 🚀

This project is an AI assistant developed with **LangChain** and **Streamlit**, capable of autonomously deciding when to use external tools to answer user questions.

## 🛠️ Features

- **Intelligent Reasoning**: Uses the GPT-3.5-Turbo model to decide the response flow.
- **Calculator**: A custom tool for precise mathematical operations.
- **NASA API**: Integration to fetch astronomical information and the Astronomy Picture of the Day.
- **Web Interface**: A user-friendly interface built with Streamlit.

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



## 🚀 How to Run

1. Install the dependencies:
   ```bash
   pip install -r requirements.txt
