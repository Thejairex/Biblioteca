const formulario = document.getElementById('formulario');
const inputs = document.querySelectorAll('.form-control');


const expresiones = {
    usuario: /^[a-zA-Z0-9\_\-]{4,16}$/, // Letras, numeros, guion y guion_bajo
    nombre: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
    password: /^.{8,24}$/, // 8 a 24 digitos.
    correo: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
    telefono: /^\d{7,14}$/ // 7 a 14 numeros.
}

const campos = {
    Username: false,
    Password: false,
    Password2: false
}

const validarFormulario = (e) => {
    switch (e.target.name) {
        case "username":
            validadCampo(expresiones.usuario, e.target, 'Username');
            
            break;
        case "password":
            validadCampo(expresiones.password, e.target, 'Password');
            break;

        case "password2":
            validarPassword2();
            break;
    }
};

const validadCampo = (expresion, input, campo) => {
    if (expresion.test(input.value)) {
        document.getElementById(`${campo}`).classList.remove('border-danger');
        document.getElementById(`${campo}`).classList.add('border-success');
        document.querySelector(`#error_${campo}.formulario__input-error`).classList.remove('formulario__input-error-activo');
        campos[campo] = true;
        validadDatos();

    } else {
        document.getElementById(`${campo}`).classList.add('border-danger');
        document.querySelector(`#error_${campo}.formulario__input-error`).classList.add('formulario__input-error-activo');
        campos[campo] = false;
        validadDatos();
    }
}

const validarPassword2 = () => {
    const inputPassword1 = document.getElementById('Password');
    const inputPassword2 = document.getElementById('confirmPassword');

    if (inputPassword1.value !== inputPassword2.value) {
        document.getElementById(`confirmPassword`).classList.add('border-danger');
        document.querySelector(`#error_confirmPassword.formulario__input-error`).classList.add('formulario__input-error-activo');
        campos['Password2'] = false;
        validadDatos();
    } else {
        document.getElementById(`confirmPassword`).classList.remove('border-danger');
        document.getElementById(`confirmPassword`).classList.add('border-success');
        document.querySelector(`#error_confirmPassword.formulario__input-error`).classList.remove('formulario__input-error-activo');
        campos['Password2'] = true;
        validadDatos();
    }
}
inputs.forEach((input) => {
    input.addEventListener('keyup', validarFormulario);
    input.addEventListener('blur', validarFormulario);
});

const validadDatos = () => {
    if (campos.Username===true && campos.Password===true && campos.Password2===true) {
        document.getElementById("btn-form").classList.remove("disabled");
    } else {
        document.getElementById("btn-form").classList.add("disabled");
    }
};

formulario.addEventListener('submit', () => {
    
});