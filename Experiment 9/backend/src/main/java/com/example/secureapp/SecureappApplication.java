package com.example.secureapp;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cache.annotation.EnableCaching;

@SpringBootApplication
@EnableCaching
public class SecureappApplication {

    public static void main(String[] args) {
        SpringApplication.run(SecureappApplication.class, args);
    }

}