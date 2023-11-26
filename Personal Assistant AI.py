from openai import OpenAI
client = OpenAI(api_key="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")


# Assistants can call OpenAI's models with specific instructions.
# Assistants can access OpenAI's hosted tools - Code Interpreter & Knowledge retrieval 
# and tools you build via Function Calling.
# The code below is to create the personal assistant.

persassistant = client.beta.assistants.create(
    name = "Math tutor",
    instructions = "You are a personal math tutor. Write and run code to answer math questions",
    tools = [{"type": "code_interpreter"}],
    model = "gpt-3.5-turbo-1106"
)

# Inside of an assistant, there are several threads. Inside threads, messages are running
# between the assistant and the user.
# The code below is to create the thread.

thread = client.beta.threads.create()
print(thread)

# Creating the message that can be added to the thread.

message = client.beta.threads.messages.create(
# thread_id is where the message is linked, provide role of user, content of message.
    thread_id = thread.id,
    role = "user",
    content = "solve this problem: 3x +11 = 14"

)

print(message)

# The code below is to run the assistant.

run = client.beta.threads.runs.create(
# To run, we have to use two parameters; Thread ID and Assistant ID.
   thread_id= thread.id,
   persassistant_id =  persassistant.id
)

# Displaying the response of the Assistant.
# To display this, we need to retrive the message from the thread.

run = client.beta.threads.runs.retrieve(
    thread_id= thread.id,
    run_id = run.id
)

# Retrieve all messages inside this run.
messages = client.beta.thread.messages.list(
    thread_id = thread.id
)

# Print out all messages sent from the assistant.
# We are doing reversed as we want to print out user messages first.

for message in reversed(messages.data):
    print(messages.role + ": "+ message.content[0].text.value) 