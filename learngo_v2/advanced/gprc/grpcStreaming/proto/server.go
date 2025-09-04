package main

import (
	mainpb "grpcstreams/proto/gen"
	"io"
	"log"
	"net"
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
