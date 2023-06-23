const signUpLink = document.querySelector('.register-link');
const signInLink = document.querySelector('.login-link');
const loginContainer = document.querySelector('.login');
const registerContainer = document.querySelector('.register');
const loginBtn = document.querySelector('.login-btn');
const registerBtn = document.querySelector('.register-btn');
const nameReg = document.querySelector('.name-reg');
const emailReg = document.querySelector('.email-reg');
const passwordReg = document.querySelector('.password-reg');
const repeatReg = document.querySelector('.repeat-reg');
const emailLog = document.querySelector('.email-log');
const passwordLog = document.querySelector('.password-log');
const inputBox = document.querySelector('.input-box');
const boxBox = document.querySelector('.box-box');
signUpLink.addEventListener('click', function(e) {
    e.preventDefault();
    loginContainer.classList.add('fade-out');
    registerContainer.classList.add('hidden');
    registerContainer.classList.remove('hidden');
    setTimeout(function() {
        loginContainer.classList.add('hidden');
        loginContainer.classList.remove('fade-out');
        registerContainer.classList.remove('fade-in');
    }, 500);
});

signInLink.addEventListener('click', function(e) {
    e.preventDefault();
    registerContainer.classList.add('fade-out');
    loginContainer.classList.add('hidden');
    loginContainer.classList.remove('hidden');
    setTimeout(function() {
        registerContainer.classList.add('hidden');
        registerContainer.classList.remove('fade-out');
        loginContainer.classList.remove('fade-in');
    }, 500);
});




