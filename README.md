# AI Article Generator Project

This project is designed to assist in generating and reviewing articles using AI agents. It leverages tools like AWS Bedrock and LangGraph to streamline the drafting and reviewing process, with a user-friendly interface powered by Streamlit.

## Demo

![Demo](demo.gif)

## Project Structure

```
|-- .gitignore
|-- article_workflow.py
|-- pyproject.toml
|-- state.py
|-- streamlit_app.py
|-- agents/
    |-- __init__.py
    |-- drafting_agent.py
    |-- reviewing_agent.py
```

### Key Files and Directories

- **`article_workflow.py`**: Contains the workflow logic for article generation and review.
- **`pyproject.toml`**: Manages project dependencies and configurations.
- **`state.py`**: Handles the application state and session management.
- **`streamlit_app.py`**: Entry point for the Streamlit application.
- **`agents/`**: Directory containing AI agents:
  - `drafting_agent.py`: Handles article drafting.
  - `reviewing_agent.py`: Handles article review and feedback.

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- Poetry (Python dependency management tool)
- AWS credentials for Bedrock integration

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/manikolbe/ai_article_generator_bedrock_langgraph_reflection-.git
   cd ai_article_generator_bedrock_langgraph_reflection-
   ```

2. Install dependencies using Poetry:

   ```bash
   poetry install
   ```

3. Activate the virtual environment:

   ```bash
   poetry shell
   ```

4. Run the Streamlit app:
   ```bash
   streamlit run streamlit_app.py
   ```

## Features

- **AI Drafting Agent**: Automatically generates article drafts based on user input.
- **AI Reviewing Agent**: Provides detailed reviews and suggestions for improvement.
- **State Management**: Tracks user sessions and workflows.
- **Streamlit Interface**: Easy-to-use web interface for managing the article generation process.

## Future Enhancements

- Support for additional AI models via LangGraph.
- Integration with cloud storage for saving and retrieving drafts.
- Enhanced UI features for better user experience.
