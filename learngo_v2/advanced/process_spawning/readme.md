
process spawning
-refers to creating + managing separte opertating system process from witihin a go programm

this involves starting new processes to run tasks 
concurrently or in isolaiton form the main program

why use prcoess spawning ?
- concurrency/parallelism -> process spawning can be used in a parallel fashion utlizing multiple cores
- isolation -> execute tasks in separate environments to avoid intefrence 
- resource management -> offlaod resource intensive taks to seprate processes

for process spawning we use the os/exec package provided by go , can execute external commands

os/exec package
- exec.Command
- cmd.Stdin /cmd.Stdout
- cmd.Start /cmd.Wait
- cmd.Output

when to use
- resource intensive tasks 
offload heavy operations or I/O to spawning processes

- isolation : execute commands or scripts  diff environments that need diff permissions then those can use excec.command

- concurrency
utlize multiple processes to parrallelize tasks or handle simultaneous requests use exec.Command

- overhead in creating + managing processes
monitor system limits on number of processes and resource usage

excellent technique for executing external commands
and integrating them to go applications

os/exec prvideds fleixble plus robust ways to start and maange external processes to handle input and capture results.

understanding how to use exec command pipes and other functionalities allows to enahcen apps with features such as 

- invoking shell commmands
- processing data with xternal tools
- automating system tasks
