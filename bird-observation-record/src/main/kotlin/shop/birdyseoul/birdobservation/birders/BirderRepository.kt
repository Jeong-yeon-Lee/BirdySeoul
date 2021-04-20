package shop.birdyseoul.birdobservation.birders

import org.springframework.data.mongodb.core.mapping.Document
import org.springframework.data.mongodb.repository.MongoRepository

@Document(collection = "birders")
interface BirderRepository : MongoRepository<Birder, String> {
    fun findByEmail(email: String): Birder?
}