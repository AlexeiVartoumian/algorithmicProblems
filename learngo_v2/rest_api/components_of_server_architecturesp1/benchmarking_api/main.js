// 
// 
// class Person {
//   constructor(name, age) {
//     this.name = name;
//     this.Age = age; // Matching Go's capitalized field name
//   }
// }

// // http://localhost:8080/person?id=3 for postman
// // wrk -t8 -c400 -d30s "http://localhost:8080/person?id=1"
// // use wrk will use 8 threads = -t8 , 400 concurrent connections
// // -c = concurrent connections , duration = -d
// // in terminal monitor with htop
// // wrk -t8 -c400 -d30s "http://wifinetworkip:8080/person?id=1"
// // take note running wrk on wsl means needing to hit the ip addr of wifi see ipconfig on powershell for details

// 
// const personData = {
//   "1": new Person("John Doe", 30),
//   "2": new Person("John Doe", 28),
//   "3": new Person("John Doe", 25),
// };

// 
// function getPersonHandler(req) {
//   const url = new URL(req.url);
  
//   
//   const id = url.searchParams.get("id");

//   if (!id || id === "") {
//     return new Response("ID is missing", { status: 400 });
//   }

//   const person = personData[id];
//   const exists = person !== undefined;

//   
//   if (!exists) {
//     return new Response("Person not found", { status: 404 });
//   }

//   
//   try {
//     return new Response(JSON.stringify(person), {
//       headers: {
//         "Content-Type": "application/json", // Fixed typo from Go code
//       },
//     });
//   } catch (err) {
//     return new Response("Failed to encode response", { status: 500 });
//   }
// }

// 
// function main() {
//   const port = 8080;

//   console.log(`Server started on port ${port}`);

//   
//   const server = Bun.serve({
//     port: port,
//     fetch(req) {
//       const url = new URL(req.url);
      
//       if (url.pathname === "/person") {
//         return getPersonHandler(req);
//       }
      
//       return new Response("Not found", { status: 404 });
//     },
//   });

//   return server;
// }


// main();


import { spawn } from "bun";
import os from "os";

const numCPUs = os.cpus().length;


class Person {
  constructor(name, age) {
    this.name = name;
    this.Age = age;
  }
}

const personData = {
  "1": new Person("John Doe", 30),
  "2": new Person("John Doe", 28),
  "3": new Person("John Doe", 25),
};


function getPersonHandler(req) {
  const url = new URL(req.url);
  const id = url.searchParams.get("id");

  if (!id || id === "") {
    return new Response("ID is missing", { status: 400 });
  }

  const person = personData[id];
  const exists = person !== undefined;

  if (!exists) {
    return new Response("Person not found", { status: 404 });
  }

  try {
    return new Response(JSON.stringify(person), {
      headers: {
        "Content-Type": "application/json",
      },
    });
  } catch (err) {
    return new Response("Failed to encode response", { status: 500 });
  }
}


const isWorker = process.env.WORKER_ID !== undefined;

if (!isWorker) {
 
  console.log(`Master process ${process.pid} is running`);
  console.log(`Number of CPUs: ${numCPUs}`);
  console.log(`Starting ${numCPUs} Bun worker processes...`);

  const workers = [];
  
  for (let i = 0; i < numCPUs; i++) {
    const worker = spawn({
      cmd: ["bun", "run", import.meta.path],
      env: {
        ...process.env,
        WORKER_ID: i.toString(),
        PORT: (8080 + i).toString(), // Each worker gets its own port
      },
      stdio: ["inherit", "inherit", "inherit"],
    });
    
    workers.push(worker);
    console.log(`Started worker ${i} on port ${8080 + i}`);
  }

  
  process.on('SIGINT', () => {
    console.log('\nShutting down workers...');
    workers.forEach(worker => worker.kill());
    process.exit(0);
  });

} else {
  
  const workerId = parseInt(process.env.WORKER_ID);
  const port = parseInt(process.env.PORT);

  console.log(`Worker ${workerId} (PID: ${process.pid}) starting on port ${port}`);

  const server = Bun.serve({
    port: port,
    fetch(req) {
      const url = new URL(req.url);
      
      if (url.pathname === "/person") {
        return getPersonHandler(req);
      }
      
      return new Response("Not found", { status: 404 });
    },
  });

  console.log(`Worker ${workerId} started on port ${port}`);
}