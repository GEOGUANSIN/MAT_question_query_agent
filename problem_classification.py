import pandas as pd
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate

model = Ollama(model="mistral", callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]))
prompt = ChatPromptTemplate.from_template("given the question and the solution, judge if it is relevant to {topic}.\n "
                                          "{question_solution} \n\n if it is relevant to {topic}, give a simple yes "
                                          "otherwise give a no. Do not explain.")


classification_chain = prompt | model


def classify_qs(question_solution_):
    print(f"Question: {question_solution_}")
    syllabus = pd.read_csv('csv/syllabus.csv')
    topics = syllabus['main_topic'].tolist()
    answer_ = {}
    for topic in topics:
        print(f"Topic: {topic}")
        a = classification_chain.invoke({"topic": topic, "question_solution": question_solution_})
        print(f'a:{a[:3]}')
        if a[1:4] == 'yes' or a[1:4] == 'Yes':
            answer_[topic] = [1]
        elif a[1:3] == 'no' or a[1:3] == 'No':
            answer_[topic] = [0]
        else:
            answer_[topic] = [-1]
        print(f"Answer: {answer_}")
    return answer_


answer_df = pd.DataFrame()
source = pd.read_csv('csv/all_merged.csv')
for index, row in source.iterrows():
    # if index > 2:
    #     break
    question_solution = f"Question = '''{row['question']}'''" + '\n\n' + f"Solution = '''{row['solution']}'''"
    answer = classify_qs(question_solution)
    answer['question_number'] = [row['question_number']]
    answer['paper_name'] = [row['paper_name']]
    print(f'answer: {answer}')
    temp_df = pd.DataFrame(answer)
    answer_df = pd.concat([answer_df, temp_df])

answer_df = answer_df.reset_index(drop=True)
answer_df.to_csv('csv/classified.csv')



