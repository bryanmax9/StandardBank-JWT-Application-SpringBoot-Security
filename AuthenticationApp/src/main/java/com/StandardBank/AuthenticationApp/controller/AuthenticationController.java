package com.StandardBank.AuthenticationApp.controller;
import com.StandardBank.AuthenticationApp.model.JwtUtil;
import com.StandardBank.AuthenticationApp.service.AuthenticationService;
import com.StandardBank.AuthenticationApp.model.UserCredentials;
import com.StandardBank.AuthenticationApp.service.AuthenticationService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/authenticate")
public class AuthenticationController {

    @Autowired
    private AuthenticationService authenticationService;

    @Autowired
    private JwtUtil jwtUtil;

    @PostMapping
    public ResponseEntity<String> authenticate(@RequestBody UserCredentials userCredentials) {
        System.out.println(userCredentials.getUsername() + " " + userCredentials.getPasswordHash());
        if (authenticationService.authenticate(userCredentials.getUsername(), userCredentials.getPasswordHash())) {
            String token = jwtUtil.generateToken(userCredentials.getUsername());
            return ResponseEntity.ok(token);
        } else {
            return ResponseEntity.status(401).body("Unauthorized");
        }
    }
}
