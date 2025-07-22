// // package main

// // import (
// // 	"encoding/json"
// // 	"fmt"
// // 	"log"
// // 	"net"
// // 	"net/http"
// // 	"runtime"
// // 	"sync"
// // )

// // type Person struct {
// // 	Name string `json:"name"`
// // 	Age  int32  `json:"Age"`
// // }

// // var personData = map[string]Person{
// // 	"1": {Name: "John Doe", Age: 30},
// // 	"2": {Name: "John Doe", Age: 28},
// // 	"3": {Name: "John Doe", Age: 25},
// // }

// // func getPersonHandler(w http.ResponseWriter, r *http.Request) {
// // 	id := r.URL.Query().Get("id")

// // 	if id == "" {
// // 		http.Error(w, "ID is missing", http.StatusBadRequest)
// // 		return
// // 	}

// // 	person, exists := personData[id]

// // 	if !exists {
// // 		http.Error(w, "Person not found", http.StatusNotFound)
// // 		return
// // 	}

// // 	w.Header().Set("Content-Type", "application/json")

// // 	if err := json.NewEncoder(w).Encode(person); err != nil {
// // 		http.Error(w, "Failed to encode response", http.StatusInternalServerError)
// // 	}
// // }

// // func handleConn(conn net.Conn, handler http.Handler) {
// // 	defer conn.Close()

// // 	// Serve HTTP on this connection using the standard HTTP server
// // 	http.Serve(&singleConnListener{conn: conn}, handler)
// // }

// // // Custom listener that serves a single connection
// // type singleConnListener struct {
// // 	conn net.Conn
// // 	once sync.Once
// // }

// // func (l *singleConnListener) Accept() (net.Conn, error) {
// // 	var conn net.Conn
// // 	l.once.Do(func() {
// // 		conn = l.conn
// // 	})
// // 	if conn != nil {
// // 		return conn, nil
// // 	}
// // 	// Return error after first connection to stop serving
// // 	return nil, fmt.Errorf("listener closed")
// // }

// // func (l *singleConnListener) Close() error {
// // 	return l.conn.Close()
// // }

// // func (l *singleConnListener) Addr() net.Addr {
// // 	return l.conn.LocalAddr()
// // }

// // func startAcceptLoop(listener net.Listener, handler http.Handler, loopID int) {
// // 	fmt.Printf("Accept loop %d started\n", loopID)

// // 	for {
// // 		conn, err := listener.Accept()
// // 		if err != nil {
// // 			log.Printf("Accept loop %d error: %v", loopID, err)
// // 			continue
// // 		}

// // 		// Handle each connection with HTTP server
// // 		go handleConn(conn, handler)
// // 	}
// // }

// // func main() {
// // 	port := 8080
// // 	numAcceptLoops := runtime.NumCPU() // One accept loop per CPU

// // 	fmt.Printf("Server starting on port %d with %d accept loops\n", port, numAcceptLoops)

// // 	// Set up HTTP handler
// // 	mux := http.NewServeMux()
// // 	mux.HandleFunc("/person", getPersonHandler)

// // 	// Create ONE listener, but multiple accept loops
// // 	listener, err := net.Listen("tcp", fmt.Sprintf(":%d", port))
// // 	if err != nil {
// // 		log.Fatal(err)
// // 	}

// // 	// Start multiple accept loops on the SAME listener
// // 	for i := 0; i < numAcceptLoops; i++ {
// // 		go startAcceptLoop(listener, mux, i)
// // 	}

// // 	fmt.Printf("All %d accept loops started on same listener\n", numAcceptLoops)

// // 	// Keep main goroutine alive
// // 	select {}
// // }

// package main

// import (
// 	"encoding/json"
// 	"fmt"
// 	"log"
// 	"net"
// 	"net/http"
// 	"runtime"
// )

// type Person struct {
// 	Name string `json:"name"`
// 	Age  int32  `json:"Age"`
// }

