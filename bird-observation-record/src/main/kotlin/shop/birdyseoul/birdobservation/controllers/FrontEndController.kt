package shop.birdyseoul.birdobservation.controllers

import org.springframework.stereotype.Controller
import org.springframework.web.bind.annotation.RequestMapping

@Controller
class FrontEndController {

    @RequestMapping(value = ["/", "/{x:[\\w\\-]+}", "/{x:^(?!api$).*$}/**/{y:[\\w\\-]+}"])
    fun index(): String {
        println("ssjsj");
        return "/index.html"
    }
}