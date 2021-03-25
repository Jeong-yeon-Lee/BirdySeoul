package shop.birdyseoul.birdobservation.dbaccess

import org.springframework.data.mongodb.core.mapping.Document
import org.springframework.data.mongodb.repository.MongoRepository

@Document(collection = "observations")
interface ObservationRecordRepository: MongoRepository<BirdObservationRecord, String> {

}