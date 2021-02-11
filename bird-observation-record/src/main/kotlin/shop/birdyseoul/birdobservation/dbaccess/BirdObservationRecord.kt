package shop.birdyseoul.birdobservation.dbaccess

import org.springframework.data.annotation.Id

data class BirdObservationRecord(
    @Id
    val id: String,

    val species: String,
    val observer: String,
    val date: String,
    val time: String,
    val location: String
)
