package main

import (
	"context"
	"fmt"
)

func main1() {

	todoContext := context.TODO() // key valyue pair contxt is a struct , however dont user .TODO for
	// cancellations signals , request scoped values or deadlines use background instead

	contextBkg := context.Background() // returns empty ctx which is a struct with all the
	// aviaalble reciever methosd as per source code below
	// type backgroundCtx struct{ emptyCtx }
	// func (emptyCtx) Deadline() (deadline time.Time, ok bool)
	// func (emptyCtx) Done() <-chan struct{}
	// func (emptyCtx) Err() error
	// func (backgroundCtx) String() string
	// func (emptyCtx) Value(key any) any

	ctx := context.WithValue(todoContext, "name", "john")
	fmt.Println(ctx)
	fmt.Println(ctx.Value("name"))

	ctx1 := context.WithValue(contextBkg, "city", "New York")
	fmt.Println(ctx1)
	fmt.Println(ctx1.Value("city"))
}
