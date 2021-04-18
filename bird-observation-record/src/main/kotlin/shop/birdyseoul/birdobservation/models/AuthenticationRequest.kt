package shop.birdyseoul.birdobservation.models

data class AuthenticationRequest(
    val email: String,
    val password: String
)