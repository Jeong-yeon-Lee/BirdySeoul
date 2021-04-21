package shop.birdyseoul.birdobservation.security

import org.springframework.beans.factory.annotation.Autowired
import org.springframework.context.annotation.Bean
import org.springframework.security.authentication.AuthenticationManager
import org.springframework.security.config.annotation.authentication.builders.AuthenticationManagerBuilder
import org.springframework.security.config.annotation.web.builders.HttpSecurity
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter
import org.springframework.security.config.http.SessionCreationPolicy
import org.springframework.security.core.Authentication
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder
import org.springframework.security.crypto.password.PasswordEncoder
import org.springframework.security.web.authentication.UsernamePasswordAuthenticationFilter
import shop.birdyseoul.birdobservation.birders.BirderRepository
import shop.birdyseoul.birdobservation.filters.JwtRequestFilter

@EnableWebSecurity
class SecurityConfig : WebSecurityConfigurerAdapter() {

    @Autowired
    lateinit var userDetailsService: BirderDetailService

    @Autowired
    lateinit var jwtRequestFilter: JwtRequestFilter

    @Autowired
    lateinit var repo: BirderRepository

    override fun configure(http: HttpSecurity?) {
        http!!.csrf().disable().authorizeRequests()
            .antMatchers(
                "/api/authenticate",
                "/api/register",
                "/static/**",
                "/*.json",
                "/*.ico",
                "/*.html",
                "/*.png",
                "/*.txt",
                "/"
            ).permitAll()
            .antMatchers("/api/records/{birder}/**")
            .access("@securityConfig.checkBirder(authentication,#birder)")
            .anyRequest().authenticated()
            .and().sessionManagement().sessionCreationPolicy(SessionCreationPolicy.STATELESS)
        http.addFilterBefore(jwtRequestFilter, UsernamePasswordAuthenticationFilter::class.java)
    }

    override fun configure(auth: AuthenticationManagerBuilder) {
        auth.userDetailsService(userDetailsService)
    }

    @Bean
    override fun authenticationManagerBean(): AuthenticationManager {
        return super.authenticationManagerBean()
    }

    @Bean
    fun passwordEncoder(): PasswordEncoder {
        return BCryptPasswordEncoder()
    }

    fun checkBirder(authentication: Authentication, birder: String): Boolean {
        return(authentication.name == birder)
    }
}