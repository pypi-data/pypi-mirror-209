<img src="repo_assets/logo.png" alt="GPT-Code logo" width=240 />

An open source implementation of OpenAI's ChatGPT [Code interpreter](https://openai.com/blog/chatgpt-plugins#code-interpreter).

Simply ask the OpenAI model to do something and it will generate & execute the code for you.

## Installation

Open a terminal and run:

```
$ pip install gpt-code-ui
$ gptcode
```

## User interface
<img src="repo_assets/screenshot.png" alt="GPT-Code logo" width="100%" />
 
## Features
- File upload
- File download
- Context insertion (it can refer to your previous messages)
- Generate code
- Run code (Python kernel)
- Model switching (GPT-3.5 and GPT-4)

## More information
Read the [blog post](https://ricklamers.io/posts/gpt-code) to find out more.

## Misc.
### Using .env for OpenAI key
You can put a .env in the root of the repository directory to load the `OPENAI_API_KEY` environment variable.