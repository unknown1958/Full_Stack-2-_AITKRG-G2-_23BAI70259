package com.example.demo.controller;

import com.example.demo.entity.Appointment;
import com.example.demo.repository.AppointmentRepository;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
@RequestMapping("/appointments")
public class AppointmentController {

    private final AppointmentRepository repo;

    public AppointmentController(AppointmentRepository repo) {
        this.repo = repo;
    }

    @PostMapping
    public Appointment add(@RequestBody Appointment a) {
        return repo.save(a);
    }

    // Cursor pagination
    @GetMapping("/after/{id}")
    public List<Appointment> getAfter(@PathVariable Long id) {
        return repo.findByIdGreaterThanOrderByIdAsc(id);
    }
}