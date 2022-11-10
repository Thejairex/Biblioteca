const formulario = document.getElementById('formulario');
const inputs = document.querySelectorAll('.form-control');


const expresiones = {
    usuario: /^.{2,300}$/, // Letras, numeros, guion y guion_bajo
    nombre: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
    password: /^.{8,24}$/, // 8 a 24 digitos.
    correo: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
    telefono: /^\d{7,14}$/, // 7 a 14 numeros.
    capitulo: /^\d{1,5}$/ // 1 a 5 numeros.
}

const campos = {
    Nombre: false,
    Capitulos: false,
    Temporadas: false,
    Tipo: false,
    Autor: false
}

const validarFormulario = (e) => {
    switch (e.target.name) {
        case "nombre":
            validadCampo(expresiones.usuario, e.target, 'Nombre');
            
            break;
        case "capitulos":
            validadCampo(expresiones.capitulo, e.target, 'Capitulos');
            break;
        
        case "Temporadas":
            validadCampo(expresiones.capitulo, e.target, 'Temporadas')
            break;

        case "Autor":
            validadCampo(expresiones.nombre, e.target, 'Autor')
            break;
        
        case "tipo":
            validarTipo(e.target, 'Tipo')
            break
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

const validarTipo = (input, campo) => {
    if (input.value != "") {
        document.getElementById(`${campo}`).classList.remove('border-danger');
        document.getElementById(`${campo}`).classList.add('border-success');
        document.querySelector(`#error_${campo}.formulario__input-error`).classList.remove('formulario__input-error-activo');
        campos[campo] = true;
        validadDatos();
    } else{
        document.getElementById(`${campo}`).classList.add('border-danger');
        document.querySelector(`#error_${campo}.formulario__input-error`).classList.add('formulario__input-error-activo');
        campos[campo] = false;
        validadDatos();
    }
}

inputs.forEach((input) => {
    input.addEventListener('keyup', validarFormulario);
    input.addEventListener('blur', validarFormulario);
    input.addEventListener('change', validarFormulario)
});

const validadDatos = () => {
    if (campos.Nombre===true && campos.Capitulos===true && campos.Tipo===true && ( campos.Temporadas===true || campos.Autor===true ) ) {
        document.getElementById("btn-form").classList.remove("disabled");
    } else {
        document.getElementById("btn-form").classList.add("disabled");
    }
};