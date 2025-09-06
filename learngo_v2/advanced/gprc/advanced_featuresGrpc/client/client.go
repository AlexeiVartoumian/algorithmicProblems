package main

import (
	"context"
	"log"
	mainpb "simplegrpc/proto/gen"
	"time"

	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials"
	"google.golang.org/grpc/encoding/gzip"
	_ "google.golang.org/grpc/encoding/gzip"
	"google.golang.org/grpc/metadata"
)

func main() {

	cert := "cert.pem"

	creds, err := credentials.NewClientTLSFromFile(cert, "")

	if err != nil {
		log.Fatalln("Did not connect", err)
	}

	conn, err := grpc.NewClient("localhost:50051", grpc.WithTransportCredentials(creds))
	// could pass in this value that will automatically compress grpc.WithDefaultCallOptions(grpc.UseCompressor(gzip.Name))
	if err != nil {
		log.Fatalln("Did not connect", err)
	}
	defer conn.Close()

	client := mainpb.NewCalculatorClient(conn)
	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()

	req := &mainpb.AddRequest{
		A: 10,
		B: 20,
	}

	//adding metadata to request from grpc recall metadata is key value pairs also is variadic func
	md := metadata.Pairs("authorizaiton", "Bearer=kjhdnoioi123-rf09", "testing", "testing2")
	ctx = metadata.NewOutgoingContext(ctx, md)

	var resHeader metadata.MD
	var resTrailer metadata.MD
	res, err := client.Add(ctx, req, grpc.UseCompressor(gzip.Name), grpc.Header(&resHeader), grpc.Trailer(&resTrailer))

	if err != nil {
		log.Fatalln("oh no could not add", err)
	}
	log.Println("resheader", resHeader)
	log.Println("resHeader[test]", resHeader["Test"][0])
	log.Println("resHeader[testTrailer]", resTrailer["testTrailer"])
	log.Println(res.Sum)

}
