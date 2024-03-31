import pandas as pd
from langchain_community.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler


source = pd.read_csv('csv/all_merged.csv')
syllabus = pd.read_csv('csv/syllabus.csv')
llm = Ollama(model = 'llama2', callback_manager = CallbackManager([StreamingStdOutCallbackHandler()]))
