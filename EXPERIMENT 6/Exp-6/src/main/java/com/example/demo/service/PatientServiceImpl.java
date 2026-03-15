package com.example.demo.service;

import com.example.demo.dto.PatientDTO;
import com.example.demo.entity.Patient;
import com.example.demo.repository.PatientRepository;

import org.springframework.stereotype.Service;

import java.util.List;
import java.util.stream.Collectors;

@Service
public class PatientServiceImpl implements PatientService {

    private final PatientRepository repo;

    public PatientServiceImpl(PatientRepository repo) {
        this.repo = repo;
    }

    private PatientDTO toDTO(Patient p) {
        PatientDTO d = new PatientDTO();
        d.id = p.getId();
        d.name = p.getName();
        d.email = p.getEmail();
        d.age = p.getAge();
        return d;
    }

    private Patient toEntity(PatientDTO d) {
        Patient p = new Patient();
        p.setId(d.id);
        p.setName(d.name);
        p.setEmail(d.email);
        p.setAge(d.age);
        return p;
    }

    public PatientDTO create(PatientDTO dto) {
        return toDTO(repo.save(toEntity(dto)));
    }

    public List<PatientDTO> getAll() {
        return repo.findAll().stream().map(this::toDTO).collect(Collectors.toList());
    }
}