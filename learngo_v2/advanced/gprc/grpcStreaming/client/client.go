package main

import (
	"context"
	mainpb "grpcstreamclient/proto/gen"
	"io"
	"log"
	"time"

	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
)

func main() {

	conn, err := grpc.NewClient("localhost:50051", grpc.WithTransportCredentials(insecure.NewCredentials()))

	if err != nil {
		log.Fatalln(err)
	}
	defer conn.Close()

	client := mainpb.NewCalculatorClient(conn)
	//prepare the parameters needed for rpc call
	ctx := context.Background()

	req := &mainpb.FibonacciReqest{
		N: 10,
	}
	//main.proto file is a stream here
	stream, err := client.GenerateFibonacci(ctx, req)

	if err != nil {
		log.Fatalln("Error calling GenerateFibonacci func: ", err)
	}

	//infiinte loop o consume stream
	for {
		//method on the client stream
		resp, err := stream.Recv()
		if err == io.EOF {
			log.Println("End of stream")
			break
		}
		if err != nil {
			log.Fatalln("Error receiving data from GenreateFibonaccu func", err)
		}
		log.Println("Fibonacci number", resp.GetNumber())
	}
	// ---- server side streaming now ends

	// client side streaming beings
	stream1, err := client.SendNumbers(ctx)
	if err != nil {
		log.Fatalln("Error creating stream:", err)
	}
	for num := range 9 {
		err := stream1.Send(&mainpb.NumberRequest{Number: int32(num)})

		if err != nil {
			log.Fatalln("Error sending number", err)
		}
		time.Sleep(time.Second)
	}
	res, err := stream1.CloseAndRecv()
	if err != nil {
		log.Fatalln("Error recieving response", err)
	}
	log.Println("SUM", res.Sum)
	//client side streaming end
}
