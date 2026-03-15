package com.example.demo.repository;

import com.example.demo.entity.Doctor;
import org.springframework.data.jpa.repository.*;
import java.util.List;

public interface DoctorRepository extends JpaRepository<Doctor, Long> {

    // JPQL Query (Objective 2)
    @Query("SELECT d FROM Doctor d WHERE d.specialization = :spec")
    List<Doctor> findBySpecialization(String spec);

    // Solve N+1 Problem
    @Query("SELECT d FROM Doctor d JOIN FETCH d.appointments")
    List<Doctor> findAllWithAppointments();
}