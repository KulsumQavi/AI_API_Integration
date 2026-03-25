
def get_groq_response(prompt):
    try:
        from groq import Groq
        client = Groq(api_key="")
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Groq Error: {str(e)}"

def get_huggingface_response(prompt):
    try:
        from huggingface_hub import InferenceClient
        client = InferenceClient(api_key="")
        response = client.chat.completions.create(
            model="meta-llama/Meta-Llama-3-8B-Instruct",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"HuggingFace Error: {str(e)}"

def get_cohere_response(prompt):
    try:
        import cohere
        client = cohere.ClientV2(api_key="")
        response = client.chat(
            model="command-a-03-2025",
            messages=[{"role":"user","content":prompt}],
        )
        return response.message.content[0].text
    except Exception as e:
        return f"Cohere Error: {str(e)}"

def get_ollama_response(prompt):
    try:
        import requests
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "tinyllama",
                "prompt": prompt,    
                "stream": False
            }
        )
        data = response.json()
        return data["response"]                   
    except Exception as e:
        return f"Ollama Error: {str(e)}"
PROVIDERS = {
    "1": ("Groq",get_groq_response),
    "2": ("HuggingFace",get_huggingface_response),
    "3": ("Cohere",get_cohere_response),
    "4": ("Ollama",get_ollama_response),
}

def show_menu():
    print("="*50)
    print("MULTI-API AI CHATBOT")
    print("="*50)
    print("Select an AI Provider:\n")
    for key, (name, _) in PROVIDERS.items():
        print(f"{key}. {name}")
    print("5. Exit")
    print("="*50)

def main():

    while True:
        show_menu()
        choice = input("\nEnter choice (1-5):").strip()

        if choice == "5":
            print("Exit\n")
            break

        if choice not in PROVIDERS:
            print("Invalid choice. Please try again.")
            continue

        provider_name, provider_func = PROVIDERS[choice]
        print(f"\nUsing: {provider_name}")

        while True:
            prompt = input("\n  Enter your prompt or'back'to change provider: ").strip()

            if prompt.lower() == "back":
                break

            if not prompt:
                print("Prompt cannot be empty.")
                continue

            print("\n Querying API...")
            print("-" * 50)
            result = provider_func(prompt)
            print("  Response:")
            print(result)
            print("-" * 50)

if __name__ == "__main__":
    main()