
templates are executd by applying them to structures knwon as tempalte data.
can be structs slices or maps or any custom types that are defined
templates have two packages html/template and text/template

features usecases
Actions
    -variable insertion: {{.FieldName}}
    -Pipelines{{functionName .FieldName}}
    -Control Structures: {{if .Condition}}... {{else}} ... {{end}}
    -Iteration: {{range .Slice}} ... {{end}}
Advanced Features
    -Nested Template: {{template "name" .}}
    -Functions
    -Custom Delimiters
    -Error Handling: tempalte.Must

USE Cases: great for outputting structured text
HTML Generation
Email tempaltes
Code Generation
DOcument generation

best prac 
separation of Concerns
efficiency
security