package shop.birdyseoul.birdobservation.controllers

import org.springframework.beans.factory.annotation.Autowired
import org.springframework.boot.web.servlet.server.Session
import org.springframework.http.ResponseEntity
import org.springframework.security.authentication.AuthenticationManager
import org.springframework.security.authentication.BadCredentialsException
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken
import org.springframework.security.core.context.SecurityContextHolder
import org.springframework.security.core.userdetails.UserDetails
import org.springframework.web.bind.annotation.*
import shop.birdyseoul.birdobservation.models.AuthenticationRequest
import shop.birdyseoul.birdobservation.models.AuthenticationResponse
import shop.birdyseoul.birdobservation.security.BirderDetailService
import shop.birdyseoul.birdobservation.util.JWTUtil
import javax.servlet.http.Cookie
import javax.servlet.http.HttpServletResponse

@RestController
@CrossOrigin(origins = ["*", "http://localhost:3000"])
class AuthenticationController {

    @Autowired
    lateinit var authenticationManager: AuthenticationManager

    @Autowired
    lateinit var userDetailsService: BirderDetailService

    @Autowired
    lateinit var jwtUtil: JWTUtil

    @RequestMapping(value=["/api/test"], method= [RequestMethod.GET])
    fun test(response: HttpServletResponse): ResponseEntity<String> {
        return ResponseEntity.ok("Test Success!!")
    }

    @RequestMapping(value = ["/api/authenticate"], method = [RequestMethod.POST], consumes = ["application/json"])
    fun createAuthenticationToken(@RequestBody request: AuthenticationRequest, response: HttpServletResponse): ResponseEntity<Any> {
        try {
            authenticationManager.authenticate(
                UsernamePasswordAuthenticationToken(request.email, request.password)
            )
        } catch(e: BadCredentialsException) {
            e.printStackTrace()
            throw Exception("Incorrect username or password", e)
        }

//        val cookie: Cookie = Cookie("platform", "web");
//        cookie.maxAge = 7*24*60*60
//        cookie.isHttpOnly = true
//        cookie.path = "/"
//
//        response.addCookie(cookie)

        val userDetails: UserDetails = userDetailsService.loadUserByUsername(request.email)
        val jwt: String = jwtUtil.generateToken(userDetails)
        return ResponseEntity.ok(AuthenticationResponse(jwt))
    }
}