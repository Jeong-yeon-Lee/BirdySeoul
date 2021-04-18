package shop.birdyseoul.birdobservation.controllers

import org.springframework.beans.factory.annotation.Autowired
import org.springframework.http.HttpStatus
import org.springframework.http.ResponseEntity
import org.springframework.security.crypto.password.PasswordEncoder
import org.springframework.stereotype.Controller
import org.springframework.web.bind.annotation.*
import shop.birdyseoul.birdobservation.birders.Birder
import shop.birdyseoul.birdobservation.birders.BirderRepository
import shop.birdyseoul.birdobservation.birders.RegistrationForm

@Controller
@RequestMapping("/api/register")
@CrossOrigin(origins = ["*"])
class RegistrationController(
    @Autowired
    val birderRepo: BirderRepository,
    @Autowired
    val passwordEncoder: PasswordEncoder
) {

    @PostMapping(consumes = ["application/json"])
    @ResponseStatus(HttpStatus.CREATED)
    fun processRegistration(@RequestBody registrationForm: RegistrationForm): ResponseEntity<Any> {
        val test: Birder? = birderRepo.findByEmail(registrationForm.email);
        if(test != null) {
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Same Email Exists")
        }
        birderRepo.save(registrationForm.toBirder(passwordEncoder))
        return ResponseEntity.ok("Registration Success!")
    }
}