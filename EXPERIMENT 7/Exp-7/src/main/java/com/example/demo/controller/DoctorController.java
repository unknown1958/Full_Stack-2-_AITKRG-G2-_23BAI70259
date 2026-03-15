package com.example.demo.controller;

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
    public Doctor addDoctor(@RequestBody Doctor d) {
        return repo.save(d);
    }

    @GetMapping
    public List<Doctor> getAll() {
        return repo.findAll();
    }

    @GetMapping("/specialization/{spec}")
    public List<Doctor> bySpec(@PathVariable String spec) {
        return repo.findBySpecialization(spec);
    }

    @GetMapping("/with-appointments")
    public List<Doctor> allWithAppointments() {
        return repo.findAllWithAppointments();
    }
}