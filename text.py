# for i in range(4):
#     print(i)

# print([i for i in range(20, 24+1)])

from langchain_community.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

# Print the answer
llm = Ollama(model = 'llama2', callback_manager = CallbackManager([StreamingStdOutCallbackHandler()]))
conversation_history = ""
while True:
    input_ = input('\ninput:')
    if input_ == 'exit':
        break
    answer = llm.invoke(f'The following is a conversation between a human and an AI. The conversation history is: {conversation_history}\nHuman: {input_}\nAI:')
    conversation_history = conversation_history + f'AI:{answer} Human:{input_}'