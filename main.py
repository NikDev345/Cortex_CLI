from agent.memory import Memory
from agent.agent import Agent

memory = Memory()

agent = Agent(memory)

print("\nMini AI Agent Started")
print("Type 'exit' to quit\n")

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    response = agent.process(user_input)

    print("\nAI:", response)
    print()