import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

# -------------------- Prompt loading functions --------------------

def upload_system_prompt(chemin="prompts/system_prompt.txt"):
    """
        Load the system prompt from a given file path.

        Args:
            chemin (str): Path to the system prompt file. Default is "prompts/system_prompt.txt".
        Returns:
            str: Contents of the system prompt file.
        Raises:
            Exits program if the file cannot be read.
    """
    try:
        with open(chemin, encoding="utf-8") as f:
            return f.read()
    except Exception:
        print("Erreur de lecture du prompt système. Vérifie le fichier system_prompt.txt.")
        exit(1)

def upload_user_prompt(num):
    """
       Load a user prompt given the prompt number.

       Args:
           num (str): Number identifying which user prompt file to load.
       Returns:
           str: Contents of the selected user prompt file.
       Behavior:
           If the specified user prompt file does not exist,
           loads a default user_1.txt prompt file.
    """
    chemin = f"prompts/user_{num}.txt"
    try:
        with open(chemin, encoding="utf-8") as f:
            return f.read()
    except Exception:
        print(f"Prompt utilisateur {chemin} non trouvé. Utilisation de user_1.txt par défaut.")
        with open("user_1.txt", encoding="utf-8") as f:
            return f.read()

def select_prompt():
    """
        Ask the user to choose which user prompt to use and load the selected prompt.

        Returns:
            tuple: (chosen prompt number as str, system prompt content, user prompt content)
    """
    print("Choisissez le prompt utilisateur :")
    fichiers = ["1", "2", "3", "4"]
    for num in fichiers:
        print(f"{num}: prompt utilisateur dans user_{num}.txt")
    choix = input("Numéro du prompt (ex : 1) : ").strip()
    if choix not in fichiers:
        print("Choix invalide, utilisation de user_1.txt.")
        choix = "1"
    system_prompt = upload_system_prompt()
    user_prompt = upload_user_prompt(choix)
    return choix, system_prompt, user_prompt

# -------------------- File reading and writing functions --------------------

def read_txt_file(path):
    """
        Read the content of a text file.

        Args:
            path (str): Path to the text file to read.
        Returns:
            str: Contents of the text file.
        Raises:
            Exits the program if the file cannot be read.
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {e}")
        exit(1)

def save_xml_file(path, content):
    """
        Save string content to a file.

        Args:
            path (str): Path where the XML content will be saved.
            content (str): String content to be written to the file.
        Raises:
            Exits the program if the file cannot be saved.
    """
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
    except Exception as e:
        print(f"Erreur lors de la sauvegarde du fichier : {e}")
        exit(1)

# -------------------- LLM API call function --------------------

def mistral_request(messages, temperature=0.0, model="mistral-large-latest", random_seed=42):
    """
        Make a chat completion request to the Mistral API.

        Args:
            messages (list): List of message dicts with roles ("system", "user") and content.
            temperature (float): Sampling temperature for the generation.
            model (str): Model identifier to use.
            random_seed (int): Random seed to use to have the same output everytime.
        Returns:
            str: Generated content from the model.
        Raises:
            Exits the program if the API call fails.
    """
    url = "https://api.mistral.ai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": 2500,
        "random_seed": random_seed
    }
    try:
        response = requests.post(url, headers=headers, json=data, timeout=120)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"Erreur API Mistral : {e}")
        exit(1)

# -------------------- MAIN PROGRAM --------------------

def main():
    """
        Main program execution function.

        Asks the user for a text file to annotate, selects prompts,
        sends the request to the Mistral API, and saves the XML response to a file.
    """
    fichier_entree = input("Chemin du fichier TXT à annoter : ").strip()
    texte = read_txt_file(fichier_entree)
    choix_prompt, system_prompt, user_prompt = select_prompt()

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt + "\n" + texte}
    ]

    try:
        xml_result = mistral_request(messages)
        model_name = "mistral"
        output_filename = f"{model_name}_{choix_prompt}_annotation.xml"
        save_xml_file(output_filename, xml_result)
        print(f"Annotation XML sauvegardée dans {output_filename}")
    except Exception as e:
        print(f"Erreur Mistral : {e}")
        exit(1)

if __name__ == "__main__":
    main()
