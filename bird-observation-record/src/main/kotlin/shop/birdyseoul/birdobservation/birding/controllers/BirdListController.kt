package shop.birdyseoul.birdobservation.birding.controllers

import com.google.gson.Gson
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.core.io.ClassPathResource
import org.springframework.security.core.annotation.AuthenticationPrincipal
import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.PostMapping
import org.springframework.web.bind.annotation.RestController
import shop.birdyseoul.birdobservation.birding.database.BirdOrdersRepository
import shop.birdyseoul.birdobservation.birding.models.BirdOrder
import java.io.File
import java.nio.file.Files

@RestController
class BirdListController(@Autowired val repo: BirdOrdersRepository) {

    @GetMapping("api/bird-list/init")
    fun initBirdListFromJson() {
        val resourceFile: File = ClassPathResource("data/birds.json").file
        val dataStr = String(Files.readAllBytes(resourceFile.toPath()))
        val orders: List<BirdOrder> = Gson().fromJson(dataStr, Array<BirdOrder>::class.java).toList()
        this.repo.saveAll(orders)
    }
}