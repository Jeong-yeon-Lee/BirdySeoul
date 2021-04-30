package shop.birdyseoul.birdobservation.birders.database

import org.springframework.data.mongodb.core.mapping.Document
import org.springframework.data.mongodb.repository.MongoRepository
import shop.birdyseoul.birdobservation.birders.models.Birder

@Document(collection = "birders")
interface BirderRepository : MongoRepository<Birder, String> {
    fun findByEmail(email: String): Birder?
}