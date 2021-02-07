package shop.birdyseoul.birdyseoulauthserver

import org.springframework.beans.factory.annotation.Autowired
import org.springframework.http.ResponseEntity
import org.springframework.security.authentication.AuthenticationManager
import org.springframework.stereotype.Controller
import org.springframework.ui.Model
import org.springframework.ui.set
import org.springframework.web.bind.annotation.*

@RestController
class LoginController {

//    @Autowired
//    lateinit var authenticationManager: AuthenticationManager

    @GetMapping("/hello")
    fun hello(): String {
        return "Hello, This is Birdy Seoul!"
    }

//    @RequestMapping(value = ["/authenticate"], method = [RequestMethod.POST])
//    fun createAuthenticationToken(@RequestBody authenticationRequest: AuthenticationRequest): ResponseEntity<> {
//
//    }
}