// var personData = map[string]Person{
// 	"1": {Name: "John Doe", Age: 30},
// 	"2": {Name: "John Doe", Age: 28},
// 	"3": {Name: "John Doe", Age: 25},
// }

// func getPersonHandler(w http.ResponseWriter, r *http.Request) {
// 	id := r.URL.Query().Get("id")

// 	if id == "" {
// 		http.Error(w, "ID is missing", http.StatusBadRequest)
// 		return
// 	}

// 	person, exists := personData[id]

// 	if !exists {
// 		http.Error(w, "Person not found", http.StatusNotFound)
// 		return
// 	}

// 	w.Header().Set("Content-Type", "application/json")

// 	if err := json.NewEncoder(w).Encode(person); err != nil {
// 		http.Error(w, "Failed to encode response", http.StatusInternalServerError)
// 	}
// }

// // Connection pool to decouple Accept() from HTTP processing
// type ConnectionPool struct {
// 	connQueue   chan net.Conn
// 	httpHandler http.Handler
// 	workers     int
// }

// func NewConnectionPool(queueSize, workers int, handler http.Handler) *ConnectionPool {
// 	return &ConnectionPool{
// 		connQueue:   make(chan net.Conn, queueSize),
// 		httpHandler: handler,
// 		workers:     workers,
// 	}
// }

// func (cp *ConnectionPool) Start() {
// 	// Start worker goroutines to process HTTP
// 	for i := 0; i < cp.workers; i++ {
// 		go cp.httpWorker(i)
// 	}
// 	fmt.Printf("Started %d HTTP workers\n", cp.workers)
// }

// func (cp *ConnectionPool) Submit(conn net.Conn) {
// 	select {
// 	case cp.connQueue <- conn:
// 		// Connection queued successfully
// 	default:
// 		// Queue full, reject connection
// 		conn.Close()
// 	}
// }

// func (cp *ConnectionPool) httpWorker(workerID int) {
// 	for conn := range cp.connQueue {
// 		// Use standard HTTP server for each connection
// 		http.Serve(&singleConnListener{conn: conn}, cp.httpHandler)
// 	}
// }

// // Helper to serve HTTP on a single connection
// type singleConnListener struct {
// 	conn   net.Conn
// 	served bool
// }

// func (l *singleConnListener) Accept() (net.Conn, error) {
// 	if l.served {
// 		return nil, fmt.Errorf("connection already served")
// 	}
// 	l.served = true
// 	return l.conn, nil
// }

// func (l *singleConnListener) Close() error {
// 	return nil // Don't close the connection here
// }

// func (l *singleConnListener) Addr() net.Addr {
// 	return l.conn.LocalAddr()
// }

// func main() {
// 	port := 8080
// 	queueSize := 1000
// 	numWorkers := runtime.NumCPU() * 2

// 	fmt.Printf("Starting split-architecture server on port %d\n", port)
// 	fmt.Printf("Connection queue size: %d, HTTP workers: %d\n", queueSize, numWorkers)

// 	// Set up HTTP handler
// 	mux := http.NewServeMux()
// 	mux.HandleFunc("/person", getPersonHandler)

// 	// Create connection pool
// 	pool := NewConnectionPool(queueSize, numWorkers, mux)
// 	pool.Start()

// 	// Create listener
// 	listener, err := net.Listen("tcp", fmt.Sprintf(":%d", port))
// 	if err != nil {
// 		log.Fatal(err)
// 	}
// 	defer listener.Close()

// 	fmt.Printf("Accept loop started, HTTP processing decoupled\n")

// 	// PART 1: Fast Accept() loop (single-threaded, no blocking)
// 	for {
// 		conn, err := listener.Accept()
// 		if err != nil {
// 			log.Printf("Accept error: %v", err)
// 			continue
// 		}

// 		// PART 2: Submit to pool for HTTP processing (non-blocking)
// 		pool.Submit(conn)
// 	}
// }
