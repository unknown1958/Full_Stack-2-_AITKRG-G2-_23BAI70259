package org.example.livepollbackend.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class PollController {

    // Home page (fixes 404 after login)
    @GetMapping("/")
    public String home() {
        return "Welcome! Google login successful 🎉";
    }

    // USER endpoint
    @GetMapping("/user/vote")
    public String vote() {
        return "User voted successfully!";
    }

    // ADMIN endpoint
    @GetMapping("/admin/create")
    public String createPoll() {
        return "Poll created successfully!";
    }
}