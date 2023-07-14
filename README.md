# chatgpt-export-code-chats
A python script to parse all_conversations.txt (made from conversaions.json) into multiple plain text files that includes all user inputs and AI responses in regards to coding projects.

# Step 0:

Export user data from ChatGPT using this method: 

https://help.openai.com/en/articles/7260999-how-do-i-export-my-chatgpt-history-and-data


# Step 1:

Generate all_conversations.txt from conversations.json with the chat_to_text.py python script found here:

https://github.com/txtatech/chatgpt-export-to-text

# Step 2:

Run the extract_code_chats.py in this repository to extract the code chats from the all_conversations.txt file created in Step 1.

**Note: The script is not incredibly accurate but it does okay at exporting the requested code types.**
