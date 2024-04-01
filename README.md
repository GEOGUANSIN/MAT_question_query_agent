
#Development phase 


### Phase 1, Data preparation:

1. extraction and structuralized MAT questions and solutions - multiple choice only
2. use LLM to add necessary feature analysis - type of question 
3. store data for retrieval - in csv at the moment 
4. SQL-based RAG base

### Phase 2, Chat-agent interaction design

(step 0: user profile and engine selection:)

**step 1: topic selection**

topic_selection:

Which topic to select for the question?
Content-of-main-topics
Context-of-sub-topics

PM + agent_design + UI design to indicate the next phase

**step 2: question presentation**

UI: a new interface where questions are posted and user is allowed to give input.
when input is given, even when it is right, explanation from the user is required.

hint building:
When user is not right, give some hint to the user

**step 3: answer presentation**

answer:
When user is right or upon request, give the answer to the user.
evaluation and documentation:
When user is right, give the evaluation of the user's answer.
explanation:

(step 4: further extension)

consider_similar_questions: be careful of the machine's problem
the user could choose to take the question, or to proceed to the next question.

### Phase 3, user-interface design and deployment

- gradio
