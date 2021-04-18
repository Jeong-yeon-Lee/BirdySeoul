package shop.birdyseoul.birdobservation.birders

import org.springframework.data.annotation.Id
import org.springframework.security.core.GrantedAuthority
import org.springframework.security.core.authority.SimpleGrantedAuthority
import org.springframework.security.core.userdetails.UserDetails

class Birder constructor(
    val email: String,
    private val password: String,
) : UserDetails {

    @Id
    private lateinit var id: String

    override fun getAuthorities(): MutableCollection<out GrantedAuthority> {
        return mutableSetOf(SimpleGrantedAuthority("ROLE_USER"))
    }

    override fun getPassword(): String {
        return this.password
    }

    override fun getUsername(): String {
        return this.email
    }

    override fun isAccountNonExpired(): Boolean {
        return true
    }

    override fun isAccountNonLocked(): Boolean {
        return true
    }

    override fun isCredentialsNonExpired(): Boolean {
        return true
    }

    override fun isEnabled(): Boolean {
        return true
    }

}