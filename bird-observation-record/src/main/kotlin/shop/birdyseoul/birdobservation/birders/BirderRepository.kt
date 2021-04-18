package shop.birdyseoul.birdobservation.birders

import org.springframework.data.mongodb.core.mapping.Document
import org.springframework.data.mongodb.repository.MongoRepository
import shop.birdyseoul.birdobservation.dbaccess.BirdObservationRecord

@Document(collection = "birders")
interface BirderRepository : MongoRepository<Birder, String> {
    fun findByEmail(email: String): Birder?
}