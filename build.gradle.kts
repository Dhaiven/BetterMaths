plugins {
    id("java")
}

group = "org.bettermaths"
version = "1.0-SNAPSHOT"

repositories {
    mavenCentral()
    maven {
        url = uri("https://mvnrepository.com/artifact/org.apache.commons/commons-lang3")
    }
}

dependencies {
    // https://mvnrepository.com/artifact/org.apache.commons/commons-lang3
    //implementation(group = "org.apache.commons", name = " commons-lang", version = "3.17.0")
    implementation("org.apache.commons:commons-lang3:3.18.0")
    testImplementation(platform("org.junit:junit-bom:5.10.0"))
    testImplementation("org.junit.jupiter:junit-jupiter")
    implementation("org.riversun:java-promise:1.1.0")
}

tasks.test {
    useJUnitPlatform()
}