package main

import (
	"fmt"
	"io"
	"net/http"

	yaml "gopkg.in/yaml.v3"
)

//Maphandler will return an http.Handlerfunc
// which also implements http.Handler that will attempt to map any paths
//in the map to thier corresponding url
//values that each keu in the map point to in string format/
// if th path is not provied in the map then the fallback
// http.Handler will be called instead

func Maphandler(pathToUrls map[string]string, fallback http.Handler) http.HandlerFunc {

	return func(w http.ResponseWriter, r *http.Request) {

		path := r.URL.Path

		if destination, ok := pathToUrls[path]; ok {
			http.Redirect(w, r, destination, http.StatusFound)
		}

		fallback.ServeHTTP(w, r)

	}

}

type pathURL struct {
	PATH string `yaml:"path" json:"path"`
	URL  string `yaml:"url"  json:"url"`
}
type decoder interface {
	Decode(v interface{}) error
}

func buildMaps(pathURLS []pathURL) map[string]string {

	pathToUrls := make(map[string]string)

	for _, urls := range pathURLS {
		pathToUrls[urls.PATH] = urls.URL
	}

	return pathToUrls
}

func YAMLHandler(r io.Reader, fallback http.Handler) (http.HandlerFunc, error) {

	decoder := yaml.NewDecoder(r)
	pathURL, err := decode(decoder)

	if err != nil {
		return nil, err
	}
	pathToUrls := buildMaps(pathURL)
	mapHandler := Maphandler(pathToUrls, fallback)

	return mapHandler, nil
}

func decode(d decoder) ([]pathURL, error) {
	var pu []pathURL
	for {
		err := d.Decode(&pu)
		if err == io.EOF {
			return pu, nil
		} else if err != nil {
			return nil, err
		}
	}
}

func main() {
	fmt.Println("hi")
}
