package main

import (
	"bufio"
	"context"
	"fmt"
	"io"
	"log"
	"net"
	"os"
	mainpb "simpleGrpc/proto/gen"
	"strings"
	"time"

	"google.golang.org/grpc"
	_ "google.golang.org/grpc/encoding/gzip" // use underscore to allow grpc to automatically use gzip but not remove the import
	"google.golang.org/grpc/metadata"
)

type server struct {
	mainpb.UnimplementedCalculatorServer
}

func (s *server) Add(ctx context.Context, req *mainpb.AddRequest) (*mainpb.AddResponse, error) {
	//adding metadata from request
	md, ok := metadata.FromIncomingContext(ctx)
	if !ok {
		log.Println("no metatData recieved")
	}
	log.Println("Metadata", md)
	val, ok := md["authorization"] //comes from ctx also accessing a key in a map need a ok bool since two vals are needed here
	//metadata work exacltly like headers
	if !ok {
		log.Println("no value with auth key in metadata")
	}
	log.Println("authorization", val)

	//set response headers
	responseHeaders := metadata.Pairs("test", "testvalue", "test2", "anotherone")
	err := grpc.SendHeader(ctx, responseHeaders) // accepts context

	if err != nil {
		return nil, err
	}

	//adding trailers here see readme
	trailer := metadata.Pairs("testTrailer", "testtrailervalue", "testtrailer2", "anotheronetrailer")
	grpc.SetTrailer(ctx, trailer)

	return &mainpb.AddResponse{
		Sum: req.A + req.B,
	}, nil
}

func (s *server) GenerateFibonacci(req *mainpb.FibonacciRequest, stream mainpb.Calculator_GenerateFibonacciServer) error {

	n := req.N
	a, b := 0, 1

	for i := 0; i < int(n); i++ {
		err := stream.Send(&mainpb.FibonacciResponse{
			Number: int32(a),
		})

		if err != nil {
			return err
		}
		a, b = b, a+b
		time.Sleep(time.Second)
	}
	return nil
}

// function signature is differnt the request type is stream
func (s *server) SendNumbers(stream mainpb.Calculator_SendNumbersServer) error {
	var sum int32
	// need infinite loop for comms to work here like a channel
	for {

		req, err := stream.Recv()
		if err == io.EOF {
			return stream.SendAndClose(&mainpb.NumberResponse{Sum: sum})
		}
		if err != nil {
			return err
		}
		log.Println(req.GetNumber())
		sum += req.GetNumber()
	}
}

func (s *server) Chat(stream mainpb.Calculator_ChatServer) error {

	reader := bufio.NewReader(os.Stdin)

	for {
		req, err := stream.Recv()
		if err == io.EOF {
			break
		}
		if err != nil {
			log.Fatalln(err)
		}
		log.Println("Recieved Message", req.GetMessage())

		fmt.Println("Enter Response")
		input, err := reader.ReadString('\n')

		if err != nil {
			return err
		}
		input = strings.TrimSpace(input)

		err = stream.Send(&mainpb.ChatMessage{
			Message: input,
		})
		if err != nil {
			return err
		}
	}
	fmt.Println("Returning Control")
	return nil
}

func main() {
	lis, err := net.Listen("tcp", ":50051")

	if err != nil {
		log.Fatalln(err)
	}
	grpcServer := grpc.NewServer()
	mainpb.RegisterCalculatorServer(grpcServer, &server{})

	err = grpcServer.Serve(lis)
	if err != nil {
		log.Fatalln(err)
	}
}
