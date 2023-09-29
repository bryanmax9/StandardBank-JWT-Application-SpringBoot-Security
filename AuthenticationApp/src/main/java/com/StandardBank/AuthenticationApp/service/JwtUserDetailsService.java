package com.StandardBank.AuthenticationApp.service;

import org.springframework.security.core.userdetails.User;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;
import org.springframework.core.io.ClassPathResource;
import org.springframework.core.io.Resource;

import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Service
public class JwtUserDetailsService implements UserDetailsService {

    // Map to store username-password pairs
    private Map<String, String> userMap = new HashMap<>();

    // Constructor to initialize the userMap from a file
    public JwtUserDetailsService() {
        try {
            // Load user credentials from a file (e.g., "credentials.txt" on the classpath)
            Resource resource = new ClassPathResource("credentials.txt");
            List<String> lines = Files.readAllLines(Paths.get(resource.getURI()));

            // Parse and populate the userMap with username-password pairs
            for (String line : lines) {
                String[] parts = line.split(":");
                if (parts.length == 2) {
                    userMap.put(parts[0], parts[1]);
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    // Implementation of the UserDetailsService interface method to load a user by username
    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
        // Retrieve the encoded password for the given username from the userMap
        String encodedPassword = userMap.get(username);
        if (encodedPassword != null) {
            // Create a UserDetails object with the retrieved username and password
            return new User(username, encodedPassword, new ArrayList<>());
        } else {
            // If the username is not found, throw an exception
            throw new UsernameNotFoundException("User not found with username: " + username);
        }
    }
}
