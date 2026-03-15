package com.example.demo.controller;

import com.example.demo.dto.AppointmentDTO;
import com.example.demo.entity.*;
import com.example.demo.repository.*;

import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/appointments")
public class AppointmentController {

    private final AppointmentRepository apptRepo;
    private final PatientRepository patientRepo;
    private final DoctorRepository doctorRepo;

    public AppointmentController(AppointmentRepository a,
                                 PatientRepository p,
                                 DoctorRepository d) {
        this.apptRepo = a;
        this.patientRepo = p;
        this.doctorRepo = d;
    }

    @PostMapping
    public Appointment create(@RequestBody AppointmentDTO dto) {

        Patient p = patientRepo.findById(dto.patientId).orElseThrow();
        Doctor d = doctorRepo.findById(dto.doctorId).orElseThrow();

        Appointment appt = new Appointment();
        appt.setAppointmentDate(dto.appointmentDate);
        appt.setPatient(p);
        appt.setDoctor(d);

        return apptRepo.save(appt);
    }

    @GetMapping
    public List<Appointment> getAll() {
        return apptRepo.findAll();
    }
}