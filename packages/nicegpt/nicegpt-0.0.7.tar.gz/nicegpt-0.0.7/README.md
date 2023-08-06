# nicegpt

A Python package that simplifies the usage of the GPT API by providing a convenient class to manage context-driven instances of GPT models. With nicegpt, you can create instances, change models, and obtain context-driven responses from the GPT model.

## Usage

First, make sure you have run the `config` function to set up your API key and optionally the organization. If you don't have environment variables set up for the key, you need to run this function.

```python
import nicegpt 

nicegpt.config("your_api_key", "your_organization")
```

Next, create a GPT instance using the GPT class. You can choose the GPT model by accessing the Model enum:

```python
gpt_instance = nicegpt.GPT(model=nicegpt.Model.GPT4)
```

Now you can obtain context-driven responses using the response function:

```python
response = gpt_instance.response("What is the capital of France?")
```

Set the `just_reply` parameter to obtain the raw JSON instead of the message. You can also pass additional kwargs to the response function, which will be forwarded to the GPT API:

```python
json_response = gpt_instance.response("What is the capital of France?", just_reply=False, max_tokens=50, temperature=0.8)
```

To change the GPT model, use the change_model function:

```python
gpt_instance.change_model(nicegpt.Model.GPT3_5)
```

To access the message history, use the get_messages function:

```python
message_history = gpt_instance.get_messages()
print(message_history)
```


## License

This project is released under the MIT License.





