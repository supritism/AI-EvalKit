from anthropic import Anthropic

# Initialize the client — it reads ANTHROPIC_API_KEY from your environment automatically
client = Anthropic() # When we create the client with no arguments, the SDK automatically looks for our ANTHROPIC_API_KEY environment variable. This way it keeps secrets out of our source code and GitHub.

# Make your first call
msg = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=200,
    temperature=0.0, # add it only to make the experiment more controlled. 
    messages=[
        {
            "role": "user",
            "content": "In one sentence, what is a large language model?"
        }
    ],
)

# Print the response
print("Model response:")
print(msg.content[0].text)
print()

# Print token usage (this is free info the API gives you)
print("Token usage:")
print(f"  Input tokens: {msg.usage.input_tokens}")
print(f"  Output tokens: {msg.usage.output_tokens}")

# Additional Notes :
# Q1 : Why content[0] ? 
# A1 : The API returns a Message object with a specific structure. msg.content is a LIST of "content blocks". 
#   msg.content[0]  # the first block in the list
#   msg.content[0].text  # the actual text string inside that block. 
# Why a list? Because a single response could contain multiple blocks — text, images, tool calls, etc. 
# In this case, you just got one text response, so you grab [0] (the first and only element).

# Q2 : Was the API actually called? How much did it cost?
# A2 : Yes, the API was called. The cost is based on the number of tokens used in the request and response. 
# You can see the token usage printed in output, which includes input tokens and output tokens. 
# The total cost can be calculated based on the pricing model provided by Anthropic. 
# Cost breakdown (Haiku pricing): 
#   Input: $1 per million tokens
# Output: $5 per million tokens

# Q3 : What is the difference between temperature=0.0 and temperature=1.0?
# A3 : Temperature is a parameter that controls the randomness of the model's output.
#   - A temperature of 0.0 makes the model deterministic, meaning it will always produce the same output for the same input. 
# This is useful for tasks where you want consistent results.
#   - A temperature of 1.0 makes the model more random, meaning it will produce different outputs for the same input. 
# This is useful for creative tasks where you want to explore different possibilities.
