from typing import TypedDict
from langgraph.graph import StateGraph, END
from llm import llm


class StudyState(TypedDict):
    question: str
    answer: str


def study_assistant(state: StudyState):

    question = state["question"]

    prompt = f"""
You are an AI Study Assistant.

Explain the following topic in a simple way for a student.

Topic:
{question}

Give:
1. Simple explanation
2. Important points
3. Example
"""

    response = llm.invoke(prompt)

    return {
        "answer": response.content
    }


workflow = StateGraph(StudyState)

workflow.add_node("study_assistant", study_assistant)

workflow.set_entry_point("study_assistant")

workflow.add_edge("study_assistant", END)

study_graph = workflow.compile()