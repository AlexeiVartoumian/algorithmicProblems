package main

import (
	"context"
	"fmt"
	"log"
	"net"

	pb "simplegprcserver/proto/gen"
	farewellpb "simplegprcserver/proto/gen/farewell"

	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials"
)

// keepin it private also when there are multiple  services
// need to add them to the server struct
type server struct {
	pb.UnimplementedCalculateServer
	pb.UnimplementedGreeterServer
	farewellpb.UnimplementedAufWiedersehenServer
}

func (s *server) Add(ctx context.Context, req *pb.AddRequest) (*pb.AddResponse, error) {
	return &pb.AddResponse{
		Sum: req.A + req.B,
	}, nil
}

//need to implement the function! for each service

func (s *server) Greet(ctx context.Context, req *pb.HelloRequest) (*pb.HelloResponse, error) {
	return &pb.HelloResponse{
		Message: fmt.Sprintf("Hello, %s nice to receive request ", req.Name),
	}, nil
}

func (s *server) BidGoodBye(ctx context.Context, req *farewellpb.GoodByeRequest) (*farewellpb.GoodByeResponse, error) {
	return &farewellpb.GoodByeResponse{
		Message: fmt.Sprintf("Goodbye, %s nice to receive request ", req.Name),
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
	//must register each service
	pb.RegisterGreeterServer(grpcServer, &server{})

	farewellpb.RegisterAufWiedersehenServer(grpcServer, &server{})

	//skipping something here
	log.Println("Server is running on port", port)
	err = grpcServer.Serve(lis)
	if err != nil {
		log.Fatal("Failed to serve :", err)
	}
}
