package com.example.demo.service;

import com.example.demo.dto.PatientDTO;
import java.util.List;

public interface PatientService {

    PatientDTO create(PatientDTO dto);
    List<PatientDTO> getAll();
}