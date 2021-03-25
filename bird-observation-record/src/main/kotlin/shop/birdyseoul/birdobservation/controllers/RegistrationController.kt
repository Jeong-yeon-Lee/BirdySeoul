package shop.birdyseoul.birdobservation.controllers

import org.springframework.beans.factory.annotation.Autowired
import org.springframework.http.HttpStatus
import org.springframework.security.crypto.password.PasswordEncoder
import org.springframework.stereotype.Controller
import org.springframework.web.bind.annotation.*
import shop.birdyseoul.birdobservation.birders.BirderRepository
import shop.birdyseoul.birdobservation.birders.RegistrationForm

@Controller
@RequestMapping("/register")
class RegistrationController(
    @Autowired
    val birderRepo: BirderRepository,
    @Autowired
    val passwordEncoder: PasswordEncoder
) {

    @PostMapping(consumes = ["application/json"])
    @ResponseStatus(HttpStatus.CREATED)
    fun processRegistration(@RequestBody registrationForm: RegistrationForm) {
        birderRepo.save(registrationForm.toBirder(passwordEncoder))
    }
}