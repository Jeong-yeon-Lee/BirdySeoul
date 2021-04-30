package shop.birdyseoul.birdobservation.birding.database

import org.springframework.data.mongodb.repository.MongoRepository
import shop.birdyseoul.birdobservation.models.Observation

interface ObservationRepository: MongoRepository<Observation, String> {
}