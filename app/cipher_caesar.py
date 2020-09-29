#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string

class Caesar(object):
    def __init__(self):
        self.ALPHABET = string.ascii_letters
	
    def character_type(self, character):
        """ Returns the alphabet box """
        if character.isupper():
            return string.ascii_uppercase
        
        return string.ascii_lowercase
    
    def encrypt(self, text: str, key: int) -> str:
        """ Returns the encrypted text """
        ENCRYPT_TEXT = ""
        
        for letter in text:
            if letter in self.ALPHABET:
                alphabet =  self.character_type(letter)
                index = alphabet.index(letter) + key
                
                ENCRYPT_TEXT += alphabet[index % len(alphabet)]
                
            if letter not in self.ALPHABET:
                ENCRYPT_TEXT += letter
                
        return ENCRYPT_TEXT
    
    def decrypt(self, cipher: str, key: int) -> str:
        """ Returns the decrypted text """
        DECRYPT_TEXT = ""
        
        for letter in cipher:
            if letter in self.ALPHABET:
                alphabet =  self.character_type(letter)
                index = alphabet.index(letter) - key
                
                DECRYPT_TEXT += alphabet[index % len(alphabet)]
                
            if letter not in self.ALPHABET:
                DECRYPT_TEXT += letter
                
        return DECRYPT_TEXT
    
    
    