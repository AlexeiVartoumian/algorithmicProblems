package main

import (
	"fmt"
	"time"
)

type ticketRequest struct {
	personId   int
	numTickets int
	cost       int
}

//simulate processing of ticket selling and buying

func TicketProcessor(requests <-chan ticketRequest, results chan<- int) {

	for req := range requests {
		fmt.Printf("Processing %d tickets(s) of personID %d with total cost %d\n", req.numTickets, req.personId, req.cost)

		//simulate processing time
		time.Sleep(time.Second)
		results <- req.personId
	}
}

func main() {
	numRequests := 5
	price := 5
	ticketRequests := make(chan ticketRequest, numRequests)
	ticketResults := make(chan int)

	for range 3 {
		//create the workers
		go TicketProcessor(ticketRequests, ticketResults)
	}

	//send ticket requests
	for i := range numRequests {
		ticketRequests <- ticketRequest{personId: (i + 1), numTickets: (i + 1) * 2, cost: (i + 1) * price}
	}
	close(ticketRequests)

	for range numRequests {
		fmt.Printf("Ticket for personId %d processed successfully \n", <-ticketResults)
	}
}
