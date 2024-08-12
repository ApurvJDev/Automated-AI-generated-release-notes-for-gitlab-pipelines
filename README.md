## This is what the release notes would look like

https://github.com/user-attachments/assets/ed38a767-9f15-49fa-8396-103c19a6bb98

## FOR MORE INFORMATION CHECK OUT THE FOLLOWING LINKS

- https://docs.gitlab.com/ee/development/changelog.html
- https://docs.gitlab.com/ee/api/repositories.html

# Important information regarding model parameters

## model
string -> specifies the model being used

## max_tokens
integer ≥ 1
Defaults to 1024
The maximum number of tokens to generate in any given call. Note that the model is not aware of this value, and generation will simply stop at the number of tokens specified.

## stream
boolean -> Defaults to false
If set, partial message deltas will be sent. Tokens will be sent as data-only server-sent events (SSE) as they become available (JSON responses are prefixed by data: ), with the stream terminated by a data: [DONE] message.

## temperature
number -> 0 to 1
Defaults to 0.5
The sampling temperature to use for text generation. The higher the temperature value is, the less deterministic the output text will be. It is not recommended to modify both temperature and top_p in the same call.

## top_p
number -> 0 to 1
Defaults to 1
The top-p sampling mass used for text generation. The top-p value determines the probability mass that is sampled at sampling time. For example, if top_p = 0.2, only the most likely tokens (summing to 0.2 cumulative probability) will be sampled. It is not recommended to modify both temperature and top_p in the same call.

## stop
A string or a list of strings where the API will stop generating further tokens. The returned text will not contain the stop sequence.

## frequency_penalty
number -> -2 to 2
Defaults to 0
Indicates how much to penalize new tokens based on their existing frequency in the text so far, decreasing model likelihood to repeat the same line verbatim.

## presence_penalty
number -> -2 to 2
Defaults to 0
Positive values penalize new tokens based on whether they appear in the text so far, increasing model likelihood to talk about new topics.

## seed
integer
Defaults to 0
The model generates random results. Changing the input seed alone will produce a different response with similar characteristics. It is possible to reproduce results by fixing the input seed (assuming all other hyperparameters are also fixed).

## messages
required
A list of messages comprising the conversation so far.


## For more information
- https://docs.api.nvidia.com/nim/reference/meta-llama3-70b-infer

- https://platform.openai.com/docs/api-reference/chat/create
