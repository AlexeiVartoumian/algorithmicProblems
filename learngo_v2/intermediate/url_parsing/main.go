package main

import (
	"fmt"
	"net/url"
)

func main() {

	//[scheme://][userinfo@]host[:port][/path][?query][#fragment]

	// protocol can be http https or ftp

	rawURL := "https://example.com:8080/path?query=param#fragment"
	parsedURL, err := url.Parse(rawURL)

	if err != nil {
		fmt.Println("Erorr in url")
	}

	fmt.Println("Scheme", parsedURL.Scheme)
	fmt.Println("Host", parsedURL.Host)
	fmt.Println("Port", parsedURL.Port())
	fmt.Println("Path", parsedURL.Path)
	fmt.Println("Raw Query", parsedURL.RawQuery)
	fmt.Println("Fragment", parsedURL.Fragment)

	//understanding query parameters and parsing// processing them

	rawUrl1 := "https://example.com/path/?name=John&age=30"
	parsedURL1, err := url.Parse(rawUrl1)

	if err != nil {
		fmt.Println("Error pasing Url", err)
		return
	}

	//gives key value pairs in map structure
	queryParams := parsedURL1.Query()
	fmt.Println(queryParams)
	fmt.Println("Name: ", queryParams.Get("name"))
	fmt.Println("Age:", queryParams.Get("age"))

	//building URl
	baseURL := &url.URL{
		Scheme: "https",
		Host:   "example.com",
		Path:   "/path",
	}
	query := baseURL.Query()
	query.Set("name", "john") // key value

	baseURL.RawQuery = query.Encode() // will take the above and turn into "bar=baz&foo=quux"

	baseURL.RawQuery = query.Encode()
	fmt.Println("Build url ", baseURL.String())

	//difffernt way to build the url
	values := url.Values{}

	values.Add("name", "Jane")
	values.Add("age", "30")
	values.Add("city", "London")
	values.Add("Country", "UK")

	encodedQuery := values.Encode()
	fmt.Println(encodedQuery)

	//building url with above
	baseUrl1 := "https://example.com/search"
	fullUrl := baseUrl1 + "?" + encodedQuery

	fmt.Println(fullUrl)
}
