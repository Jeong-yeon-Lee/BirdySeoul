package shop.birdyseoul.birdyseoulauthserver

import org.springframework.boot.SpringApplication
import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication

@SpringBootApplication
class BirdyseoulAuthServerApplication

fun main(args: Array<String>) {
    runApplication<BirdyseoulAuthServerApplication>(*args)
}

