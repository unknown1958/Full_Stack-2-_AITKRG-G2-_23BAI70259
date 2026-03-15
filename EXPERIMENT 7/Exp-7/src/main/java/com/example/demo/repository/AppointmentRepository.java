package com.example.demo.repository;

import com.example.demo.entity.Appointment;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.List;

public interface AppointmentRepository
        extends JpaRepository<Appointment, Long> {

    // Cursor-based pagination
    List<Appointment> findByIdGreaterThanOrderByIdAsc(Long id);
}