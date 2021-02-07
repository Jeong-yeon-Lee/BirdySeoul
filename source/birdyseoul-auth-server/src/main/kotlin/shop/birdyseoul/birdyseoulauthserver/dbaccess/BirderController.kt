package shop.birdyseoul.birdyseoulauthserver.dbaccess

import org.springframework.beans.factory.annotation.Autowired
import org.springframework.stereotype.Controller
import org.springframework.web.bind.annotation.*

@Controller
@RequestMapping("/demo")
class BirderController {

    @Autowired
    private lateinit var birderRepository: BirderRepository

    @PostMapping("/add")
    @ResponseBody
    fun addNewBirder(@RequestParam name: String, @RequestParam email: String): String {
        val newBirder = Birder(email, name)
        this.birderRepository.save(newBirder)
        return "saved"
    }

    @GetMapping("/all")
    @ResponseBody fun getAllUsers(): MutableIterable<Birder> {
        return this.birderRepository.findAll()
    }
}