package com.example.demo.entity;

import jakarta.persistence.*;

@Entity
@Table(
    name = "appointments",
    indexes = @Index(name = "idx_patient_name", columnList = "patientName")
)
public class Appointment {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String patientName;

    private String date;

    // Many Appointments → One Doctor
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "doctor_id")
    private Doctor doctor;

    // getters & setters
}