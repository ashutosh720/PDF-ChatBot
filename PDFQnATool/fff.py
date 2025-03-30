import openai

# Set your OpenAI API key (Replace with your actual API key)
openai.api_key = "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"


# Function to test OpenAI API response
def test_openai_response():
    try:
        # Send a prompt to the OpenAI API for response
        response = openai.Completion.create(
            engine="text-davinci-003",  # Choose the model you want to use (e.g., 'davinci', 'curie', etc.)
            prompt="Hello, how are you today?",  # Example prompt
            max_tokens=50  # Limit the number of tokens in the response
        )

        # Print the response
        print("OpenAI API Response:")
        print(response.choices[0].text.strip())  # Extract and print the generated text
    except openai.error.RateLimitError as e:
        print("Error: Rate limit exceeded. Please try again later.")
    except openai.error.AuthenticationError as e:
        print("Error: Authentication failed. Please check your API key.")
    except openai.error.OpenAIError as e:
        print(f"OpenAI API Error: {e}")


# Run the test
test_openai_response()
