package shop.birdyseoul.birdyseoulauthserver.dbaccess

import org.springframework.data.repository.CrudRepository


interface BirderRepository: CrudRepository<Birder, Int> {

}