package shop.birdyseoul.birdobservation.models

import org.springframework.data.annotation.Id
import shop.birdyseoul.birdobservation.birders.Birder
import java.util.*

data class BirdingRecord(
    @Id
    val id: String?,

    val recorder: String,
    val observer: List<String>?,
    val date: Date,
    val startTime: Date?,
    val endTime: Date?,
    val location: String?,
    val observations: List<Observation>
)

data class Observation (
    val species: String,
    val time: Date?
)