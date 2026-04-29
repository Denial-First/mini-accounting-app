# Prompt History Overview
Here is short explanation of conversation with chatGPT. If you want to see the full chat, you can follow the link:
```
https://chatgpt.com/share/69f28638-7768-83eb-887c-166fcbbdda0c
```

If you have questions about difference between code and chatGPT generated, I also used streamlit documentation and wrote some code on my own.

## Prompts explanation

### 1. First analyzing message

Goal: Setting up LLM on conversation about this task, sent data for analysis

Message: Whole task from readme file on task repo.

Result: Structured overview of sent task, implemented solution after that.

### 2. Understanding written code

Goal: I want to understand part of code by asking LLM to explain that part.

Message: "{specified output} what this output means"

Result: Explained output, so I can move further.

### 3. Correcting implemented solution

Goal: Making solution more appropriate to the specified task.

Message: "add navigation fields with names like 'pay transaction' and 'receive transaction'. Create buffer where money are saved before receiving transaction"

Result: Code with specified corrections

### 4. Explanation of tasks' part

* 1000 postings

Goal: Understanding what 1000 postings mean

Message: "what is sense of 1000 - cash. Can I just leave receivable, payable, revenue and expense?"

Result: Explained sense of 1000 - cash postings.

* 1100 and 2000 postings

Goal: Simplifying Accounts Receivable (AR) and Accounts Payable (AP) logic

Message: "on sale is just ar+100, on receiving revenue +100 and ar -100?"

Result: Explanation why it is impossible and how it would break the app.

### 5. Trying to remove is_debit field in postings class

Goal: Rewrite solution without is_devit field in Posting class and replacing missing logic with negative values if needed.

Message: "can I replace "is_debit" field by negative amount values?"

Result: Explaining pros and cons of implementing this, but not implementing in appropriate way.

### 6. Help with streamlit

Goal: Some hints on how to work with streamlit: working with columns, changing text color.

Messages: Short messages to reach specific goal.

Result: Code I needed to understand how some streamlit parts work

