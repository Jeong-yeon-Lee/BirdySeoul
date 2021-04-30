package shop.birdyseoul.birdobservation.birding.models

import org.springframework.data.annotation.Id

data class BirdingSpot(
    @Id val id: String?,
    val environment: Environment,
    val species: List<String>,
)

/**
 * 탐조지의 환경에 대한 정보를 표현하기 위한 클래스.
 * 산, 강, 바다, 숲, 초지 등의 유형
 * 침엽수/활엽수/관목 등 나무의 유형 등이 기록되면 좋을 듯.
 * 서식지 유형을 구조화하려면 어떻게 해야할지
 */
data class Environment(
    val description: String?
)