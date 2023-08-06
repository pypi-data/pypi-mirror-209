### Abbreivation decoder
It's not really smart, but extremely simple.
Example:
```
from abbrey import AbbrDecoder

decoder = AbbrDecoder()

input_string = "He is a good pm"
print(decoder.decode_sentence(input_string))
```
Output:
```
He is a good project manager
```