import ollama


def calculator(expression: str) -> str:
    """Evaluate a basic arithmetic expression."""
    allowed = set("0123456789+-*/(). ")

    if not expression or not all(char in allowed for char in expression):
        return "Error: Only basic arithmetic is supported."

    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return str(result)
    except (SyntaxError, ZeroDivisionError, TypeError, OverflowError):
        return "Error: Invalid arithmetic expression."


def main():
    print("Local AI Assistant")
    print("Ask a question, or type 'quit' to exit.\n")

    while True:
        question = input("You: ").strip()

        if question.lower() == "quit":
            break

        response = ollama.chat(
            model="llama3.1:8b",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a helpful, general-purpose AI assistant. "
                        "Answer the user's questions clearly and directly. "
                        "For arithmetic questions that require calculation, "
                        "use the calculator tool. For other questions, answer "
                        "normally without using a tool. Do not claim to have "
                        "used a tool unless you actually used it."
                    ),
                },
                {"role": "user", "content": question},
            ],
            tools=[
                {
                    "type": "function",
                    "function": {
                        "name": "calculator",
                        "description": "Calculate a basic arithmetic expression.",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "expression": {
                                    "type": "string",
                                    "description": (
                                        "Arithmetic expression, such as "
                                        "(25 * 4) + 10"
                                    ),
                                }
                            },
                            "required": ["expression"],
                        },
                    },
                }
            ],
        )

        if response.message.tool_calls:
            for tool_call in response.message.tool_calls:
                if tool_call.function.name == "calculator":
                    expression = tool_call.function.arguments["expression"]
                    result = calculator(expression)
                    print(
                        f"[Python calculator executed: "
                        f"{expression} = {result}]"
                    )

                    response = ollama.chat(
                        model="llama3.1:8b",
                        messages=[
                            {"role": "user", "content": question},
                            response.message,
                            {
                                "role": "tool",
                                "name": "calculator",
                                "content": result,
                            },
                        ],
                    )
                    break

        print(f"Assistant: {response.message.content}\n")


if __name__ == "__main__":
    main()
