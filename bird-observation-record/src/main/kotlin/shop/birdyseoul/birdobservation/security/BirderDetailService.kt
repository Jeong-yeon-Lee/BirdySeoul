package shop.birdyseoul.birdobservation.security

import org.springframework.security.core.userdetails.User
import org.springframework.security.core.userdetails.UserDetails
import org.springframework.security.core.userdetails.UserDetailsService
import org.springframework.stereotype.Service

@Service
class BirderDetailService: UserDetailsService {
    override fun loadUserByUsername(username: String?): UserDetails {
        return User("foo", "foo", ArrayList())
    }
}