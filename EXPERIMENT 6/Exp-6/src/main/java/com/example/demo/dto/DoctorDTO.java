package com.example.demo.dto;

import jakarta.validation.constraints.NotBlank;

public class DoctorDTO {

    public Long id;

    @NotBlank
    public String name;

    @NotBlank
    public String specialization;
}