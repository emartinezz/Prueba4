function validardatos(){
    var Nombre = document.getElementById("txt-Nombre").value;
    var Apellido = document.getElementById("txt-Apellido").value;
    var Contraseña = document.getElementById("txt-Contraseña").value;
    var rut = document.getElementById("rut").value;
  
    if (Nombre.trim() == ""){

        document.getElementById("error-nombre").style.visibility = "visible";
    }
    else
    {
     
        document.getElementById("error-nombre").style.visibility = "hidden";
    }

    if (Apellido== ""){
    
        document.getElementById("error-Apellido").style.visibility = "visible";
    }
    else
    {
    
        document.getElementById("error-Apellido").style.visibility = "hidden";
    }
 
   
    if (Contraseña  == ""){
    
        document.getElementById("error-Contraseña").style.visibility = "visible";
    }
    else
    {
    
        document.getElementById("error-Contraseña").style.visibility = "hidden";
    }

    if (rut.trim() == ""){

        document.getElementById("error-rut").style.visibility = "visible";

    }
    else
    {
        document.getElementById("error-rut").style.visibility = "hidden"; 
    }
 }
