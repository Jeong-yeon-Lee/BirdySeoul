package shop.birdyseoul.birdobservation.birders

import org.springframework.security.crypto.password.PasswordEncoder

data class RegistrationForm(
    val id: String,
    val username: String,
    val password: String,
    val email: String
) {
    fun toBirder(passwordEncoder: PasswordEncoder): Birder {
        return Birder(id, email, passwordEncoder.encode(password), username)
    }
}