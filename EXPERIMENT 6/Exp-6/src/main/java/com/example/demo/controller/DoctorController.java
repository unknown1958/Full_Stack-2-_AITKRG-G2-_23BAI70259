package com.example.demo.controller;

import com.example.demo.dto.DoctorDTO;
import com.example.demo.entity.Doctor;
import com.example.demo.repository.DoctorRepository;

import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/doctors")
public class DoctorController {

    private final DoctorRepository repo;

    public DoctorController(DoctorRepository repo) {
        this.repo = repo;
    }

    @PostMapping
    public Doctor create(@RequestBody Doctor d) {
        return repo.save(d);
    }

    @GetMapping
    public List<Doctor> getAll() {
        return repo.findAll();
    }
}