from config.llm import generate_response
from tools.calculator import calculate
from tools.task_manager import (
    add_task,
    list_tasks,
    delete_task
)
from modes.extractor import extract_info


class Agent:

    def __init__(self, memory):
        self.memory = memory

    def process(self, user_input):

        try:

            if user_input.startswith("/extract"):

                data = user_input.replace("/extract", "").strip()

                response = extract_info(data)

                self.memory.add("user", user_input)
                self.memory.add("assistant", response)

                return response

            if user_input.lower().startswith("calculate"):

                expression = user_input.replace(
                    "calculate",
                    ""
                ).strip()

                response = str(
                    calculate(expression)
                )

                self.memory.add("user", user_input)
                self.memory.add("assistant", response)

                return response

            if user_input.startswith("/task add"):

                task = user_input.replace(
                    "/task add",
                    ""
                ).strip()

                response = add_task(task)

                self.memory.add("user", user_input)
                self.memory.add("assistant", response)

                return response

            if user_input.startswith("/task list"):

                response = list_tasks()

                self.memory.add("user", user_input)
                self.memory.add("assistant", response)

                return response

            if user_input.startswith("/task delete"):

                index = int(
                    user_input.split()[-1]
                )

                response = delete_task(index)

                self.memory.add("user", user_input)
                self.memory.add("assistant", response)

                return response

            history = self.memory.get_history()

            context = ""

            for item in history:
                context += (
                    f"{item['role']}: "
                    f"{item['content']}\n"
                )

            prompt = f"""
Previous Conversation:

{context}

Current User Message:

{user_input}
"""

            response = generate_response(prompt)

            self.memory.add("user", user_input)
            self.memory.add("assistant", response)

            return response

        except Exception as e:

            return f"Error: {str(e)}"