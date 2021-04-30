package shop.birdyseoul.birdobservation.birding.models

import org.springframework.data.annotation.Id

data class BirdOrder(
    @Id
    val id: String?,
    val name: String,
    val korName: String?,
    val families: List<BirdFamily>
)

data class BirdFamily(
    @Id
    val id: String?,
    val name: String,
    val korName: String?,
    val species: List<BirdSpecies>
)

data class BirdSpecies(
    @Id
    val eBirdCode: String,
    val engName: String,
    val scientificName: String,
    val korName: String?,
    val subSpecies: List<SubSpecies>
)

data class SubSpecies(
    val postfix: String,
    val korName: String?
)

