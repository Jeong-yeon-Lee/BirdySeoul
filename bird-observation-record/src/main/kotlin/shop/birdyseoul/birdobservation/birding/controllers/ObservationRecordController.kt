package shop.birdyseoul.birdobservation.birding.controllers

import org.springframework.beans.factory.annotation.Autowired
import org.springframework.http.HttpStatus
import org.springframework.http.ResponseEntity
import org.springframework.security.core.context.SecurityContextHolder
import org.springframework.web.bind.annotation.*
import shop.birdyseoul.birdobservation.models.BirdingRecord
import shop.birdyseoul.birdobservation.birding.database.BirdingRecordRepository

@RestController
class ObservationRecordController {

    @Autowired
    lateinit var repository: BirdingRecordRepository

    @PostMapping(path = ["/api/record/create/{birder}"], consumes = ["application/json"])
    @ResponseStatus(HttpStatus.CREATED)
    fun addRecord(@RequestBody record: BirdingRecord, @PathVariable birder: String): ResponseEntity<String> {
        this.repository.save(record)
        return ResponseEntity.ok("Successfully saved a birding record!")
    }

    @GetMapping("/api/records/{birder}")
    fun getAllRecords(@PathVariable("birder") birder: String): ResponseEntity<List<BirdingRecord>> {
        val result: MutableList<BirdingRecord> = mutableListOf()
        result.addAll(repository.findByRecorder(birder))
        return ResponseEntity.ok(result)
    }
}