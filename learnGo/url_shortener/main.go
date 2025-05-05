package main

import (
	"flag"
	"fmt"
	"net/http"
	"os"
	urlshort "url_shortener/short"
)

const (
	// yaml flag us used to set urls for yaml
	YAMLFlag      = "yaml"
	YAMLFlagValue = "urls.yaml"
	YAMLFlagUsage = "URLS file in yaml format"
)

type Flagger interface {
	StringVar(p *string, name, value, usage string)
}

type urlshortFlagger struct{}

func (uf *urlshortFlagger) StringVar(p *string, name, value, usage string) {
	flag.StringVar(p, name, value, usage)
}

var yaml string

// configflags will configure the flags used by the application
func ConfigFlags(flagger Flagger) {
	flagger.StringVar(&yaml, YAMLFlag, YAMLFlagValue, YAMLFlagUsage)
}

func main() {
	flagger := &urlshortFlagger{}
	ConfigFlags(flagger)

	mapHandler := createMapHandler()
	yamlHandler := createYAMLHandler(mapHandler)

	fmt.Println("start the server on : 8080")
	http.ListenAndServe(":8080", yamlHandler)
}

var pathsToUrls = map[string]string{
	"/urlshort-godoc": "https://godoc.org/github.com/gophercises/urlshort",
	"/yaml-godoc":     "https://godoc.org/gopkg.in/yaml.v2",
}

func createMapHandler() http.HandlerFunc {
	mux := defaultMux()
	return urlshort.MapHandler(pathsToUrls, mux)
}
func defaultMux() *http.ServeMux {
	mux := http.NewServeMux()
	mux.HandleFunc("/", hello)
	return mux
}

func hello(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintln(w, "hello world")
}

func createYAMLHandler(fallback http.Handler) http.HandlerFunc {
	yamlFile, err := os.Open(yaml)
	if err != nil {
		panic(err)
	}

	yamlHandler, err := urlshort.YAMLHandler(yamlFile, fallback)
	if err != nil {
		panic(err)
	}

	return yamlHandler
}
