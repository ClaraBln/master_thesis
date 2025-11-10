# Automatic Text Encoding in XML-TEI Using Large Language Models

This project explores the integration of Large Language Models (LLMs) with XML-TEI for automating text encoding processes in digital humanities research. The objective is to enhance the efficiency, accuracy, and scalability of encoding scholarly texts, specifically focusing on annotations in the TEI (Text Encoding Initiative) format.

## About the Project

This ongoing research, part of my master’s thesis, investigates how advanced AI technologies can support scholarly work in digital humanities. The project revolves around automating the creation of TEI-XML annotations from imperfect digitized texts, using prompts guided by LLMs such as ChatGPT, Gemini, Mistral, and Claude. The aim is to reduce manual effort and improve the consistency of text markup, which is otherwise labor-intensive.

## Specific Repository Content

This repository presents the script to interact with the Mistral API for automatic XML-TEI encoding of text. The script automates prompt submission and annotation retrieval using Mistral’s model. The other LLMs (ChatGPT, Gemini, Claude) will be tested directly via their respective user interfaces, outside of this repository.

This repository includes a sample of my corpus stored in `plain_text.txt`, which I use for testing and evaluating prompts behavior.

## Objectives

- Automate the annotation process for digital texts in TEI format.
- Develop effective prompt strategies for guiding LLMs.
- Evaluate and compare LLM performance on TEI-encoded texts.
- Use API automation with Python for reproducibility and efficiency.
- Analyse the data using Tableau

## Technologies Used

- Python
- Large Language Models (ChatGPT, Gemini, Mistral, Claude)
- LLM APIs
- XML & TEI standards
- Tableau

## Getting Started

Installation

1. Clone this repository:

```
git clone https://github.com/ClaraBln/master_thesis.git
cd master_thesis
```


2. Install dependencies

```
pip install -r requirements.txt
```

3. Create a `.env` file in the root folder with your API key:

```
MISTRAL_API_KEY=your_mistral_api_key
```

## Usage

Configure your Mistral API key in the  .env  file or config script. Run the encoding script as follows:

```
python main.py --input plain_text.txt --output encoded_text.xml
```

## Configuration

Make sure you obtain and set environment variables for:

- `MISTRAL_API_KEY`: Your Mistral AI API key.


## Contributing

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request. Follow best practices for prompt design and API interactions for consistency.

## License

This project is licensed under the MIT License.  
See the [LICENSE](LICENSE) file for details.

## Contact

Clara Blanchard - clara.blanchard@etu.unistra.fr
