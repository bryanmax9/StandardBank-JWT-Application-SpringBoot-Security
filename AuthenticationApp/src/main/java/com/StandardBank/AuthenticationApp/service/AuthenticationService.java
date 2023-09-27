package com.StandardBank.AuthenticationApp.service;
import org.springframework.stereotype.Service;

@Service
public class AuthenticationService {

    // For simplicity, hardcoding username and password hash.
    private final String USERNAME = "user";
    private final String PASSWORD_HASH = "5f4dcc3b5aa765d61d8327deb882cf99"; // md5 hash for "password"

    public boolean authenticate(String username, String passwordHash) {
        return USERNAME.equals(username) && PASSWORD_HASH.equals(passwordHash);
    }
}

