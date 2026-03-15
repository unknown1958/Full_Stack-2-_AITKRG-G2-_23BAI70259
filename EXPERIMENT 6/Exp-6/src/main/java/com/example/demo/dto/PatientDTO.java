package com.example.demo.dto;

import jakarta.validation.constraints.*;

public class PatientDTO {

    public Long id;

    @NotBlank
    public String name;

    @Email
    public String email;

    public int age;
}