import org.jetbrains.kotlin.gradle.tasks.KotlinCompile

plugins {
	id("org.springframework.boot") version "2.4.2"
	id("io.spring.dependency-management") version "1.0.11.RELEASE"
	kotlin("jvm") version "1.4.21"
	kotlin("plugin.spring") version "1.4.21"
}

group = "shop.birdyseoul"
version = "0.0.1-SNAPSHOT"
java.sourceCompatibility = JavaVersion.VERSION_1_8

repositories {
	mavenCentral()
}

dependencies {
	implementation("org.springframework.boot:spring-boot-starter-data-mongodb")
	implementation("org.springframework.boot:spring-boot-starter-web")
	implementation("org.springframework.boot:spring-boot-starter-security")
	implementation("com.fasterxml.jackson.module:jackson-module-kotlin")
	implementation("io.jsonwebtoken:jjwt-api:0.11.2")
	implementation("org.jetbrains.kotlin:kotlin-reflect")
	implementation("org.jetbrains.kotlin:kotlin-stdlib-jdk8")
	testImplementation("org.springframework.boot:spring-boot-starter-test")
	runtimeOnly("io.jsonwebtoken:jjwt-impl:0.11.2")
	runtimeOnly("io.jsonwebtoken:jjwt-jackson:0.11.2")
}

val webappDir = "$projectDir/src/main/frontend-react"

sourceSets {
	main {
		resources {
			srcDirs.add(File("$webappDir/build"))
		}
	}
}

tasks.withType<ProcessResources> {
	// dependsOn("copyFront")
}

tasks.register<Copy>("copyFront") {
	dependsOn("buildReact")
	from("$webappDir/build/")
	into("$projectDir/src/main/resources/static/")
}

tasks.register<Exec>("installReact") {
	workingDir = File(webappDir)
	inputs.dir(webappDir)
	group = BasePlugin.BUILD_GROUP
	if(System.getProperty("os.name").toLowerCase().contains("windows")) {
		commandLine("npm.cmd", "audit", "fix")
		commandLine("npm.cmd", "install")
	} else {
		commandLine("npm", "audit", "fix")
		commandLine("npm", "install")
	}
}

tasks.register<Exec>("buildReact") {
	dependsOn("installReact")
	workingDir = File(webappDir)
	inputs.dir(webappDir)
	group = BasePlugin.BUILD_GROUP
	if(System.getProperty("os.name").toLowerCase().contains("windows")) {
		commandLine("npm.cmd", "run-script", "build")
	} else {
		commandLine("npm", "run-script", "build")
	}
}

tasks.withType<KotlinCompile> {
	kotlinOptions {
		freeCompilerArgs = listOf("-Xjsr305=strict")
		jvmTarget = "1.8"
	}
}

tasks.withType<Test> {
	useJUnitPlatform()
}
