package main

import (
	"bufio"
	"fmt"
	mainpb "grpcstreams/proto/gen"
	"io"
	"log"
	"net"
	"os"
	"strings"
	"time"

	"google.golang.org/grpc"
)

type server struct {
	mainpb.UnimplementedCalculatorServer
}

func (s *server) GenerateFibonacci(req *mainpb.FibonacciReqest, stream mainpb.Calculator_GenerateFibonacciServer) error {

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

// function signature here is different the request type is stream
func (s *server) SendNumbers(stream mainpb.Calculator_SendNumbersServer) error {
	var sum int32
	//similar to channel this is an incoming stream so need an infinite llop
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
		// receiving values/messages from stream
		req, err := stream.Recv()
		if err == io.EOF {
			break
		}
		if err != nil {
			log.Fatalln(err)
		}
		log.Println("Received Message", req.GetMessage())

		// Read input from the terminal
		fmt.Println("Enter response: ")
		input, err := reader.ReadString('\n')
		if err != nil {
			return err
		}

		input = strings.TrimSpace(input)

		// sending data/messages values through the stream
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
