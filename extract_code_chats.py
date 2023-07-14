import re

# Define a set of regex patterns for each code type.
code_patterns = {
    'html': r'<(html|head|body|title|div|span|p|h[1-6]|a|link|script|style|img|br|ul|ol|li|table|tr|td|th)',
    'js': r'\b(function|var|let|const|if|else|for|while|switch|return|in|of|case|break|default|console.log)\b',
    'rust': r'\b(fn|let|mut|if|else|for|while|loop|match|return|in|println!)\b',
    'system': r'\b(ls|cd|rm|mkdir|touch|sudo|chmod|chown|cp|mv|cat|echo|grep|find|ping|exit|shutdown|reboot)\b',
    'python': r'\b(def|class|if|else|elif|for|while|import|from|as|with|return|print|lambda|try|except|finally|raise|yield)\b',
}

# Open and read the file with all conversations.
with open('all_conversations.txt', 'r') as f:
    conversations = f.read()

# Split the conversations by blank lines.
conversations = conversations.split("\n\n")

# Find conversations that contain code.
code_regex = re.compile(r'\b(for|if|else|while|def|return|import|from|as|class|with)\b')
code_conversations = [conv for conv in conversations if code_regex.search(conv)]

# For each code type, filter the conversations and write them to separate files.
for code_type, pattern in code_patterns.items():
    regex = re.compile(pattern)
    matching_conversations = [conv for conv in code_conversations if regex.search(conv)]

    with open(f'{code_type}_conversations.txt', 'w') as f:
        f.write('\n\n'.join(matching_conversations))
