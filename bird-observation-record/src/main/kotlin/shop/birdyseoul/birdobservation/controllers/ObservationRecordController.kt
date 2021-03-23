package shop.birdyseoul.birdobservation.controllers

import org.springframework.beans.factory.annotation.Autowired
import org.springframework.http.HttpStatus
import org.springframework.web.bind.annotation.*
import shop.birdyseoul.birdobservation.dbaccess.BirdObservationRecord
import shop.birdyseoul.birdobservation.dbaccess.ObservationRecordRepository

@RestController
class ObservationRecordController {

    @Autowired
    lateinit var repository: ObservationRecordRepository

    @PostMapping(path = ["/api/record"],consumes = ["application/json"])
    @ResponseStatus(HttpStatus.CREATED)
    fun addRecord(@RequestBody record: BirdObservationRecord) {
        this.repository.save(record)
    }

    @PostMapping(path = ["/api/observations"], consumes = ["application/json"])
    @ResponseStatus(HttpStatus.CREATED)
    fun addRecords(@RequestBody records: List<BirdObservationRecord>) {
        this.repository.saveAll(records)
    }

    @GetMapping("/api/records")
    fun getAllRecords(): MutableList<BirdObservationRecord> {
        return repository.findAll()
    }
}