package shop.birdyseoul.birdyseoulauthserver.dbaccess

import javax.persistence.Entity
import javax.persistence.GeneratedValue
import javax.persistence.GenerationType
import javax.persistence.Table
import javax.persistence.Id

@Entity
@Table(name = "BIRDERS")
class Birder(val emailAddress: String, val name: String) {

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    var id: Long = 0L

    override fun toString(): String {
        return "Birder[email=${this.emailAddress}, name=${this.name}]"
    }
}