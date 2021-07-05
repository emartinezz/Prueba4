
var alerta = document.getElementById("alerta");
var mensaje = document.getElementById("mensaje");


function isNumber(evt) {
  var charCode = evt.which ? evt.which : event.keyCode;
  if (charCode > 31 && (charCode < 48 || charCode > 57) && charCode === 75) return false;

  return true;
}

function checkRut(rut) {

  if (rut.value.length <= 1) {
    alerta.classList.remove('alert-success', 'alert-danger');
    alerta.classList.add('alert-info');
    mensaje.innerHTML = 'Ingrese su  RUT ';
  }


  var valor = clean(rut.value);


  cuerpo = valor.slice(0, -1);
  dv = valor.slice(-1).toUpperCase();

 
  rut.value = format(rut.value);


  if (cuerpo.length < 7) {
   
    alerta.classList.remove('alert-success', 'alert-danger');
    alerta.classList.add('alert-info');
    mensaje.innerHTML = 'su rut es invalido. Ej: x.xxx.xxx-x';
    return false;
  }

 
  suma = 0;
  multiplo = 2;

  
  for (i = 1; i <= cuerpo.length; i++) {
    
    index = multiplo * valor.charAt(cuerpo.length - i);

   
    suma = suma + index;


    if (multiplo < 7) {
      multiplo = multiplo + 1;
    } else {
      multiplo = 2;
    }
  }


  dvEsperado = 11 - (suma % 11);


  dv = dv == "K" ? 10 : dv;
  dv = dv == 0 ? 11 : dv;


  if (dvEsperado != dv) {


    alerta.classList.remove('alert-info', 'alert-success');
    alerta.classList.add('alert-danger');
    mensaje.innerHTML = 'El RUT  Es <strong>INCORRECTO</strong>.';

    return false;
  } else {


    alerta.classList.remove('d-none', 'alert-danger');
    alerta.classList.add('alert-success');
    mensaje.innerHTML = 'El RUT  Es <strong>CORRECTO</strong>.';
    return true;
  }
}

function format (rut) {
  rut = clean(rut)

  var result = rut.slice(-4, -1) + '-' + rut.substr(rut.length - 1)
  for (var i = 4; i < rut.length; i += 3) {
    result = rut.slice(-3 - i, -i) + '.' + result
  }

  return result
}

function clean (rut) {
  return typeof rut === 'string'
    ? rut.replace(/^0+|[^0-9kK]+/g, '').toUpperCase()
    : ''
}
