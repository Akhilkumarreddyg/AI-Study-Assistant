from graph import study_graph

result = study_graph.invoke(
    {
        "question": "What is Machine Learning?",
        "answer": ""
    }
)

print(result["answer"])