package shop.birdyseoul.birdobservation.security

import org.springframework.beans.factory.annotation.Autowired
import org.springframework.security.core.userdetails.User
import org.springframework.security.core.userdetails.UserDetails
import org.springframework.security.core.userdetails.UserDetailsService
import org.springframework.security.core.userdetails.UsernameNotFoundException
import org.springframework.stereotype.Service
import shop.birdyseoul.birdobservation.birders.BirderRepository

@Service
class BirderDetailService(
    @Autowired
    val birderRepo: BirderRepository
) : UserDetailsService {

    override fun loadUserByUsername(username: String?): UserDetails {
        val birder = birderRepo.findByUsername(username!!)
        if(birder != null) {
            return birder
        }
        throw UsernameNotFoundException("User $username not found")
    }
}