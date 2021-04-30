package shop.birdyseoul.birdobservation.birding.database

import org.springframework.data.mongodb.repository.MongoRepository
import shop.birdyseoul.birdobservation.birding.models.BirdingSpot

interface BirdingSpotRepository: MongoRepository<BirdingSpot, String> {
}