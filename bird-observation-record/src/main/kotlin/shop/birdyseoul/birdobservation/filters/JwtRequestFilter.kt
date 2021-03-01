package shop.birdyseoul.birdobservation.filters

import org.springframework.beans.factory.annotation.Autowired
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken
import org.springframework.security.core.context.SecurityContextHolder
import org.springframework.security.web.authentication.WebAuthenticationDetailsSource
import org.springframework.stereotype.Component
import org.springframework.web.filter.OncePerRequestFilter
import shop.birdyseoul.birdobservation.security.BirderDetailService
import shop.birdyseoul.birdobservation.util.JWTUtil
import javax.servlet.FilterChain
import javax.servlet.http.HttpServletRequest
import javax.servlet.http.HttpServletResponse

@Component
class JwtRequestFilter : OncePerRequestFilter() {

    @Autowired
    lateinit var userDetailsService: BirderDetailService

    @Autowired
    lateinit var jwtUtil: JWTUtil

    override fun doFilterInternal(
        request: HttpServletRequest,
        response: HttpServletResponse,
        filterChain: FilterChain
    ) {
        val authorizationHeader = request.getHeader("Authorization")
        var username: String? = null
        var jwt: String? = null

        if (authorizationHeader != null && authorizationHeader.startsWith("Bearer ")) {
            jwt = authorizationHeader.substring(7)
            username = jwtUtil.extractUserName(jwt)
        }

        if (username != null && SecurityContextHolder.getContext().authentication == null) {
            val userDetails = this.userDetailsService.loadUserByUsername(username)
            if (jwtUtil.validateToken(jwt!!, userDetails)) {
                val authenticationToken =
                    UsernamePasswordAuthenticationToken(userDetails, null, userDetails.authorities)
                authenticationToken.details = WebAuthenticationDetailsSource().buildDetails(request)
                SecurityContextHolder.getContext().authentication = authenticationToken
            }
        }
        filterChain.doFilter(request, response)
    }

}