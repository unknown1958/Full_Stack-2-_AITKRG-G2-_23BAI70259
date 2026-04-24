package com.example.secureapp.service;

import com.example.secureapp.model.Role;
import com.example.secureapp.model.User;
import com.example.secureapp.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.cache.annotation.Cacheable;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class UserService {

    @Autowired
    private UserRepository userRepository;

    @Cacheable("users")
    public List<User> getAllUsers() {
        return userRepository.findAll();
    }

    @Cacheable("user")
    public Optional<User> getUserById(Long id) {
        return userRepository.findById(id);
    }

    public User createUser(String email, String name, Role role) {
        User user = new User(email, name, role);
        return userRepository.save(user);
    }

    public Optional<User> findByEmail(String email) {
        return userRepository.findByEmail(email);
    }
}