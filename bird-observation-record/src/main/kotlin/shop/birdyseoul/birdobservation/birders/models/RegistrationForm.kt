package shop.birdyseoul.birdobservation.birders.models

import org.springframework.security.crypto.password.PasswordEncoder

data class RegistrationForm(
    val password: String,
    val email: String
) {
    fun toBirder(passwordEncoder: PasswordEncoder): Birder {
        return Birder(email, passwordEncoder.encode(password))
    }
}