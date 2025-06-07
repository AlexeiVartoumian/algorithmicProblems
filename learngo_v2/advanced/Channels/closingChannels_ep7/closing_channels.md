
closing channels

why close? 
- signal completion
- prevent resource elaks


best prac for closing channels
- close channles only from the sender
- avoid closing channels more than once -> causes runtime panic
- avoid closing channels from multiple gorotuintes

common patterns for closing channels
- pipeline pattern
- worker pool pattern 
- debugging + troubleshooting channel Closures
- identify clsoing channel error  
- use.sync.WaitGroup for co-ordinations 