
embed directive 
embedding static files and directories in go binaries at BUILD TIME
-> files cannot be modified at runtime , binary will have to be rebuilt

simleifies deployent for number of files to manage 

noi need to worry about file paths and dependenccies

supports individual files and directories -> anything can be embedded
not a command but a directive

web servers that serve static content i.e html css javascript files
building command-line tools that require configuration files

Real-world examples:
kubectl embeds OpenAPI schemas for validation
helm embeds default chart templates
docker-compose has embedded validation schemas
terraform providers embed resource schemas
