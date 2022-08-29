extern crate crypto;
extern crate base64;
extern crate hex;
extern crate rustc_serialize;
use std::env;
use std::process::Command;
use std::str;
use std::fs::File;
use std::io::prelude::*;
use crypto::aes_gcm::AesGcm;
use crypto::aead::{AeadDecryptor};
use rustc_serialize::hex::FromHex;
// use core::str;
use std::iter::repeat;

fn main(){
    let args: Vec<String> = env::args().collect();
    let cuenta = args.len();
    if cuenta > 3 {
        return
    }else {
        let comando: Vec<&str> = args[1].split(':').collect();
        // let comando_arr : Vec<&str> = comando.collect();
        // println!("{:?}", comando);
        let opcode_1 = comando[0];
        let opcode_2 = comando[1];
        if opcode_1 == "9" {
            if opcode_2 == "F" {
                    ascii_hackdef();
                }else if opcode_2 == "9"{
                    print_some();
                }else if opcode_2 == "0"{
                    follow_me_on_twitch();
                }else {
                    no_valido();
                }
        }else if opcode_1 == "8" {
            if opcode_2 == "E"{
                    print_help();

                }else if opcode_2 == "7"{
                    chall_desc();
                }else if opcode_2 == "8"{
                    flag_f();
                }else{
                    no_valido();
                }
        }else if opcode_1 == "7"{
                if opcode_2 == "D" {
                    let nombre = get_name(args);
                    say_hello(nombre);
                } else if opcode_2 == "2"{
                    flag_s();
                } else if opcode_2 == "3"{
                    let uname = get_name(args);
                    let unam3 = base64::decode("bm90bWFsYWZhbWE=").unwrap();
                    if uname == String::from_utf8_lossy(&unam3){
                        flag_c();
                    }else{
                        print!("Usuario no valido!")
                    }
                }else {
                    no_valido();
                }
        }else {
            no_valido();
        }
    }
}

fn flag_c() -> std::io::Result<()>{
    let mykey = "a6794bc04afe816b51ddd6e3454c29de";
    let myiv = "39e0b057ae6efa5c03dada43";
    let myadd = "HACKDEF6QUALS";

    let key_size = crypto::aes::KeySize::KeySize128;
    
    let key=&hex_to_bytes( mykey)[..];
    let iv=&hex_to_bytes( myiv)[..];
    let add=myadd.as_bytes();
    
    let out_tag: Vec<u8> = vec![51, 105, 19, 139, 27, 181, 60, 177, 241, 246, 99, 225, 36, 153, 194, 141];
    
    let mut decipher = AesGcm::new(key_size, key, iv, add);
    
    let out: Vec<u8> = vec![106, 78, 208, 26, 195, 76, 25, 79, 245, 5, 209, 58, 205, 154, 199, 144, 2, 2, 84, 173, 82, 207, 190, 230, 160, 156, 21, 14, 79, 51, 60, 183, 53, 100, 231, 223, 143, 114, 17, 86, 114, 69, 137, 238, 84];
    // println!("{:?}", out);
    let mut out2: Vec<u8> = repeat(0).take(45).collect();
    // println!("comienza a decriptar");
    let result = decipher.decrypt(&out[..], &mut out2[..], &out_tag[..]);
    // println!("termina decriptar");
    if result == true {
    println!("\nWelcome back Sir all systems for CTF gaming will be prepared in a few minutes.\nFor now, feel free to grab your flag\n{}",str::from_utf8(&out2[..]).unwrap());
    }
    Ok(())
}
fn hex_to_bytes(s: &str) -> Vec<u8> {
    s.from_hex().unwrap()
}
fn flag_s() -> std::io::Result<()>{
    let mut file = File::create("/tmp/flag.txt")?;
    file.write_all(b"6861636B6465667B657374615F74616D706F636F5F65735F6C615F666C61675F76656E67617D")?;
    Ok(())
}
fn get_name(params: Vec<String>) -> String{
    if params.len() == 3{
        let s = &params[2];
        return s.to_string();
    } else {
        let cmd = Command::new("whoami").output().expect("fallo al ejecutar el comando");
        let name = cmd.stdout;
        let s = String::from_utf8_lossy(&name);
        return s.to_string();
    }
}
fn say_hello(n : String){
    println!("Hello, {}", n);
}
fn flag_f(){
    println!("hackdef{{{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}}}", 110,111,95,101,115,116,97,95,110,111,95,101,115,95,108,97,95,102,108,97,103);
}
fn chall_desc(){
    println!("Reversing RUST 101\nYa habias escuhado del lenguaje RUST?");
}
fn print_help(){
    println!("./binary_name X:Y second_param <optional>\nX=[0..9]\nY=[0..F]\nsecond_param is optional\nExample:./rev_400 5:A");
}
fn ascii_hackdef(){
    let p1 = r"  ___ ___                __    ________          _____    ________ ________               .__          ";
    let p2 = r"/   |   \_____    ____ |  | __\______ \   _____/ ____\  /  _____/ \_____  \  __ _______  |  |   ______";
    let p3 = r"/    ~    \__  \ _/ ___\|  |/ / |    |  \_/ __ \   __\  /   __  \   /  / \  \|  |  \__  \ |  |  /  ___/";
    let p4 = r"\    Y    // __ \\  \___|    <  |    `   \  ___/|  |    \  |__\  \ /   \_/.  \  |  // __ \|  |__\___ \ ";
    let p5 = r" \___|_  /(____  /\___  >__|_ \/_______  /\___  >__|     \_____  / \_____\ \_/____/(____  /____/____  >";
    let p6 = r"       \/      \/     \/     \/        \/     \/               \/         \__>          \/          \/ ";
    println!("{}",p1);
    println!("{}",p2);
    println!("{}",p3);
    println!("{}",p4);
    println!("{}",p5);
    println!("{}",p6);
}

fn print_some(){
    println!("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\nUt enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.\nExcepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.");
}

fn follow_me_on_twitch(){
    println!("Followme on Twitch,\nstream every Thursday on twitch.tv/bm90bWFsYWZhbWE=");
}

fn no_valido(){
    println!("OPCODE no valido =(");
}