

$( document ).ready(function() {
    console.log( "ready!" );

    $("#formulario").submit(function(e){
        e.preventDefault();
        var form = document.getElementById('formulario');

        if( form.checkValidity()){
            $("#myModal").modal("toggle");
        } else alert("Faltan campos por llenar. :(");     
    });

});
