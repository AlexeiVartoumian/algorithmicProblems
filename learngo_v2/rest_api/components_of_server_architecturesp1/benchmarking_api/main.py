
import asyncio
import json
import multiprocessing
import os
from dataclasses import dataclass
from typing import Dict

from aiohttp import web


@dataclass
class Person:
    name: str
    Age: int  

# http://localhost:8080/person?id=3 for postman
# wrk -t8 -c400 -d30s "http://localhost:8080/person?id=1"
# use wrk will use 8 threads = -t8 , 400 concurrent connections
# -c = concurrent connections , duration = -d
# in terminal monitor with htop
# wrk -t8 -c400 -d30s "http://wifinetworkip:8080/person?id=1"
# take note running wrk on wsl means needing to hit the ip addr of wifi see ipconfig on powershell for details


person_data: Dict[str, Person] = {
    "1": Person(name="John Doe", Age=30),
    "2": Person(name="John Doe", Age=28),
    "3": Person(name="John Doe", Age=25),
}


async def get_person_handler(request):
  
    id_param = request.query.get('id')
    
    if not id_param or id_param == "":
        return web.Response(text="ID is missing", status=400)
    
    person = person_data.get(id_param)
    exists = person is not None
    
    
    if not exists:
        return web.Response(text="Person not found", status=404)
    
   
    try:
        
        person_dict = {"name": person.name, "Age": person.Age}
        response_text = json.dumps(person_dict)
        return web.Response(
            text=response_text,
            content_type="application/json"  
        )
    except Exception as err:
        return web.Response(text="Failed to encode response", status=500)


async def run_worker():
    port = 8080
    
    print(f"Worker {os.getpid()} listening on port {port}")
    
    app = web.Application()
    
    
    app.router.add_get('/person', get_person_handler)
    
    runner = web.AppRunner(app, access_log=None)
    await runner.setup()
    
    
    site = web.TCPSite(
        runner, 
        '0.0.0.0', 
        port,
        reuse_port=True,  
        reuse_address=True
    )
    
    try:
        await site.start()
        
        await asyncio.Future()
    except Exception as err:
        print(f"Server error: {err}")
        await runner.cleanup()
        exit(1)

def worker_process():
    
    asyncio.run(run_worker())

def main():
    """main function equivalent with clustering like Node.js"""
    port = 8080
    num_cpus = multiprocessing.cpu_count()
    
    print(f"Server started on port {port}")
    print(f"Master process {os.getpid()} using {num_cpus} CPU cores")
    print(f"Starting {num_cpus} worker processes to match Go's concurrency...")
    
    processes = []
    
    try:
     
        for i in range(num_cpus):
            process = multiprocessing.Process(target=worker_process)
            process.start()
            processes.append(process)
            print(f"Started worker process {i}: PID {process.pid}")
        
        
        for process in processes:
            process.join()
            
    except KeyboardInterrupt:
        print("\nShutting down workers...")
        for process in processes:
            process.terminate()
            process.join()
    except Exception as err:
        print(f"Error: {err}")
        for process in processes:
            process.terminate()
            process.join()


if __name__ == "__main__":
    main()