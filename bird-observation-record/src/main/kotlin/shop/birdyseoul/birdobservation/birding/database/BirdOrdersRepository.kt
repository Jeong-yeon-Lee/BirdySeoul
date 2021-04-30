package shop.birdyseoul.birdobservation.birding.database

import org.springframework.data.mongodb.core.mapping.Document
import org.springframework.data.mongodb.repository.MongoRepository
import shop.birdyseoul.birdobservation.birding.models.BirdOrder

@Document(collection = "species")
interface BirdOrdersRepository: MongoRepository<BirdOrder, String> {

}