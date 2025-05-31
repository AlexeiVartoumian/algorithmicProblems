
cool to use for temp storage duirng program execution

uses the os.CreateTemp function

creats temp files in the default locations

this will be root tmp in unix directories

cautious with tempfiles w. sensitive data


practical applications -> BECAREFUL FOR PLATFORM SPECIFIC DIRECOTY NAMING
- file processing -> i.e file uploads where data needs temporary storage before being processed
- testing 
- caching -> caching computing results or intermediate results