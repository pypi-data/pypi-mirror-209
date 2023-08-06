# hugging-chat-api

English | [简体中文](README_cn.md)

HuggingChat Python API

[![PyPi](https://img.shields.io/pypi/v/hugchat.svg)](https://pypi.python.org/pypi/hugchat)
[![Support_Platform](https://img.shields.io/pypi/pyversions/hugchat)](https://pypi.python.org/pypi/hugchat)
[![Downloads](https://static.pepy.tech/badge/hugchat)](https://pypi.python.org/pypi/hugchat)

Leave a star :)

> When you use this project, it means that you have agreed to the following two requirements of the HuggingChat:  
>
> 1. AI is an area of active research with known problems such as biased generation and misinformation. Do not use this application for high-stakes decisions or advice.  
> 2. Your conversations will be shared with model authors.

## Authentication (Required Now)

### Cookies

<details>
<summary>How to Get Cookies ?</summary>

- Install the `Cookie-Editor` extension for [Chrome](https://chrome.google.com/webstore/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm) or [Firefox](https://addons.mozilla.org/en-US/firefox/addon/cookie-editor/)
- Go to [HuggingChat](https://huggingface.co/chat) and **login**
- Open the extension
- Click `Export` on the bottom right, then `Export as JSON`(This saves your cookies to the clipboard)
- Paste your cookies into a file `cookies.json`

</details>

## Usage

### Basic mode

```bash
pip install hugchat
```

```py
from hugchat import hugchat
chatbot = hugchat.ChatBot(cookie_path="cookies.json")  # or cookies=[...]
print(chatbot.chat("HI"))

# Create a new conversation
id = chatbot.new_conversation()
chatbot.change_conversation(id)

# Get conversation list
conversation_list = chatbot.get_conversation_list()
```

The `chat()` function receives these parameters:

- `text`: Required[str].
- `temperature`: Optional[float]. Default is 0.9
- `top_p`: Optional[float]. Default is 0.95
- `repetition_penalty`: Optional[float]. Default is 1.2
- `top_k`: Optional[int]. Default is 50
- `truncate`: Optional[int]. Default is 1024
- `watermark`: Optional[bool]. Default is False
- `max_new_tokens`: Optional[int]. Default is 1024
- `stop`: Optional[list]. Default is ["</s>"]
- `return_full_text`: Optional[bool]. Default is False
- `stream`: Optional[bool]. Default is True
- `use_cache`: Optional[bool]. Default is False
- `is_retry`: Optional[bool]. Default is False
- `retry_count`: Optional[int]. Number of retries for requesting huggingchat. Default is 5

### CLI mode

> `version 0.0.5.2` or newer

Simply run the following command in your terminal to start the CLI mode

```bash
python -m hugchat.cli
```

Commands in cli mode:

- `/new` : Create and switch to a new conversation.
- `/ids` : Shows a list of all ID numbers and ID strings in current session.
- `/switch <id>` : Switches to the ID number passed.
- `/exit` : Closes CLI environment.

## Disclaimers

This is not an official [Hugging Face](https://huggingface.co/) product. This is a **personal project** and is not affiliated with [Hugging Face](https://huggingface.co/) in any way. Don't sue us.

**Server resources are precious, it is not recommended to request this API frequently.**
