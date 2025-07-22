package middlewares

import "net/http"

//applying a chaining technique basic skeleton is like so
// func securityHeaders(next http.Handler) http.Handler {
// 	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {

// 	})
// }

func SecurityHeaders(next http.Handler) http.Handler {
	//user Handelefunc
	//HandleFunc lets you Handle a request with a Func, i.e think mux its a conveinence method
	//HandlerFunc is a type that is an adapter and allows the use of ordinary finctions as http functions
	// i.e think middleware below function can now be used to wrap around mux
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {

		//actual secrity headers by protecting api and what go does internaly when applied many headers outside of these ones

		w.Header().Set("X-DNS-Prefetch-Control", "off")
		// disables mechanism for browsers to resolve domain names while user is browsing a web page
		// wihtout browser can expose users or trigger uneccsary dns traffic
		w.Header().Set("X-Frame-Options", "DENY")
		//prevent web page from being displayed in an iframe on other websites . avoid clickjacking attacks

		w.Header().Set("X-XSS-Protection", "1;mode=block")
		//instructs browser to block page if xss is detected internally. without header this may not be enforced

		w.Header().Set("X-Content-Type-Options", "nosniff")
		//this header prevents browsers from MIME(multi-purpose internet mail extensions)
		// sniffing ensuring files are shared over email sometimes called content-type prevents some wied diffusion attack

		w.Header().Set("Strict Transport Security", "max-age=63072000;includeSubDomains;preload")
		//enforces https and tells browsers to interact with api only via https . without this
		// http could be used exposing users to potential man in middle attacks

		w.Header().Set("Content-Security-Policy", "default-src 'self'")
		// controls which resources are loaded mitigating against cross-site scripting , data injection
		// eithout this browser can allow content to be loaded

		w.Header().Set("Referred-Policy", "no-referrer")
		// will strip out the referrer information from sender

		w.Header().Set("X-Powered-By", "Django") // lies by obfuscation!

		w.Header().Set("Server", "")
		w.Header().Set("X-Permitted-Cross-Domain-Policies", "none")
		w.Header().Set("Cache-Control", "no-store, no-cache, must-revalidate , max-age=0")
		w.Header().Set("Cross-Origin-Resource-Policy", "same-origin")
		w.Header().Set("Cross-Origin-Opener-Policy", "same-origin")
		w.Header().Set("Cross-Origin-Embedder-Policy", "require-corp")

		w.Header().Set("Permissions-policy", "geolocation=(self), microphone=()")
		next.ServeHTTP(w, r)
	})
}
