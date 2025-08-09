

best practis

- all inputs are potentnially harmful
- use establishedd libraries for sanitizations
sanitiza at multiple layers
contextual escaping
regurlarly update

- common pitfalls
- relying solely on client side sanitization
- incomplete sanitizatiojn , eg all enrtry points -> wrong santization method eg html esacping for javsacript contexts
- regularly updating 
striiping too many characters  
neglecting output snaitzaation
over-sanitization

exxamples
preventing sql injection
preventing xss
preventing url injection


bluemonday is an example of a library