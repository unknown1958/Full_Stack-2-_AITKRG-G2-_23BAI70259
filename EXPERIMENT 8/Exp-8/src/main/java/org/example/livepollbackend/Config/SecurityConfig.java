package org.example.livepollbackend.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.web.SecurityFilterChain;
import org.springframework.security.core.userdetails.*;
import org.springframework.security.provisioning.InMemoryUserDetailsManager;

@Configuration
public class SecurityConfig {

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {

        http
                .csrf(csrf -> csrf.disable())

                .authorizeHttpRequests(auth -> auth
                        .requestMatchers("/admin/**").hasRole("ADMIN")   // only admin
                        .requestMatchers("/user/**").authenticated()     // any logged-in user (Google or form)
                        .anyRequest().authenticated()
                )

                .formLogin(form -> {})   // normal login

                .oauth2Login(oauth -> oauth
                        .defaultSuccessUrl("/user/vote", true)   // after Google login
                );

        return http.build();
    }

    // In-memory users (for admin testing)
    @Bean
    public UserDetailsService userDetailsService() {
        return new InMemoryUserDetailsManager(

                User.withDefaultPasswordEncoder()
                        .username("user")
                        .password("1234")
                        .roles("USER")
                        .build(),

                User.withDefaultPasswordEncoder()
                        .username("admin")
                        .password("1234")
                        .roles("ADMIN")
                        .build()
        );
    }
}