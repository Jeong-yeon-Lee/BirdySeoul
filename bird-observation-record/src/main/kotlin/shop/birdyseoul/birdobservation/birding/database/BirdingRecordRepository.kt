package shop.birdyseoul.birdobservation.birding.database

import org.springframework.data.mongodb.core.mapping.Document
import org.springframework.data.mongodb.repository.MongoRepository
import shop.birdyseoul.birdobservation.models.BirdingRecord

@Document(collection = "observations")
interface BirdingRecordRepository: MongoRepository<BirdingRecord, String> {
    fun findByRecorder(recorder: String): MutableList<BirdingRecord>
}