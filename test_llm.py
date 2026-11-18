from llm import llm

response = llm.invoke("Explain Python in simple words")

print(response.content)