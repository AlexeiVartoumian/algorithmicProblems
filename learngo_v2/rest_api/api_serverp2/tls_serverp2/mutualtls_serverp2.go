package main

import (
	"crypto/tls"
	"crypto/x509"
	"fmt"
	"log"
	"net/http"
	"os"

	"golang.org/x/net/http2"
)

// very similar to tlsserver but have addiaiontl function to pass client ca to tls config struct
// using the below function to pass in and read  the same Certificate.
func loadClientCAs() *x509.CertPool {
	clientCAs := x509.NewCertPool()
	caCert, err := os.ReadFile("cert.pem")

	if err != nil {
		log.Fatalln("Cannot run the server without loading Client CA", err)
	}
	clientCAs.AppendCertsFromPEM(caCert)
	return clientCAs
}

func main2() {

	// since http vevrbs and methods not defined can send any requ3esr
	http.HandleFunc("/orders", func(w http.ResponseWriter, r *http.Request) {
		logRequestDetails(r)
		fmt.Fprintf(w, "handling incoming orders")
	})

	http.HandleFunc("/users", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintf(w, "hadnling users")
	})

	port := 3000
	// implementing a tls certificate is a but differnt
	// requires certifcate openssl req -x509 -newkey rsa:2048 -nodes -keyout key.pem -out cert.pem -days 365
	cert := "cert.pem"
	key := "key.pem"

	// configure tls only accepting requests with tls 1.2 and above
	tlsConfig := &tls.Config{
		MinVersion: tls.VersionTLS12,
		ClientAuth: tls.RequireAndVerifyClientCert, //enforces mTls , a valid certificate must be provided
		ClientCAs:  loadClientCAs(),                // this is a pool of trusted certificate authorities by the server
	}

	server := &http.Server{
		Addr:      fmt.Sprintf(":%d", port),
		Handler:   nil,
		TLSConfig: tlsConfig,
	}
	// using the http2 package to enable versioned protocol
	http2.ConfigureServer(server, &http2.Server{})
	fmt.Println("Server is running on port ", port)
	err := server.ListenAndServeTLS(cert, key) // using the certs + keys jsut created

	if err != nil {
		log.Fatalln("coukd not start server", err)
	}
	// below is http 1.1 server without tls
	// fmt.Println("Server is running on port ", port)
	// //log.Fatal(http.ListenAndServe(fmt.Sprintf(":%d", port), nil))
	// err := http.ListenAndServe(fmt.Sprintf(":%d", port), nil)
	// if err != nil {
	// 	log.Fatalln("Could not start sever", err)
	// }
}

func logRequestDetails2(r *http.Request) {
	httpVersion := r.Proto
	fmt.Println("Received request with http version", httpVersion)

	if r.TLS != nil {
		tlsVersion := getTLSVersionName(r.TLS.Version)
		fmt.Println("Received request with TLS version", tlsVersion)
	} else {
		fmt.Println("Revcived request without tls")
	}
}

func getTLSVersionName2(version uint16) string {

	switch version {
	case tls.VersionTLS10:
		return "TLS1.0"
	case tls.VersionTLS11:
		return "TLS1.1"
	case tls.VersionTLS12:
		return "TLS1.2"
	case tls.VersionTLS13:
		return "TLS1.3"
	default:
		return "Unknown TLS version"

	}
}
