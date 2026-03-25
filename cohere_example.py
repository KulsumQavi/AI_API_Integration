import cohere

# Configure API
client = cohere.ClientV2(api_key="TPbKILFM9xOEdR2Si9anLYWpvoAeiqrMsjvDklGF")

def query_api(prompt):
    """Query the AI API with a prompt"""
    try:
        response = client.chat(
            model="command-a-03-2025",
            messages=[{"role": "user", "content": prompt}],
        )
        return response.message.content[0].text
    except Exception as e:
        return f"Error: {str(e)}"

# Main execution
if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    print("Querying API...")
    result = query_api(user_prompt)
    print("Response:")
    print(result)