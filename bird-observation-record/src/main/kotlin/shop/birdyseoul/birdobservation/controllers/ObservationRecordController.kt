package shop.birdyseoul.birdobservation.controllers

import org.springframework.beans.factory.annotation.Autowired
import org.springframework.http.HttpStatus
import org.springframework.http.ResponseEntity
import org.springframework.security.core.context.SecurityContextHolder
import org.springframework.web.bind.annotation.*
import shop.birdyseoul.birdobservation.models.BirdingRecord
import shop.birdyseoul.birdobservation.dbaccess.BirdingRecordRepository
import javax.servlet.http.HttpServletResponse

@RestController
class ObservationRecordController {

    @Autowired
    lateinit var repository: BirdingRecordRepository

    @PostMapping(path = ["/api/record/create"], consumes = ["application/json"])
    @ResponseStatus(HttpStatus.CREATED)
    fun addRecord(@RequestBody record: BirdingRecord): ResponseEntity<String> {
        val userName = SecurityContextHolder.getContext().authentication.name
        if (userName != record.recorder) {
            val response = ResponseEntity<String>("Wrong Request", HttpStatus.FORBIDDEN);
            return response;
        }
        this.repository.save(record)
        return ResponseEntity.ok("Successfully saved a birding record!")
    }

//    @PostMapping(path = ["/api/observations"], consumes = ["application/json"])
//    @ResponseStatus(HttpStatus.CREATED)
//    fun addRecords(birder: String, records: List<BirdingRecord>) {
//            this.repository.saveAll(records)
//    }

    @GetMapping("/api/records/{birder}")
    fun getAllRecords(@PathVariable("birder") birder: String): ResponseEntity<List<BirdingRecord>> {
        val result: MutableList<BirdingRecord> = mutableListOf()
        result.addAll(repository.findByRecorder(birder))
        return ResponseEntity.ok(result)
    }
}