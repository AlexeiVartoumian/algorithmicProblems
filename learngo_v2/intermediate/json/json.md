lightweight data change format
use encoding json package
`json.Marshal` convert Go data structures into JSON (encoding)
`json.Unmarshal` convert json into Go data structures (decoding)

use struct tags (above) for encoding and decoding 
ommiting fields if emptu (`omitempty`) or always
when making api applicaitons gotta validate and sanitize