package main

import (
	"context"
	"log"
	mainpipb "simplegprcserver/proto/gen"
	"time"

	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials"
)

func main() {

	cert := "../cert.pem"
	creds, err := credentials.NewClientTLSFromFile(cert, "")
	if err != nil {
		log.Fatalln("did not connect", err)
	}
	//to call over rpc need to establosh a connection to server and
	// that means a domain and port

	//conn, err := grpc.NewClient("localhost:50051", grpc.WithTransportCredentials(insecure.NewCredentials()))
	conn, err := grpc.NewClient("localhost:50051", grpc.WithTransportCredentials(creds))
	if err != nil {
		log.Fatalln("Did not connect", err)
	}
	defer conn.Close()

	//now we can call rpc's
	// need to call the interface and the methdod to implement it refer to generated main_gprc.pb.go file

	client := mainpipb.NewCalculateClient(conn)

	// once client has been crested can now
	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()
	req := mainpipb.AddRequest{
		A: 10,
		B: 20,
	}
	res, err := client.Add(ctx, &req)
	if err != nil {
		log.Fatalln("could not add", err)
	}
	log.Println("Sum", res.Sum)
}
