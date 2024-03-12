#!/bin/sh
#firstly, install opensll
#secondly, generate rsa or ecdsa key
#[rsa generate key]
./openssl genrsa -out private.pem 2048
./openssl rsa -in private.pem -outform PEM -pubout -out public.pem

#[ecdsa generate key]
./openssl ecparam -name prime256v1 -genkey -noout -out private.pem
./openssl ec -in private.pem -pubout -out public.pem