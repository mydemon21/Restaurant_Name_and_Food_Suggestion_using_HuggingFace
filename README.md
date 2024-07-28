# Restaurant_Name_and_Food_Suggestion_using_HuggingFace

This project uses the Hugging Face Transformers library to generate creative restaurant names and menu suggestions based on different cuisines. The application provides a simple web interface using Streamlit for users to interact and generate names and menu items.

## Features

- **Generate Restaurant Names**: Suggests unique and creative restaurant names based on the selected cuisine.
- **Menu Item Suggestions**: Provides a list of potential menu items that match the generated restaurant name.

## Requirements

- Python 3.x
- Libraries:
  - `streamlit`
  - `transformers`

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/mydemon21/Restaurant_Name_and_Food_Suggestion_using_HuggingFace.git
    cd Restaurant_Name_and_Food_Suggestion_using_HuggingFace
    ```

2. **Install dependencies**:

    Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

    Install the required libraries:

    ```bash
    pip install -r requirements.txt
    ```

## Model Description

The application utilizes a text generation model from Hugging Face's Transformers library. Here’s a brief overview of how the model integration works:

1. **Hugging Face Integration**:
    - **Text Generation**: A text generation pipeline is used to generate restaurant names and menu items based on a prompt.
    - **Prompting and Response Handling**: The system sends a prompt to the model and processes the response to extract the restaurant name and menu items.

2. **Process Flow**:
    - **Input Handling**: The user selects a cuisine type via the Streamlit interface.
    - **Generation and Display**: The application uses the model to generate text, which is then parsed to display the restaurant name and menu items.

## Usage

1. **Run the application**:

    ```bash
    streamlit run app.py
    ```

2. **Using the application**:
   - Select a cuisine from the sidebar dropdown.
   - The application will generate and display a restaurant name along with a list of menu items.

## Notes

- Ensure you have a stable internet connection as the Hugging Face model may need to download additional data.
- You may need to adjust settings or paths in the code according to your environment.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

Special thanks to the creators of Streamlit and Hugging Face Transformers for providing powerful tools for building language-based applications.

## Author

Sajal Patel
