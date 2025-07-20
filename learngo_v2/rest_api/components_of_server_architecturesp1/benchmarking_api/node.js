
const cluster = require('cluster');
const http = require('http');
const url = require('url');
const os = require('os');


class Person {
  constructor(name, age) {
    this.name = name;
    this.Age = age; 
  }
}

// http://localhost:8080/person?id=3 for postman
// wrk -t8 -c400 -d30s "http://localhost:8080/person?id=1"
// use wrk will use 8 threads = -t8 , 400 concurrent connections
// -c = concurrent connections , duration = -d
// in terminal monitor with htop
// wrk -t8 -c400 -d30s "http://wifinetworkip:8080/person?id=1"
// take note running wrk on wsl means needing to hit the ip addr of wifi see ipconfig on powershell for details


const personData = {
  "1": new Person("John Doe", 30),
  "2": new Person("John Doe", 28),
  "3": new Person("John Doe", 25),
};


function getPersonHandler(req, res) {
  const parsedUrl = url.parse(req.url, true);
  

  const id = parsedUrl.query.id;

  if (!id || id === "") {
    res.writeHead(400, { 'Content-Type': 'text/plain' });
    res.end('ID is missing');
    return;
  }

  const person = personData[id];
  const exists = person !== undefined;


  if (!exists) {
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('Person not found');
    return;
  }


  res.writeHead(200, { 'Content-Type': 'application/json' }); 

  try {
    res.end(JSON.stringify(person));
  } catch (err) {
    res.writeHead(500, { 'Content-Type': 'text/plain' });
    res.end('Failed to encode response');
  }
}


function main() {
  const port = 8080;
  const numCPUs = os.cpus().length;

  if (cluster.isMaster) {

    console.log(`Server started on port ${port}`);
    console.log(`Master process ${process.pid} using ${numCPUs} CPU cores`);
    console.log(`Starting ${numCPUs} worker processes to match Go's concurrency...`);

    // Fork workers for each CPU core (equivalent to Go's GOMAXPROCS)
    for (let i = 0; i < numCPUs; i++) {
      cluster.fork();
    }

    cluster.on('exit', (worker, code, signal) => {
      console.log(`Worker ${worker.process.pid} died, restarting...`);
      cluster.fork(); // Restart worker if it dies
    });

  } else {
   
    const server = http.createServer((req, res) => {
      const parsedUrl = url.parse(req.url, true);
      
      if (parsedUrl.pathname === "/person") {
        getPersonHandler(req, res);
      } else {
        res.writeHead(404, { 'Content-Type': 'text/plain' });
        res.end('Not found');
      }
    });

   
    server.listen(port, () => {
      console.log(`Worker ${process.pid} listening on port ${port}`);
    });

    server.on('error', (err) => {
      console.error('Server error:', err);
      process.exit(1);
    });
  }
}


main();