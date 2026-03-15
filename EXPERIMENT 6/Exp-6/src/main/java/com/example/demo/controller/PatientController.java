package com.example.demo.controller;

import com.example.demo.dto.PatientDTO;
import com.example.demo.service.PatientService;

import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/patients")
public class PatientController {

    private final PatientService service;

    public PatientController(PatientService service) {
        this.service = service;
    }

    @PostMapping
    public PatientDTO create(@RequestBody PatientDTO dto) {
        return service.create(dto);
    }

    @GetMapping
    public List<PatientDTO> getAll() {
        return service.getAll();
    }
}