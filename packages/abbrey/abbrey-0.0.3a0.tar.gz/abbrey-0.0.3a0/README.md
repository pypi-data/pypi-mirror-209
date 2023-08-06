### Abbreivation decoder
It's not really smart, but extremely simple.
You need to create a `abbr_file.csv` to provide the definition for each abbreviation in the following format:
```
acronym,detail
[ACR_1],[DETAIL_1]
[ACR_2],[DETAIL_2]
...
``` 

Example:
```
from abbrey import AbbrDecoder

decoder = AbbrDecoder("abbr_file.csv")

input_string = "He is a good pm"
print(decoder.decode_sentence(input_string))
```
Output:
```
He is a good project manager
```