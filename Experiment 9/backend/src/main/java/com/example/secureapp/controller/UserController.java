package com.example.secureapp.controller;

import com.example.secureapp.model.User;
import com.example.secureapp.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.security.oauth2.core.user.OAuth2User;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api")
public class UserController {

    @Autowired
    private UserService userService;

    @GetMapping("/user")
    public String user(@AuthenticationPrincipal OAuth2User principal) {
        return "Hello, " + principal.getAttribute("name");
    }

    @GetMapping("/public")
    public String publicEndpoint() {
        return "This is public";
    }

    @GetMapping("/users")
    @PreAuthorize("hasRole('ADMIN')")
    public List<User> getUsers() {
        return userService.getAllUsers();
    }

    @PostMapping("/users")
    @PreAuthorize("hasRole('ADMIN')")
    public User createUser(@RequestBody User user) {
        return userService.createUser(user.getEmail(), user.getName(), user.getRole());
    }
}