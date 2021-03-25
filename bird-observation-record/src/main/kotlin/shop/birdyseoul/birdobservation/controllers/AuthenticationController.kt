package shop.birdyseoul.birdobservation.controllers

import org.springframework.beans.factory.annotation.Autowired
import org.springframework.http.ResponseEntity
import org.springframework.security.authentication.AuthenticationManager
import org.springframework.security.authentication.BadCredentialsException
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken
import org.springframework.security.core.userdetails.UserDetails
import org.springframework.web.bind.annotation.RequestBody
import org.springframework.web.bind.annotation.RequestMapping
import org.springframework.web.bind.annotation.RequestMethod
import org.springframework.web.bind.annotation.RestController
import shop.birdyseoul.birdobservation.models.AuthenticationRequest
import shop.birdyseoul.birdobservation.models.AuthenticationResponse
import shop.birdyseoul.birdobservation.security.BirderDetailService
import shop.birdyseoul.birdobservation.util.JWTUtil

@RestController
class AuthenticationController {

    @Autowired
    lateinit var authenticationManager: AuthenticationManager

    @Autowired
    lateinit var userDetailsService: BirderDetailService

    @Autowired
    lateinit var jwtUtil: JWTUtil

    @RequestMapping(value = ["/authenticate"], method = [RequestMethod.POST], consumes = ["application/json"])
    fun createAuthenticationToken(@RequestBody request: AuthenticationRequest): ResponseEntity<Any> {
        try {
            authenticationManager.authenticate(
                UsernamePasswordAuthenticationToken(request.username, request.password)
            )
        } catch(e: BadCredentialsException) {
            throw Exception("Incorrect username or password", e)
        }
        val userDetails: UserDetails = userDetailsService.loadUserByUsername(request.username)
        val jwt: String = jwtUtil.generateToken(userDetails)
        return ResponseEntity.ok(AuthenticationResponse(jwt))
    }
}