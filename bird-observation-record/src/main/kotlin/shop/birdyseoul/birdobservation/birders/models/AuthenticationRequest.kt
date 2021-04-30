package shop.birdyseoul.birdobservation.birders.models

data class AuthenticationRequest(
    val email: String,
    val password: String
)