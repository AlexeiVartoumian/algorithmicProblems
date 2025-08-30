package main

import (
	"context"
	"log"
	"net"

	pb "simplegprcserver/proto/gen"

	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials"
)

// keepin it private
type server struct {
	pb.UnimplementedCalculateServer
}

func (s *server) Add(ctx context.Context, req *pb.AddRequest) (*pb.AddResponse, error) {
	return &pb.AddResponse{
		Sum: req.A + req.B,
	}, nil
}
func main() {

	cert := "cert.pem"
	key := "key.pem"

	port := ":50051"
	//grpc can handle both unary and streaming rpcs
	lis, err := net.Listen("tcp", port)
	if err != nil {
		log.Fatal("Failed to listen:", err)
	}

	//need to create a new grpc server with certs
	creds, err := credentials.NewServerTLSFromFile(cert, key)

	if err != nil {
		log.Fatalln("Failed to load credentails", err)
	}

	grpcServer := grpc.NewServer(grpc.Creds(creds))

	pb.RegisterCalculateServer(grpcServer, &server{})

	//skipping something here
	log.Println("Server is running on port", port)
	err = grpcServer.Serve(lis)
	if err != nil {
		log.Fatal("Failed to serve :", err)
	}
}
